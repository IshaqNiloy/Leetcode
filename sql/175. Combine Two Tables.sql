-- Write your PostgreSQL query statement below
select  Person.firstName as firstName, Person.lastName as lastName, Address.city, Address.state
from Person
left join Address on Person.personId = Address.personId