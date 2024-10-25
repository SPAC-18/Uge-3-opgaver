-- 2.
select * from products
order by UnitPrice;

-- 3.
select * from customers
where Country = "Spain" or Country = "UK"
;

-- 4.
select * from products
where UnitsInStock > 100 and UnitPrice >= 25
;

-- 5.
select distinct ShipCountry from orders;

-- 6.
select * from orders
where OrderDate LIKE '%1996-10-%'
;

-- 7.
select * from orders
where ShipRegion is NULL and ShipCountry = "Germany" and Freight >= 100 and EmployeeID = 1 and OrderDate LIKE '%1996%'
;

-- 8.
select * from orders
where ShippedDate > RequiredDate
;

-- 9.
select * from orders
where ShipCountry = "Canada" and (OrderDate LIKE '%1997-01%' or OrderDate LIKE '%1997-02%' or OrderDate LIKE '%1997-03%' or OrderDate LIKE '%1997-04%')
;

-- 10.
select * from orders
where (EmployeeID = 2 or EmployeeID = 5 or EmployeeID = 8) and ShipRegion != '' and (ShipVia = 1 or ShipVia = 3)
order by EmployeeID asc, ShipVia asc
;

-- 11.
select * from employees
where (Region is NULL) and BirthDate < '1960-01-01 00:00:00'
;