# CREATE TABLE IF NOT EXISTS Employee (Id int, Name varchar(255), Salary int, DepartmentId int);
# CREATE TABLE IF NOT EXISTS Department (Id int, Name varchar(255));
# TRUNCATE TABLE Employee;
# INSERT INTO Employee (Id, Name, Salary, DepartmentId) VALUES ('1', 'Joe', '85000', '1');
# INSERT INTO Employee (Id, Name, Salary, DepartmentId) VALUES ('2', 'Henry', '80000', '2');
# INSERT INTO Employee (Id, Name, Salary, DepartmentId) VALUES ('3', 'Sam', '60000', '2');
# INSERT INTO Employee (Id, Name, Salary, DepartmentId) VALUES ('4', 'Max', '90000', '1');
# INSERT INTO Employee (Id, Name, Salary, DepartmentId) VALUES ('5', 'Janet', '69000', '1');
# INSERT INTO Employee (Id, Name, Salary, DepartmentId) VALUES ('6', 'Randy', '85000', '1');
# INSERT INTO Employee (Id, Name, Salary, DepartmentId) VALUES ('7', 'Will', '70000', '1');
# TRUNCATE TABLE Department;
# INSERT INTO Department (Id, Name) VALUES ('1', 'IT');
# INSERT INTO Department (Id, Name) VALUES ('2', 'Sales');

# Version 1
# 通过自连接 + COUNT 实现TopN
SELECT
	d.Name 'Department', e1.Name 'Employee', e1.Salary
FROM
	Employee e1 JOIN Department d 
	ON
		E1.DepartmentId = d.Id
WHERE
	3 > (
	SELECT COUNT(DISTINCT e2.Salary)
	FROM Employee e2
	WHERE
		e2.Salary > e1.Salary
		AND
		# 条件连接实现分组
		e1.DepartmentId = e2.DepartmentId
	)


# Version 2
# 窗口函数
SELECT 
	Department, Employee, Salary
FROM
	(
	SELECT 
		d.Name 'Department', 
		e.Name 'Employee',
		e.Salary 'Salary',
		dense_rank() OVER (
			PARTITION BY d.Name
			ORDER BY Salary DESC
			) AS ranking
	FROM
		Employee e
		JOIN
		Department d
	ON e.DepartmentId = d.Id
	) AS a
WHERE
	ranking <= 3;


# Version 3
# 自变量 + 自连接
# 步骤：①按部门给员工工资排序；②取出排名不小于3的员工；③与部门名称表进行连接；
SELECT 
	dpTable.Name Department, Employee, Salary
FROM
	(
	SELECT
		Name AS Employee,
		Salary,
		DepartmentId,
		@rank := IF(@preDepartmentId=DepartmentId, 
					IF(@preSalary = Salary, @rank+0, @rank+1), 1) AS SalaryRank,
		@preDepartmentId := DepartmentId,
		@preSalary := Salary
	FROM
		Employee, (SELECT @preDepartmentId:=NULL, @preSalary:=NULL, @rank:=0) AS Init
	ORDER BY DepartmentId, Salary DESC
	) AS RankTable
	JOIN 
		Department
	AS dpTable
	ON
		RankTable.DepartmentId = dpTable.Id
WHERE
	SalaryRank <= 3;


