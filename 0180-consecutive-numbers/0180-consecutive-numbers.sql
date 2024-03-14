# Write your MySQL query statement below


select distinct(num) as ConsecutiveNums
from(
select num, lead(num) over(order by id) as leadA, lag(num) over(order by id) as lagA
from logs
) t
where leadA = num and lagA = num