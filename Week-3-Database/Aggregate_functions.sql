/*
Aggregate functions perform operations on multiple rows and return single result
*/
CREATE TABLE product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    quantity INT
);
INSERT INTO product (product_id, product_name, category, price, quantity)
VALUES
(101, 'Laptop', 'Electronics', 65000, 10),
(102, 'Mouse', 'Electronics', 800, 50),
(103, 'Keyboard', 'Electronics', 1500, 35),
(104, 'Monitor', 'Electronics', 12000, 15),
(105, 'Office Chair', 'Furniture', 7000, 20),
(106, 'Study Table', 'Furniture', 8500, 12),
(107, 'Notebook', 'Stationery', 100, 100),
(108, 'Pen', 'Stationery', 20, 500),
(109, 'Printer', 'Electronics', 15000, 8),
(110, 'Water Bottle', 'Accessories', 500, 60),
(111, 'Backpack', 'Accessories', 1800, 25),
(112, 'Desk Lamp', 'Furniture', 2500, 18),
(113, 'Calculator', 'Stationery', 900, 30),
(114, 'Headphones', 'Electronics', 2500, 22),
(115, 'USB Drive', 'Electronics', 700, 40);

show tables;

Select * from product;

-- count

select count(*) from product;
select count(*) from product where category="furniture";
select count(product_name) from product where price>1000; 

-- MIN
select min(price) As min_price from product where category="furniture"; 
select min(quantity) AS min_quantity from product group by category;

-- MAX
select max(price) As min_price,product_name from product group by product_name; 

-- SUM
select sum(price) as pricesum,category from product group by category;
select sum(price) as pricesum from product;
select sum(price) as pricesum,category from product where category="electronics" group by category;

-- AVG
select avg(price) as avgprice,category from product where category="furniture" group by category;
select avg(price) as Avrage from product;


-- Display categories where the total quantity is greater than 100
select category,sum(quantity) as quantity from product group by category HAVING (quantity)>100;

-- Show the category with the highest average price
select category,avg(price) as Average 
from product 
group by category 
order by Average desc
limit 1; 