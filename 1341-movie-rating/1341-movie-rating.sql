# Write your MySQL query statement below

# select max(count(*)) as cnt
# from MovieRating
# group by user_id
# order by cnt desc
# limit 1


# select U.user_id
# from MovieRating M
# join Users U
# on M.user_id = U.user_id
# group by U.user_id
# order by count(*) desc, name
# limit 1


(SELECT name AS results
FROM MovieRating JOIN Users USING(user_id)
GROUP BY name
ORDER BY COUNT(*) DESC, name
LIMIT 1)

UNION ALL

(SELECT title AS results
FROM MovieRating JOIN Movies USING(movie_id)
WHERE EXTRACT(YEAR_MONTH FROM created_at) = 202002
GROUP BY title
ORDER BY AVG(rating) DESC, title
LIMIT 1);