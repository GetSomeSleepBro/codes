-- Create log table for trigger
CREATE TABLE salary_log (
    emp_id INT,
    old_salary DECIMAL(10,2),
    new_salary DECIMAL(10,2),
    change_date DATE
);

-- Trigger 1: BEFORE INSERT - Validate salary > 30000
CREATE OR REPLACE TRIGGER trg_before_insert_emp
BEFORE INSERT ON employees
FOR EACH ROW
BEGIN
    IF :NEW.salary < 30000 THEN
        RAISE_APPLICATION_ERROR(-20001, 'Salary must be at least 30000');
    END IF;
END;
/

-- Trigger 2: AFTER UPDATE - Log salary changes
CREATE OR REPLACE TRIGGER trg_after_update_salary
AFTER UPDATE OF salary ON employees
FOR EACH ROW
BEGIN
    INSERT INTO salary_log (emp_id, old_salary, new_salary, change_date)
    VALUES (:OLD.emp_id, :OLD.salary, :NEW.salary, SYSDATE);
END;
/

-- Test triggers
INSERT INTO employees VALUES (103, 'Charlie', 25000.00, 1, '2023-03-10');  -- Should raise error
INSERT INTO employees VALUES (103, 'Charlie', 35000.00, 1, '2023-03-10');  -- Success
UPDATE employees SET salary = 40000.00 WHERE emp_id = 103;  -- Logs change

-- View log
SELECT * FROM salary_log;
