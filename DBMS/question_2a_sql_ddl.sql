-- 1. TABLE with PRIMARY KEY, NOT NULL, DEFAULT, CHECK constraints
CREATE TABLE employee (
    emp_id      NUMBER(5)      PRIMARY KEY,
    emp_name    VARCHAR2(10)   NOT NULL,
    job_name    VARCHAR2(10)   NOT NULL,
    hire_date   DATE           DEFAULT SYSDATE,
    salary      DECIMAL(6,2)   CHECK (salary >= 0),
    commission  DECIMAL(6,2)   NULL,
    dept_id     NUMBER(4)      REFERENCES department(dept_id)  -- Foreign Key
);

-- 2. Supporting DEPARTMENT table for FOREIGN KEY
CREATE TABLE department (
    dept_id     NUMBER(4)      PRIMARY KEY,
    dept_name   VARCHAR2(20)   UNIQUE NOT NULL
);

-- 3. SEQUENCE for auto-generating emp_id
CREATE SEQUENCE emp_id_seq
    START WITH 1
    INCREMENT BY 1
    NOCACHE;

-- 4. VIEW - Shows employee details with department name
CREATE OR REPLACE VIEW v_emp_dept AS
SELECT e.emp_id, e.emp_name, e.job_name, e.salary, d.dept_name
FROM employee e
JOIN department d ON e.dept_id = d.dept_id;

-- 5. INDEX - For faster search on salary
CREATE INDEX idx_emp_salary ON employee(salary);

-- 6. COMPOSITE INDEX - On job_name and hire_date
CREATE INDEX idx_emp_job_hire ON employee(job_name, hire_date);

-- 7. SYNONYM - Simplified name for the view
CREATE SYNONYM empview FOR v_emp_dept;

-- 8. Insert using SEQUENCE and test constraints
INSERT INTO department VALUES (10, 'IT');
INSERT INTO department VALUES (20, 'HR');

INSERT INTO employee (emp_id, emp_name, job_name, dept_id, salary)
VALUES (emp_id_seq.NEXTVAL, 'Amit', 'Manager', 10, 50000.00);

-- This will fail: salary negative
-- INSERT INTO employee VALUES (emp_id_seq.NEXTVAL, 'Raj', 'Clerk', SYSDATE, -100, NULL, 20);

-- This will fail: dept_id not in department
-- INSERT INTO employee VALUES (emp_id_seq.NEXTVAL, 'Priya', 'Analyst', SYSDATE, 45000, NULL, 99);

-- 9. Query the view using synonym
SELECT * FROM empview;

-- 10. Drop objects (optional cleanup)
-- DROP SYNONYM empview;
-- DROP INDEX idx_emp_salary;
-- DROP VIEW v_emp_dept;
-- DROP SEQUENCE emp_id_seq;
-- DROP TABLE employee;
-- DROP TABLE department;
