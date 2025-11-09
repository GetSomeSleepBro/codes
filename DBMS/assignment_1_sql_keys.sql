CREATE TABLE students (student_id INT PRIMARY KEY, name       VARCHAR (100), email      VARCHAR 
(100));
CREATE TABLE users (user_id INT PRIMARY KEY, email   VARCHAR (100) UNIQUE, phone   VARCHAR 
(15) UNIQUE);
CREATE TABLE departments (    dept_id INT PRIMARY KEY,    dept_name VARCHAR(50));
CREATE TABLE employees (    emp_id    INT PRIMARY KEY,    name      VARCHAR(100), 
    dept_id   INT,    FOREIGN KEY (dept_id) REFERENCES departments(dept_id));
CREATE TABLE course_registration (    student_id INT,    course_id  INT,    registration_date DATE, 
     PRIMARY KEY (student_id, course_id));
CREATE TABLE students ( 
    student_id     INT PRIMARY KEY,    aadhar_number  CHAR(12) UNIQUE,    name           
VARCHAR(100));
CREATE TABLE Employees (EmployeeID INT PRIMARY KEY, Name VARCHAR(50), Email 
VARCHAR(100) UNIQUE, PhoneNumber VARCHAR(15) UNIQUE );
