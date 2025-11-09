-- PL/SQL Stored Procedure and Function for grading students
-- Requires tables from sql/students_schema.sql

-- Function: returns class based on total marks
CREATE OR REPLACE FUNCTION fn_grade (p_marks IN NUMBER)
  RETURN VARCHAR2
IS
  v_class VARCHAR2(30);
BEGIN
  IF p_marks BETWEEN 990 AND 1500 THEN
    v_class := 'Distinction';
  ELSIF p_marks BETWEEN 900 AND 989 THEN
    v_class := 'First Class';
  ELSIF p_marks BETWEEN 825 AND 899 THEN
    v_class := 'Higher Second Class';
  ELSE
    v_class := 'No Category';
  END IF;
  RETURN v_class;
END fn_grade;
/

-- Procedure: processes Stud_Marks and populates Result
CREATE OR REPLACE PROCEDURE proc_grade
IS
BEGIN
  FOR rec IN (SELECT name, total_marks FROM Stud_Marks) LOOP
    INSERT INTO Result(roll, name, class)
    VALUES (seq_roll.NEXTVAL, rec.name, fn_grade(rec.total_marks));
  END LOOP;
  COMMIT;
END proc_grade;
/

-- Demo block to use procedure
SET SERVEROUTPUT ON;
BEGIN
  proc_grade;
  DBMS_OUTPUT.PUT_LINE('Grading completed. Rows in Result:');
  FOR r IN (SELECT roll, name, class FROM Result ORDER BY roll) LOOP
    DBMS_OUTPUT.PUT_LINE(r.roll || ': ' || r.name || ' -> ' || r.class);
  END LOOP;
END;
/

