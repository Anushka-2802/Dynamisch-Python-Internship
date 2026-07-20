/*
filtering: Selecting only the rows that satisfy a condition.
sorting: ordering data 
*/
show tables;
-- filtering (where)
select * from Emp_details;

-- 1.Show all employees from the ML department
select * from Emp_details where department="ML";

-- 2.Show employees with a salary greater than 30,000
select * from Emp_details where salary > 30000;

-- 3.Show employees whose age is between 22 and 25
select * from Emp_details where age between 22 and 25;

-- Show employees from IT or AI departments
select * from Emp_details where department in ("AI","ML");

-- Show employees not in the Sales department
select * from Emp_details where not department="Sales";

-- Show employees whose names start with 'A'
select * from Emp_details where name like 'A%';


-- sorting(order by)

-- Show all employees ordered by salary (highest first)
select * from Emp_details order by salary desc; 

-- Show all employees ordered by department, then by salary (highest first).
select * from Emp_details order by department,salary desc; 

-- Show only IT employees ordered by age (youngest first)
select * from Emp_details where department="IT" order by age desc;

-- Show employees with salaries between 20,000 and 40,000, sorted by name.
select * from Emp_details where salary between 20000 and 40000 order by name;

-- how the top 3 highest-paid employees
select * from Emp_details order by salary desc limit 3;
