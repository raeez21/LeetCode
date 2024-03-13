# Write your MySQL query statement below
select M.name
from Employee E
inner join Employee M
on E.managerId = M.id
group by M.id
having count(E.id) >=5

-- SELECT *
-- FROM Employee AS e 
-- INNER JOIN Employee AS m ON e.id=m.managerId 
-- GROUP BY m.managerId 
-- HAVING COUNT(m.managerId) >= 5