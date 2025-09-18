select  Person.firstName as firstName, Person.lastName as lastName, Address.city, Address.state
from Person
left join Address on Person.personId = Address.personId

select max(salary_amount) from salaries where salary_amount < (select max(salary_amount) from salaries);