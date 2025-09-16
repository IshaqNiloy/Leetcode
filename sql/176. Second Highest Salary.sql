select MAX(salary) as secondHighestSalary
from Employee
where salary < (select MAX(salary) from Employee)
