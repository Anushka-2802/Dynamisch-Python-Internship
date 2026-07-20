/*The JOIN clause is used to combine rows from two or more tables, 
based on a related column between them */

create database student_management;
use student_management;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    age INT,
    gender VARCHAR(10),
    city VARCHAR(50),
    email VARCHAR(100)
);
INSERT INTO students VALUES
(101, 'Anushka Gujar', 21, 'Female', 'Pune', 'anushka@gmail.com'),
(102, 'Prachi Patil', 22, 'Female', 'Mumbai', 'prachi@gmail.com'),
(103, 'Esha Khan', 20, 'Female', 'Nagpur', 'esha@gmail.com'),
(104, 'Arfa Shaikh', 23, 'Female', 'Hyderabad', 'arfa@gmail.com'),
(105, 'Rahul Sharma', 22, 'Male', 'Delhi', 'rahul@gmail.com'),
(106, 'Amit Verma', 21, 'Male', 'Pune', 'amit@gmail.com'),
(107, 'Sneha Joshi', 20, 'Female', 'Nashik', 'sneha@gmail.com'),
(108, 'Rohan Patil', 24, 'Male', 'Kolhapur', 'rohan@gmail.com'),
(109, 'Divya Nair', 22, 'Female', 'Kochi', 'divya@gmail.com'),
(110, 'Akash Singh', 23, 'Male', 'Jaipur', 'akash@gmail.com'),
(111, 'Neha Gupta', 21, 'Female', 'Lucknow', 'neha@gmail.com'),
(112, 'Karan Mehta', 24, 'Male', 'Ahmedabad', 'karan@gmail.com'),
(113, 'Sanchi More', 22, 'Female', 'Satara', 'sanchi@gmail.com'),
(114, 'Pooja Kulkarni', 23, 'Female', 'Solapur', 'pooja@gmail.com'),
(115, 'Vikas Yadav', 25, 'Male', 'Indore', 'vikas@gmail.com');

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    department VARCHAR(50),
    duration VARCHAR(30),
    fee DECIMAL(10,2)
);

INSERT INTO courses VALUES
(201, 'Python Programming', 'Computer Science', '3 Months', 15000.00),
(202, 'Java Programming', 'Computer Science', '4 Months', 18000.00),
(203, 'Web Development', 'IT', '3 Months', 20000.00),
(204, 'Data Science', 'AI & ML', '6 Months', 35000.00),
(205, 'Machine Learning', 'AI & ML', '5 Months', 30000.00),
(206, 'Cyber Security', 'IT', '4 Months', 25000.00),
(207, 'Cloud Computing', 'Computer Science', '3 Months', 22000.00),
(208, 'SQL Database', 'Database', '2 Months', 12000.00),
(209, 'DevOps', 'IT', '4 Months', 28000.00),
(210, 'Artificial Intelligence', 'AI & ML', '6 Months', 40000.00),
(211, 'C Programming', 'Computer Science', '2 Months', 10000.00),
(212, 'C++ Programming', 'Computer Science', '3 Months', 14000.00),
(213, 'Operating Systems', 'Computer Science', '4 Months', 16000.00),
(214, 'Computer Networks', 'IT', '3 Months', 17000.00),
(215, 'Software Testing', 'IT', '2 Months', 13000.00);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    semester VARCHAR(20),
    grade CHAR(2),

    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
INSERT INTO enrollments VALUES
(1, 101, 201, '2026-01-10', 'Semester 1', 'A'),
(2, 102, 202, '2026-01-12', 'Semester 1', 'B'),
(3, 103, 204, '2026-01-15', 'Semester 1', 'A'),
(4, 104, 205, '2026-01-16', 'Semester 2', 'A'),
(5, 105, 203, '2026-01-18', 'Semester 2', 'B'),
(6, 106, 206, '2026-01-20', 'Semester 2', 'A'),
(7, 107, 208, '2026-01-22', 'Semester 1', 'C'),
(8, 108, 210, '2026-01-24', 'Semester 3', 'A'),
(9, 109, 209, '2026-01-26', 'Semester 2', 'B'),
(10, 110, 207, '2026-01-28', 'Semester 1', 'A'),
(11, 111, 214, '2026-02-01', 'Semester 3', 'B'),
(12, 112, 215, '2026-02-03', 'Semester 2', 'A'),
(13, 113, 212, '2026-02-05', 'Semester 1', 'A');
select * from students;
select * from courses;
select * from enrollments;

-- INNER JOIN
select student_name,age,enrollment_date 
from students 
inner join enrollments on students.student_id=enrollments.student_id;

select * from students 
inner join enrollments on students.student_id=enrollments.student_id
inner join courses on enrollments.course_id=courses.course_id;

-- LEFT JOIN
select student_name,age,course_name,enrollment_date
from students 
left join enrollments on students.student_id=enrollments.student_id
left join courses on enrollments.course_id=courses.course_id;

-- RIGHT JOIN
select student_name, course_name, fee 
from students
right join enrollments on students.student_id = enrollments.student_id
right join courses on enrollments.course_id = courses.course_id;

-- Self join 
CREATE TABLE student_mentor (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    city VARCHAR(50),
    mentor_id INT
);
INSERT INTO student_mentor VALUES
(101,'Anushka','Pune',NULL),
(102,'Prachi','Mumbai',101),
(103,'Esha','Nagpur',101),
(104,'Arfa','Hyderabad',102),
(105,'Rahul','Delhi',102),
(106,'Amit','Pune',103),
(107,'Sneha','Nashik',103),
(108,'Rohan','Kolhapur',104);

select T1.student_name as student, T2.student_name as mentor
from student_mentor as T1
join student_mentor as T2 
on T2.student_id=T1.mentor_id



