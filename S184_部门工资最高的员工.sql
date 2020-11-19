#CREAT TABLE IF NOT EXISTS Employee (Id int, Name varchar(255), Salary int, DepartmentId int);
#CREAT TABLE IF NOT EXISTS Department (Id int, Name varchar(255));
#TRUNCATE TABLE Employee;
#INSERT INTO Employee (Id, Name, Salary, DepartmentId) VALUES ('1', 'Joe', '70000', '1');
#INSERT INTO Employee (Id, Name, Salary, DepartmentId) VALUES ('2', 'Jim', '90000', '1');
#INSERT INTO Employee (Id, Name, Salary, DepartmentId) VALUES ('3', 'Henry', '80000', '2');
#INSERT INTO Employee (Id, Name, Salary, DepartmentId) VALUES ('4', 'Sam', '60000', '2');
#INSERT INTO Employee (Id, Name, Salary, DepartmentId) VALUES ('5', 'Max', '90000', '1');
#TRUNCATE TABLE Department;
#INSERT INTO Department (Id, Name) VALUES ('1', 'IT');
#INSERT INTO Department (Id, Name) VALUES ('2', 'Sales');


# Version 0
# 分组排序 + 连接
# NOT PASS
# LIMIT 不会作用在分组上
SELECT D.Name Department, TopS.Name Employee, Salary
FROM 
	Department D LEFT JOIN
(
	SELECT DepartmentId, Name, Salary
	FROM Employee
	GROUP BY DepartmentId
	ORDER BY Salary DESC
	LIMIT 1 OFFSET 0
) AS TopS
	ON D.Id = TopS.DepartmentId


# Version 1
# Join + in
# 因为有重复工资，所以驱动子表元信息只选部门ID和最高薪
SELECT
	Department.name AS 'Department',
	Employee.name AS 'Employee',
	Salary
FROM
	Employee JOIN Department
	ON Employee.DepartmentId = Department.Id
WHERE
(
	(Employee.DepartmentId, Salary) IN
	(
		SELECT 
			DepartmentId, MAX(Salary)
		FROM
			Employee
		GROUP BY DepartmentId
	)
)


# Version 2
# WHERE, 多表内连接
SELECT
	b.Name Department,
	a.Name Employee,
	c.MaxSalary Salary
FROM
	Employee a,
	Department b,
	(
		SELECT DepartmentId, MAX(Salary) MaxSalary
		FROM Employee
		GROUP BY DepartmentId
	) c
WHERE
	a.DepartmentId = c.DepartmentId
	AND a.DepartmentId = b.Id
	AND a.Salary = c.MaxSalary