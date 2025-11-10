-- Create Departments table
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL UNIQUE,
    location VARCHAR(50)
);

-- Create Employees table with constraints
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    salary DECIMAL(10,2) CHECK (salary > 0),
    dept_id INT,
    hire_date DATE DEFAULT SYSDATE,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- Alter table to add constraint
ALTER TABLE employees ADD CONSTRAINT chk_salary_range CHECK (salary BETWEEN 30000 AND 200000);

-- Create a view
CREATE VIEW emp_dept_view AS
SELECT e.name, e.salary, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id;

-- Create index
CREATE INDEX idx_emp_salary ON employees(salary);

-- Insert sample data
INSERT INTO departments VALUES (1, 'IT', 'Pune');
INSERT INTO departments VALUES (2, 'HR', 'Mumbai');

INSERT INTO employees VALUES (101, 'Alice', 50000.00, 1, '2023-01-15');
INSERT INTO employees VALUES (102, 'Bob', 60000.00, 2, '2023-02-20');

-- Query view
SELECT * FROM emp_dept_view;

-- Drop table (if needed)
-- DROP TABLE employees;