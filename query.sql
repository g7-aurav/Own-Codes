use sales;
select sum(updated_sales_amount) from transactions_duplicate;
with cte as (
select t.order_date,m.markets_name,m.zone,p.product_type,c.custmer_name,c.customer_type,sum(t.sales_qty) sales_qty,
sum(t.profit_margin) profit_margin ,sum(t.updated_sales_amount) revenue
	from transactions_duplicate t
    left join
    markets m on t.market_code = m.markets_code
    left join
    products p on t.product_code = p.product_code
    left join
    customers c on t.customer_code = c.customer_code
    group by 1,2,3,4,5,6 )
select markets_name,zone,custmer_name,sum(revenue) as revenue,
row_number() over(partition by markets_name order by sum(revenue) desc ) as RNK,
case when sum(revenue) > 31000000 then 'Very High'
	when sum(revenue) > 10000000 then 'Medium' 
    else 'Low'
end as
Category from cte where zone = 'North' group by 1,2,3 ; 
select * from transactions limit 5;