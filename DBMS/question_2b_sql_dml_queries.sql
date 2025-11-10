-- 1. Insert single record
INSERT INTO Emp VALUES (100, 'Amit Sharma', '2023-06-15', 75000, 10);

-- 2. Insert multiple rows
INSERT INTO Emp VALUES
(101, 'Priya Singh', '2023-07-20', 82000, 20),
(102, 'Rohan Patel', '2023-08-10', 65000, 10),
(103, 'Neha Gupta', '2023-09-05', 90000, 30),
(104, 'Vikram Rao', '2023-05-12', 78000, 20);

-- 3. Display all records
SELECT * FROM Emp;

-- 4. Display records where salary > 8000
SELECT * FROM Emp WHERE Salary > 8000;

-- 5. Display records in ascending order of joining date
SELECT * FROM Emp ORDER BY Joiningdate ASC;

-- 6. Update salary of employee id=100 to 50000
UPDATE Emp SET Salary = 50000 WHERE Id = 100;

-- 7. Remove record of employee id=106
DELETE FROM Emp WHERE Id = 106;

-- 8. Use DISTINCT to display unique salaries
SELECT DISTINCT Salary FROM Emp;

-- 9. Display minimum and maximum salary
SELECT MIN(Salary) AS Min_Salary, MAX(Salary) AS Max_Salary FROM Emp;

-- 10. Display total number of employees
SELECT COUNT(*) AS Total_Employees FROM Emp;

-- 11. Display sum of salaries of dept=10
SELECT SUM(Salary) AS Total_Salary_Dept10 FROM Emp WHERE Dept = 10;
