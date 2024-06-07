-- Write your PostgreSQL query statement below
select A.name as Customers
from Customers A
left join Orders B on A.id = B.customerId
where B.customerId is NULL;