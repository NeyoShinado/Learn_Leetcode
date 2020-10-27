// Version 0
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
	RETURN(
		SELECT
		(SELECT DISTINCT 
			Salary 
		 FROM 
		 	Employee
		 order by Salary desc
		 LIMIT N-1, 1;
		 ) as getNthHighestSalary
	);
END


// Version 1
// LIMIT + GROUP/DISTINCT
// 不适用存在重复值跳级排名和连续排名的情况
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
	SET N := N-1;
	RETURN(
		SELECT
			Salary
		FROM
			Employee
		GROUP by
			Salary
		ORDER by
			Salary DESC
		LIMIT N, 1
	);
END


// Version 2
// 子查询查出去重后高于N-1个薪水值的目标值
// 返回的薪水也应该去重，因为可能有重复薪水
// 每个薪水值需要执行一遍统计，所以效率低下
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
	RETURN(
		SELECT
			DISTINCT e.Salary
		FROM
			Employee e
		WHERE(
			SELECT count(DISTINCT Salary) FROM Employee WHERE Salary > e.Salary) = N-1
		);
END


// Version 3
// 自连接
// 自连接辅助表e2的salary记录数相当于计数器
// 取<=以及计数为N项的目的是避免取<时N-1(N=1)无记录的情况，这时也可通过left join 实现
// 同样每个薪水值需要统计，速度也会比较慢
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT 
          e1.salary
      FROM 
          employee e1 JOIN employee e2 ON e1.salary <= e2.salary
      GROUP BY 
          e1.salary
      HAVING 
          count(DISTINCT e2.salary) = N
  );
END


// Version 4
// 笛卡尔积
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT 
          e1.salary
      FROM 
          employee e1, employee e2 
      WHERE 
          e1.salary <= e2.salary
      GROUP BY 
          e1.salary
      HAVING 
          count(DISTINCT e2.salary) = N
  );
END


// Version 5
// ▲自定义变量
// 建立两表关联的方法不适用于数据量大的情况，复杂度会达到O(N^2)级别
// 建立自定义变量能优化至O(2N)
// ①变量实现按薪水降序含重连续排名；②筛选出排名为N的薪水；③DISTINCT去重
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT 
          DISTINCT salary 
      FROM 
          (SELECT 
                salary, @r:=IF(@p=salary, @r, @r+1) AS rnk,  @p:= salary 
            FROM  
                employee, (SELECT @r:=0, @p:=NULL)init 
            ORDER BY 
                salary DESC) tmp
      WHERE rnk = N
  );
END


// Version 6
// 窗口函数▲
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
        SELECT 
            DISTINCT salary
        FROM 
            (SELECT 
                salary, dense_rank() over(ORDER BY salary DESC) AS rnk
             FROM 
                employee) tmp
        WHERE rnk = N
  );
END