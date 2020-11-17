#Create table If Not Exists Employee (Id int, Name varchar(255), Salary int, ManagerId int)
#Truncate table Employee
#insert into Employee (Id, Name, Salary, ManagerId) values ('1', 'Joe', '70000', '3')
#insert into Employee (Id, Name, Salary, ManagerId) values ('2', 'Henry', '80000', '4')
#insert into Employee (Id, Name, Salary, ManagerId) values ('3', 'Sam', '60000', 'None')
#insert into Employee (Id, Name, Salary, ManagerId) values ('4', 'Max', '90000', 'None')


# Version 1
# inner join
# 内连接会自动过滤NULL值
SELECT
	a.Name AS Employee
FROM
	Employee AS a,
	JOIN Employee AS b
ON
	a.ManagerId = b.Id
	AND a.Salary > b.Salary


# Version 2
# Cross join
# 连接有时会击中索引，不过不会自动过滤NULL
SELECT 
	a.Name as Employee
FROM
	Employee a, Employee b
WHERE
	a.ManagerId is not null
	AND a.ManagerId = b.Id
	And a.Salary > b.Salary


# Version 3
# 子查询
# 似乎比较慢
SELECT
	name AS Employee
FROM 
	Employee A
WHERE
	Salary > (
		SELECT 
			Salary
		FROM
			Employee
		WHERE
			A.ManagerId = Id
		)


# Version 4
# exist
SELECT 
	name as Employee
FROM
	Employee A
WHERE exists
	(SELECT
		Salary
	FROM
		Employee
	WHERE
		A.ManagerId = Id
		AND A.Salary > Salary
		)