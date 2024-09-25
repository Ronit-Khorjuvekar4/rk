/* How many pizzas were ordered?*/
select count(*) as pizza_ordered from customer_orders;

/* How many unique customer orders were made? */
select count(distinct order_id) unique_customer from customer_orders;

/* How many successful orders were delivered by each runner? */
select runner_id,count(order_id) succes_order from runner_orders
WHERE distance != 0
group by runner_id;

/* How many of each type of pizza was delivered? */
select c.pizza_id,pn.pizza_name,count(c.order_id) from customer_orders c
join runner_orders r on c.order_id = r.order_id
join pizza_names pn on c.pizza_id = pn.pizza_id
where r.distance != 0
group by pizza_id;


/* How many Vegetarian and Meatlovers were ordered by each customer? */
select c.customer_id, pn.pizza_name, count(c.order_id) from customer_orders c
join pizza_names pn on c.pizza_id = pn.pizza_id
group by c.customer_id,pn.pizza_id
order by c.customer_id;

/* What was the maximum number of pizzas delivered in a single order? */

with ok AS(
	select c.order_id,
    count(c.pizza_id) as pizza_per_order from customer_orders c
    join runner_orders r on c.order_id = r.order_id
	where r.distance != 0
    group by order_id
)select max(pizza_per_order) as pizza_count from ok;


/* For each customer, how many delivered pizzas had at least 1 change and how many had no changes? */

SELECT 
  c.customer_id,
  SUM(
    CASE WHEN c.exclusions <> ' ' OR c.extras <> ' ' THEN 1
    ELSE 0
    END) AS at_least_1_change,
  SUM(
    CASE WHEN c.exclusions = ' ' AND c.extras = ' ' THEN 1 
    ELSE 0
    END) AS no_change
FROM customer_orders AS c
JOIN runner_orders AS r
  ON c.order_id = r.order_id
WHERE r.distance != 0
GROUP BY c.customer_id
ORDER BY c.customer_id;


/* How many pizzas were delivered that had both exclusions and extras? */

SELECT  
  SUM(
    CASE WHEN exclusions IS NOT NULL AND extras IS NOT NULL THEN 1
    ELSE 0
    END) AS pizza_count_w_exclusions_extras
FROM customer_orders AS c
JOIN runner_orders AS r
  ON c.order_id = r.order_id
WHERE r.distance >= 1 
  AND exclusions <> ' ' 
  AND extras <> ' ';

/* What was the total volume of pizzas ordered for each hour of the day? */

select extract(HOUR from order_time) as hourr, count(order_id) as pizza_count from customer_orders
group by hourr
order by pizza_count;

/*What was the volume of orders for each day of the week? */

select dayname(order_time) as days, count(order_id) from customer_orders
group by days
order by days;













