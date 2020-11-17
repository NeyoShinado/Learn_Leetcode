#Create table If Not Exists Person (Id int, Email varchar(255))
#Truncate table Person
#insert into Person (Id, Email) values ('1', 'a@b.com')
#insert into Person (Id, Email) values ('2', 'c@d.com')
#insert into Person (Id, Email) values ('3', 'a@b.com')

# Version 0
# not pass
SELECT Email 
FROM (
	SELECT Email, COUNT(Email) Cnt
	FROM Person
	GROUP BY Person.Email
) Tmp
WHERE Tmp.Cnt > 1


# Version 1
# 临时表 + Group By
SELECT Email
FROM(
	SELECT Email, COUNT(Email) as Cnt
	FROM Person
	GROUP BY Email
) AS Tmp
WHERE Cnt > 1;


# Version 2
# Group By + Having
# 优先顺序where>group by>having>order by
SELECT Email
FROM Person
GROUP BY Email
HAVING
	COUNT(Email) > 1;