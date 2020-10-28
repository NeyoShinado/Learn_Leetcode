# Create table If Not Exists Scores (Id int, Score DECIMAL(3,2))
# Truncate table Scores
# insert into Scores (Id, Score) values ('1', '3.5')
# insert into Scores (Id, Score) values ('2', '3.65')
# insert into Scores (Id, Score) values ('3', '4.0')
# insert into Scores (Id, Score) values ('4', '3.85')
# insert into Scores (Id, Score) values ('5', '4.0')
# insert into Scores (Id, Score) values ('6', '3.65')


# Version 0
# 左连接 + 单表查询
SELECT Score, 'Rank'
FROM 
	(Scores e
	LEFT JOIN 
		(
		SELECT DISTINCT
			Score, @r:=@r+1 AS 'Rank' 
		FROM 
			Scores, (SELECT @r:=0) init
		ORDER BY Score DESC
		) AS rt 
	ON e.Score=rt.Score
	)


# Version 1
# 自连接
SELECT a.Score as Score,
	(
	SELECT COUNT(DISTINCT b.Score) 
	from Scores b 
	where b.Score >= a.Score
	) as 'Rank'
FROM Scores a
ORDER BY a.Score DESC


# Version 2
# 思路同Version 0
select rt.score Score, rt.rank 'Rank'
from scores join
	(
    SELECT ind_Scores.score score , @rank:=@rank+1 'rank' FROM 
        (SELECT distinct(score) score FROM Scores ORDER BY score DESC) ind_Scores , (SELECT @rank:=0 ) q
	) rt
on scores.score = rt.score
order by score desc