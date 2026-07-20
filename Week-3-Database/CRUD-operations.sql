/*
CRUD operations: 
Create: (INSERT) Add new records.
Read:   (SELECT) Retrieve records.
Update: (UPDATE) Modify existing records.
Delete: (DELETE) Remove records.
*/
-- display existing databases
show databases;

-- create database 
create database employee;
use employee;

-- create table
create table Emp_details(
id int primary key,
name varchar(100),
department varchar(100),
salary decimal(10,2),
age int
);

-- Display tables
show tables;

select database();
show tables;

DESC emp_details;

-- Create operation: Add new record
-- Add employee details
insert into emp_details values 
(1,"Anushka","IT",20000,21),
(2,"Prachi","AI",30000,22),
(3,"Esha","Sales",22000,20),
(4,"Arfa","AI",30000,23),
(5,"Abhilasha","ML",20000,22),
(6,"Divya","ML",23000,23),
(7,"Sanchi","ML",10000,24);
insert into Emp_details values
(8, 'Rahul', 'IT', 35000, 25),
(9, 'Amit', 'HR', 28000, 26),
(10, 'Priya', 'Finance', 45000, 29),
(11, 'Neha', 'Sales', 27000, 24),
(12, 'Rohan', 'IT', 50000, 30),
(13, 'Karan', 'HR', 26000, 27),
(14, 'Sneha', 'Finance', 55000, 31),
(15, 'Pooja', 'AI', 42000, 26),
(16, 'Vikas', 'Marketing', 32000, 28),
(17, 'Nisha', 'Marketing', 31000, 25),
(18, 'Akash', 'IT', 48000, 29),
(19, 'Meera', 'ML', 38000, 27),
(20, 'Sagar', 'Sales', 29000, 26);

-- Read operations: Retrieve Data
-- Display all employee details 
select * from Emp_details

-- Update operation: modify data
update Emp_details set salary=25000 where id=1;
select * from Emp_details where id=1;
update Emp_details set department="ML", age=20 where id=2

-- view result
select * from Emp_details;

-- Delete operation 
/*
DELETE: Delete removes rows using where 
TRUNCATE: Delete all rows 
DROP: Delete entire table
*/
delete from Emp_details where id = 7;

-- truncate 
create table emp(
id int,
name varchar(100),
age int
);

insert into emp values (1,"Anu",21);
insert into emp values (2,"Sanu",19);
insert into emp values (1,"Abhi",22);

truncate table emp;
-- display empty table 
select *  from emp;

-- Delete entire table
drop table emp;

-- Display existing tables
show tables;

-- count and display distinct values
select distinct age from Emp_details;
select count(distinct(age)) from Emp_details;

