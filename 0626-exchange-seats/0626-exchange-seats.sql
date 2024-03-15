# Write your MySQL query statement below

select case
            when id = (select max(id) from seat) and id%2=1
                THEN id
            when id % 2 = 1
                THEN id+1
            ELSE id-1
        END as id,
        student
from seat
order by id 