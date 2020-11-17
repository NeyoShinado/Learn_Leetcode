#Create table If Not Exists Customers (Id int, Name varchar(255))
#Create table If Not Exists Orders (Id int, CustomerId int)
#Truncate table Customers
#insert into Customers (Id, Name) values ('1', 'Joe')
#insert into Customers (Id, Name) values ('2', 'Henry')
#insert into Customers (Id, Name) values ('3', 'Sam')
#insert into Customers (Id, Name) values ('4', 'Max')
#Truncate table Orders
#insert into Orders (Id, CustomerId) values ('1', '3')
#insert into Orders (Id, CustomerId) values ('2', '1')


# Version 0
# 左连接 + 值为null筛选
SELECT Customers.Name as Customers
FROM (
	Customers LEFT JOIN Orders
	ON Customers.Id = Orders.CustomerId
)
WHERE Orders.Id is null


# Version 1
# IN 子句
# IN 子句效率较慢，且NOT IN 不走索引，慎用
SELECT customers.name as 'Customers'
FROM customers
WHERE customers.id not in
(
	SELECT customerid from orders
);


# Version 2
# Exists 子句
SELECT name Customers
FROM customers c
WHERE NOT EXISTS
(
	SELECT 1
	FROM orders o
	WHERE O.customerid = c.id
);