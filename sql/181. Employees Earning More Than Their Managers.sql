-- Write your PostgreSQL query statement below
select A.name as Employee
from Employee A
join Employee B on A.managerId = B.id
and A.salary > B.salary;
