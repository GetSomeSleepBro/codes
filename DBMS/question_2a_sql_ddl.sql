-- SQL DDL (Data Definition Language) Script
-- Demonstrates creating tables, constraints, sequences, views, indexes, and synonyms.

-- 1. Create DEPARTMENT table
-- This table stores department information and is referenced by the EMPLOYEE table.
CREATE TABLE department (
    dept_id     NUMBER(4)      PRIMARY KEY,
    dept_name   VARCHAR2(20)   UNIQUE NOT NULL
);

-- 2. Create EMPLOYEE table
-- This table stores employee details with several constraints.
CREATE TABLE employee (
    emp_id      NUMBER(5)      PRIMARY KEY,
    emp_name    VARCHAR2(10)   NOT NULL,
    job_name    VARCHAR2(10)   NOT NULL,
    hire_date   DATE           DEFAULT SYSDATE,
    salary      DECIMAL(6,2)   CHECK (salary >= 0),
    commission  DECIMAL(6,2)   NULL,
    dept_id     NUMBER(4)      REFERENCES department(dept_id)  -- Foreign Key
);

-- 3. Create a SEQUENCE for auto-generating employee IDs
CREATE SEQUENCE emp_id_seq
    START WITH 1
    INCREMENT BY 1
    NOCACHE;

-- 4. Create a VIEW to show employee details with department name
CREATE OR REPLACE VIEW v_emp_dept AS
SELECT e.emp_id, e.emp_name, e.job_name, e.salary, d.dept_name
FROM employee e
JOIN department d ON e.dept_id = d.dept_id;

-- 5. Create an INDEX for faster searches on the salary column
CREATE INDEX idx_emp_salary ON employee(salary);

-- 6. Create a COMPOSITE INDEX on job_name and hire_date
CREATE INDEX idx_emp_job_hire ON employee(job_name, hire_date);

-- 7. Create a SYNONYM for the view to provide a simpler name
CREATE SYNONYM empview FOR v_emp_dept;

-- 8. Insert sample data to test the schema and constraints
-- Insert departments first due to the foreign key constraint
INSERT INTO department VALUES (10, 'IT');
INSERT INTO department VALUES (20, 'HR');

-- Insert an employee using the sequence for the primary key
INSERT INTO employee (emp_id, emp_name, job_name, dept_id, salary)
VALUES (emp_id_seq.NEXTVAL, 'Amit', 'Manager', 10, 50000.00);

-- 9. Query the view using the synonym to see the results
SELECT * FROM empview;

-- 10. Optional cleanup: Drop all created objects
/*
DROP SYNONYM empview;
DROP INDEX idx_emp_job_hire;
DROP INDEX idx_emp_salary;
DROP VIEW v_emp_dept;
DROP SEQUENCE emp_id_seq;
DROP TABLE employee;
DROP TABLE department;
*/
