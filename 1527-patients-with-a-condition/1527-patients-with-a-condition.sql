# Write your MySQL query statement below
select *
from patients
where conditions like 'DIAB1%' OR conditions LIKE '% DIAB1%';