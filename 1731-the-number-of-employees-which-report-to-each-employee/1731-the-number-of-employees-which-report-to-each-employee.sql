# Write your MySQL query statement below
select M.employee_id, M.name, count(E.reports_to) as reports_count, round(avg(E.age)) as average_age from 
Employees M
join Employees E
on M.employee_id = E.reports_to
group by M.employee_id
order by M.employee_id