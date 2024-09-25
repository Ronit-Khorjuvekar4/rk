/*B. Runner and Customer Experience*/
/*How many runners signed up for each 1 week period? (i.e. week starts 2021-01-01)*/
select week(registration_date,0) as week_joined, count(runner_id) from runners
group by week_joined;

/* What was the average time in minutes it took for each runner to arrive at the Pizza Runner HQ to pickup the order? */

select ro.runner_id, avg(timestampdiff(minute,c.order_time,ro.pickup_time)) avg_pickup_minutes from runner_orders ro
join customer_orders c on ro.order_id = c.order_id
where  ro.pickup_time IS NOT NULL 
    AND ro.cancellation IS NULL
group by ro.runner_id
order by ro.runner_id;

/* Is there any relationship between the number of pizzas and how long the order takes to prepare?  */

with preptime AS (
select c.order_id,
	count(c.pizza_id) total_pizzas,
	c.order_time, ro.pickup_time, 
    timestampdiff(minute,c.order_time,ro.pickup_time) time_to_prepare 
from customer_orders c
	join runner_orders ro on c.order_id = ro.order_id
		where ro.distance != 0
		group by c.order_id, c.order_time, ro.pickup_time
		order by c.order_id
)select total_pizzas,
	avg(time_to_prepare) 
	from preptime
	group by total_pizzas;


/* What was the average distance travelled for each customer? */

select * from runner_orders;
select * from customer_orders order by customer_id;

select c.customer_id, avg(ro.distance) from customer_orders c
join runner_orders ro on c.order_id = ro.order_id
where distance != 0
group by c.customer_id;

/* What was the difference between the longest and shortest delivery times for all orders? */

with timee AS(
	select c.order_id,c.order_time,
		ro.pickup_time,
        timestampdiff(minute,c.order_time, ro.pickup_time) max_delivery_time
	from customer_orders c
		join runner_orders ro on c.order_id = ro.order_id
		where ro.distance != 0
        group by c.order_id
)select (max(max_delivery_time) - min(max_delivery_time)) diff_delivery_time from timee;

/* What was the average speed for each runner for each delivery and do you notice any trend for these values? */

with avg_delivery_time AS(
	select c.order_id,ro.runner_id,COUNT(c.order_id) AS pizza_count,
    round((ro.distance/ro.duration * 60),2) as avg_delivery_time
    from customer_orders c
    join runner_orders ro on c.order_id = ro.order_id
    where distance != 0
    group by ro.runner_id,c.order_id
)select *
	from avg_delivery_time
    group by runner_id,order_id;
    

/*What is the successful delivery percentage for each runner?*/

SELECT 
  runner_id, 
  ROUND(100 * SUM(
    CASE WHEN distance = 0 THEN 0
    ELSE 1 END) / COUNT(*), 0) AS success_perc
FROM runner_orders
GROUP BY runner_id;
