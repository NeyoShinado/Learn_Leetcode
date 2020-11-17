#Create table If Not Exists Logs (Id int, Num int)
#Truncate table Logs
#insert into Logs (Id, Num) values ('1', '1')
#insert into Logs (Id, Num) values ('2', '1')
#insert into Logs (Id, Num) values ('3', '1')
#insert into Logs (Id, Num) values ('4', '2')
#insert into Logs (Id, Num) values ('5', '1')
#insert into Logs (Id, Num) values ('6', '2')
#insert into Logs (Id, Num) values ('7', '2')

# Version 1
# 使用三表连接
# 有局限性，不能拓展为任意次情况，且复杂度过高
# TC: O(N^3), SC: O(N^3)
SELECT DISTINCT
	l1.Num AS ConsecutiveNums    # 多次至少连续出现三次的数需要去重
FROM
	Logs l1,
	Logs l2,
	Logs l3
WHERE
	l1.Id = l2.Id-1 AND l2.Id = l3.Id-1
	AND l1.Num = l2.Num AND l2.Num = l3.Num


# Version 2
#*自定义变量（循环更新变量值）
SELECT DISTINCT a.Num ConsecutiveNums FROM(
	SELECT t.Num,
			@cnt:=IF(@pre=t.Num, @cnt+1, 1) cnt,
			@pre:=t.Num pre 			# *变量pre在循环中记录上一个数字
	FROM Logs t, (SELECT @pre:=null, @cnt:=0) b) a
WHERE a.cnt >= 3


# Version 3
# *窗口函数
# 思路：复制列变量，并依次上移1,2,...,n-1行，值全等的就是连续出现n次的记录
SELECT DISTINCT
	num AS ConsecutiveNums
FROM
	(
	SELECT num, lead(num, 1) over() as num1, lead(num, 2) over() as num2
	FROM 
		Logs
	) AS C
WHERE c.num=c.num1 AND c.num1 = c.num2


# Version 4
# 正序编号与分组编号之差
# 最后进行分组统计，连续出现的值编号相同
SELECT DISTINCT 
	Num AS ConsecutiveNums
FROM(
	SELECT 
		num, count(*) num_count
	FROM(
		SELECT id, num,
			row_number() over(order by id) - row_number() over(partition by num order by id) AS order
		FROM
			logs
		) AS W
	group by num, order
) AS S
WHERE num_count >= 3

