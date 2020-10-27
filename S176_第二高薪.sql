#Create table If Not Exists Employee (Id int, Salary int)
#Truncate table Employee	# 删除表的所有记录，使用系统和事务日志资源更少，速度比DELETE快，且保持表的列、约束和索引结构
#insert into Employee (Id, Salary) values ('1', '100')
#insert into Employee (Id, Salary) values ('2', '200')
#insert into Employee (Id, Salary) values ('3', '300')

# Version 0
# 不会取第二项记录
SELECT Salary as SecondHighestSalary 
From(SELECT DISTINCT Salary as SecondHighestSalary 
	From Employee
order by Salary)


# Version 1
# 不能处理没有第二高薪水的情况
SELECT DISTINCT
	Salary as SecondHighestSalary
From
	Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1


#* Version 2
# 使用子查询 + LIMIT
# 使用临时表子查询
SELECT 
	(SELECT DISTINCT
		Salary
	FROM 
		Employee
	ORDER BY Salary DESC
	LIMIT 1 OFFSET 1) AS SecondHighestSalary


# Version 3
# 使用IFNULL判断句 + LIMIT
SELECT  IFNULL(
	(SELECT DISTINCT Salary
		FROM Employee
		ORDER BY Salary DESC
		LIMIT 1 OFFSET 1),
	NULL) AS SecondHighestSalary