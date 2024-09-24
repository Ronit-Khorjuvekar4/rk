/* 1. What is the total amount each customer spent at the restaurant? */

select s.customer_id,sum(m.price) as Amount from sales s
left join menu m on 
m.product_id = s.product_id
group by s.customer_id;

/* How many days has each customer visited the restaurant?  */
select customer_id,count(distinct order_date) as visit_days from sales
group by customer_id;


/* What was the first item from the menu purchased by each customer?*/
SELECT s.customer_id, m.product_name, min(s.order_date) order_date
FROM sales s
JOIN menu m ON s.product_id = m.product_id
GROUP BY customer_id;

-- WITH ranked_orders AS (
--     SELECT s.customer_id, m.product_name, s.order_date,
--            ROW_NUMBER() OVER (PARTITION BY s.customer_id ORDER BY s.order_date) AS rn
--     FROM sales s
--     JOIN menu m ON s.product_id = m.product_id
-- )
-- SELECT customer_id, product_name
-- FROM ranked_orders
-- WHERE rn = 1;


/* What is the most purchased item on the menu and how many times was it purchased by each customers? */
with rankorder AS (
	select s.product_id,count(s.product_id) as purchase_count,m.product_name 
    from sales s
	join menu m on s.product_id = m.product_id
	group by s.product_id 
    order by purchase_count desc 
    limit 1
)
select s.customer_id,count(r.product_id) as products_purchased,r.product_name from rankorder r
join sales s on r.product_id = s.product_id
group by s.customer_id;


/* What is the most purchased item on the menu and how many times was it purchased by all customers? */
select s.product_id,count(s.product_id) as purchase_count,m.product_name 
    from sales s
	join menu m on s.product_id = m.product_id
	group by s.product_id 
    order by purchase_count desc 
    limit 1;


/* Which item was the most popular for each customer? */

WITH most_popular AS (
  SELECT 
    sales.customer_id, 
    menu.product_name, 
    COUNT(menu.product_id) AS order_count,
    DENSE_RANK() OVER (
      PARTITION BY sales.customer_id 
      ORDER BY COUNT(sales.customer_id) DESC) AS rank1
  FROM dannys_diner.menu
  INNER JOIN dannys_diner.sales
    ON menu.product_id = sales.product_id
  GROUP BY sales.customer_id, menu.product_name
)SELECT 
  customer_id, 
  product_name, 
  order_count
FROM most_popular 
WHERE rank1 = 1;


/*Which item was purchased first by the customer after they became a member? */
    
WITH first_purchase AS (
    SELECT s.customer_id, m.product_name, s.order_date,
           ROW_NUMBER() OVER (PARTITION BY s.customer_id ORDER BY s.order_date) AS rn
    FROM sales s
    JOIN menu m ON s.product_id = m.product_id
    JOIN members mem ON s.customer_id = mem.customer_id
    WHERE s.order_date > mem.join_date
)
SELECT customer_id, product_name, order_date
FROM first_purchase
WHERE rn = 1;


/*Which item was purchased just before the customer became a member? */

with before_member AS (
	select s.customer_id, s.order_date,m.product_id,ma.join_date, m.product_name,
    row_number() OVER (PARTITION BY s.customer_id order by s.order_date desc) ok
    from sales s
    join members ma on s.customer_id = ma.customer_id
    join menu m on s.product_id = m.product_id
    where ma.join_date > s.order_date
    order by s.customer_id,s.order_date
)select * from before_member where ok = 1;


/*What is the total items and amount spent for each member before they became a member? */

with before_member AS(
	select s.customer_id, s.order_date,m.product_id,ma.join_date, m.product_name, m.price
    from sales s
    join members ma on s.customer_id = ma.customer_id
    join menu m on s.product_id = m.product_id
	where ma.join_date > s.order_date
    order by s.customer_id,s.order_date
)select *,sum(price),count(product_id) from before_member
group by customer_id
order by customer_id;

/* Below is better solution */
SELECT 
  sales.customer_id, 
  COUNT(sales.product_id) AS total_items, 
  SUM(menu.price) AS total_sales
FROM dannys_diner.sales
INNER JOIN dannys_diner.members
  ON sales.customer_id = members.customer_id
  AND sales.order_date < members.join_date
INNER JOIN dannys_diner.menu
  ON sales.product_id = menu.product_id
GROUP BY sales.customer_id
ORDER BY sales.customer_id;

/*If each $1 spent equates to 10 points and sushi has a 2x points multiplier - how many points would each customer have?*/

select s.customer_id, sum(if(m.product_name = 'sushi',m.price * 2 * 10,m.price * 10)) as total_points from sales s
join menu m on m.product_id = s.product_id
group by customer_id
order by customer_id;



/*In the first week after a customer joins the program (including their join date) they earn 2x points on all items,
not just sushi - how many points do customer A and B have at the end of January?*/

    WITH dates_cte AS (
  SELECT 
    customer_id, 
      join_date, 
      join_date + 6 AS valid_date,
      '2021-01-31' AS last_date
  FROM dannys_diner.members
)SELECT 
  sales.customer_id, 
  SUM(CASE
    WHEN menu.product_name = 'sushi' THEN 2 * 10 * menu.price
    WHEN sales.order_date BETWEEN dates.join_date AND dates.valid_date THEN 2 * 10 * menu.price
    ELSE 10 * menu.price END) AS points
FROM dannys_diner.sales
INNER JOIN dates_cte AS dates
  ON sales.customer_id = dates.customer_id
  AND dates.join_date <= sales.order_date
  AND sales.order_date <= last_date
INNER JOIN dannys_diner.menu
  ON sales.product_id = menu.product_id
GROUP BY sales.customer_id;











