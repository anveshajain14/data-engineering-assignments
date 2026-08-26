create table if not exists cyntexa_dev.gold.customer_revenue as
select customer_id, sum(sale_amount) as total_revenue 
from cyntexa_dev.silver.sales_cleaned
group by customer_id
order by sum(sale_amount)