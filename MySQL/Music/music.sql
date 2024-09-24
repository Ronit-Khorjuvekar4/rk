select * from employee;

/*Q1: Who is the senior most employee based on job title? */
select * from employee order by levels desc limit 1;

/*Q2: Which countries have the most Invoices?*/
select billing_country as country, count(*) as no_of_invoices from invoice
group by country
order by no_of_invoices desc;

/*Q3: What are top 3 values of total invoice?*/
 select * from invoice;
 select round(total,3) from invoice 
 order by total desc
 limit 3;

/* Q4: Which city has the best customers? We would like to throw a promotional Music Festival in the city we made the most money.
Write a query that returns one city that has the highest sum of invoice totals. 
Return both the city name & sum of all invoice totals. */
select billing_city, round(sum(total),3) as total from invoice
group by billing_city
order by total desc
limit 1;



/*Q5: Who is the best customer? The customer who has spent the most money will be declared the best customer.
Write a query that returns the person who has spent the most money.*/
select * from customer;

select c.customer_id,first_name,round(sum(total),2) as money_spent from invoice as i
left join customer as c on i.customer_id = c.customer_id
group by first_name, c.customer_id
order by money_spent desc;


/*Q6:Write query to return the email, first name, last name, & Genre of all Rock Music listeners. 
Return your list ordered alphabetically by email starting with A..*/
select * from media_type;
select email,first_name,last_name,g.name from customer as c
join invoice as i on c.customer_id = i.customer_id
join invoice_line as il on i.invoice_id = il.invoice_id
join track as t on il.track_id = t.track_id
join genre as g on t.genre_id = g.genre_id
where g.name like "Rock"
order by email asc;

/*Q7: Let's invite the artists who have written the most rock music in our dataset.
Write a query that returns the Artist name and total track count of the top 10 rock bands*/
select ar.artist_id as id ,ar.name as Artist_name, count(t.track_id) as track_count from artist as ar
left join album2 as al on ar.artist_id = al.artist_id
left join track as t on al.album_id = t.album_id
left join genre as g on t.genre_id = g.genre_id where g.name like 'Rock'
group by ar.name, ar.artist_id 
order by track_count desc
limit 10; 

/*Q8: Return all the track names that have a song length longer than the average song length.
Return the Name and Milliseconds for each track. Order by the song length with the longest songs listed first.*/
select name, milliseconds as ms from track
where milliseconds > (select avg(milliseconds) from track)
order by milliseconds desc;

/*Q9: Find how much amount spent by each customer on artists? 
Write a query to return customer name, artist name and total spent*/
select c.first_name, art.name, round(sum(inc.total),2) from customer as c
left join invoice as inc on c.customer_id = inc.customer_id
left join invoice_line as incl on inc.invoice_id = incl.invoice_id
left join track as t on incl.track_id = t.track_id
left join album2 as al on t.album_id = al.album_id
left join artist as art on al.artist_id = art.artist_id
where art.name is not null
group by c.first_name, art.name
order by c.first_name;

WITH best_selling_artist AS (
	SELECT artist.artist_id, artist.name AS artist_name, 
    SUM(invoice_line.unit_price*invoice_line.quantity) AS Total_Sales
	FROM invoice_line
	JOIN track ON track.track_id = invoice_line.track_id
	JOIN album2 ON album2.album_id = track.album_id
	JOIN artist ON artist.artist_id = album2.artist_id
	GROUP BY 1,2
	ORDER BY 3 DESC
	LIMIT 1
)
SELECT c.customer_id, c.first_name, c.last_name, bsa.artist_name, 
ROUND(SUM(il.unit_price*il.quantity),2) AS Total_Spent
FROM invoice i
JOIN customer c ON c.customer_id = i.customer_id
JOIN invoice_line il ON il.invoice_id = i.invoice_id
JOIN track t ON t.track_id = il.track_id
JOIN album2 alb ON alb.album_id = t.album_id
JOIN best_selling_artist bsa ON bsa.artist_id = alb.artist_id
GROUP BY 1,2,3,4
ORDER BY 5 DESC;



select * from customer;
select * from invoice order by customer_id;
select * from invoice_line order by invoice_id;
select * from track order by album_id;
select * from album2 order by artist_id ;
select * from artist;

/*Q10: We want to find out the most popular music Genre for each country.

Q11: Write a query that determines the customer that has spent the most on music for each country. */