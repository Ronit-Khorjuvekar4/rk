-- SET FOREIGN_KEY_CHECKS=1;

/* If a Meat Lovers pizza costs $12 and Vegetarian costs $10 and there were no charges for changes - 
how much money has Pizza Runner made so far if there are no delivery fees? */

select * from pizza_names;

select c.pizza_id,rn.runner_id, pn.pizza_name, count(c.order_id) as pizza_delivered,
case
	when pn.pizza_name = 'Meatlovers' then count(c.order_id ) * 12
	when pn.pizza_name = 'Vegetarian' then count(c.order_id ) * 10
end  as runner_money_earned
from customer_orders c
join pizza_names pn on c.pizza_id = pn.pizza_id
join runner_orders rn on c.order_id = rn.order_id
group by pn.pizza_name, rn.runner_id
order by rn.runner_id,pn.pizza_name;


/*  If a Meat Lovers pizza was $12 and Vegetarian $10 fixed prices with no cost for extras 
and each runner is paid $0.30 per kilometre traveled - 
how much money does Pizza Runner have left over after these deliveries? */

select ro.runner_id,ro.order_id,pn.pizza_name,
case
	when pn.pizza_name = 'Meatlovers' then round(12 - (ro.distance * 0.30),2)
    when pn.pizza_name = 'Vegetarian' then round(10 - (ro.distance * 0.30),2)
end as runners_eranings
from runner_orders ro
join customer_orders c on ro.order_id = c.order_id
join pizza_names pn on c.pizza_id = pn.pizza_id
where ro.distance != 0
group by ro.runner_id,ro.order_id
order by ro.runner_id;

/* The Pizza Runner team now wants to add an additional ratings system that allows customers to rate their runner, 
how would you design an additional table for this new dataset - generate a schema for this new table and insert your 
own data for ratings for each successful customer order between 1 to 5. */

select * from runners;
select * from runner_orders order by order_id,runner_id;
select * from customer_orders order by order_id;
select * from ratings;

/* Using your newly generated table - can you join all of the information together to form a table which has the following information for successful deliveries?
customer_id
order_id
runner_id
rating
order_time
pickup_time
Time between order and pickup
Delivery duration
Average speed
Total number of pizzas */

select c.customer_id,
	   c.order_id,
       ro.runner_id,
	   ra.rating,
       c.order_time,
       ro.pickup_time,
       timestampdiff(minute,c.order_time,ro.pickup_time) time_between_order_pickup,
       ro.duration,
       ro.distance,
       count(c.pizza_id) as total_no_pizzas,
       round((ro.distance/ro.duration * 60),2) as avg_speed
from customer_orders c
join runner_orders ro on c.order_id = ro.order_id
join ratings ra on ra.order_id =  c.order_id
where ro.cancellation IS NULL OR ro.cancellation = ''
group by c.customer_id, c.order_id, ro.runner_id, ra.rating, c.order_time, ro.pickup_time, ro.duration;











