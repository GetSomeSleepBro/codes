-- Stored Procedure and Function for grading
-- Short guide:
-- - fn_grade: returns class label from total_marks
-- - proc_grade: reads from stud_marks and upserts into result

-- Tables
CREATE TABLE stud_marks (
  roll        NUMBER       PRIMARY KEY,
  name        VARCHAR2(100) NOT NULL,
  total_marks NUMBER(4)    NOT NULL
);

CREATE TABLE result (
  roll  NUMBER        PRIMARY KEY,
  name  VARCHAR2(100) NOT NULL,
  class VARCHAR2(40)  NOT NULL
);

-- Function to compute class label
-- Function: input total marks => output class
CREATE OR REPLACE FUNCTION fn_grade(p_marks NUMBER)
RETURN VARCHAR2
IS
BEGIN
  IF p_marks BETWEEN 990 AND 1500 THEN
    RETURN 'Distinction';
  ELSIF p_marks BETWEEN 900 AND 989 THEN
    RETURN 'First Class';
  ELSIF p_marks BETWEEN 825 AND 899 THEN
    RETURN 'Higher Second Class';
  ELSE
    RETURN 'Second Class';
  END IF;
END;
/

-- Procedure to insert into result for a given roll
-- Procedure: compute class for a roll and store to RESULT
CREATE OR REPLACE PROCEDURE proc_grade(p_roll NUMBER)
IS
  v_name  stud_marks.name%TYPE;
  v_marks stud_marks.total_marks%TYPE;
  v_class VARCHAR2(40);
BEGIN
  SELECT name, total_marks INTO v_name, v_marks FROM stud_marks WHERE roll = p_roll;
  v_class := fn_grade(v_marks);

  MERGE INTO result r
  USING (SELECT p_roll AS roll, v_name AS name, v_class AS class FROM dual) x
  ON (r.roll = x.roll)
  WHEN MATCHED THEN UPDATE SET r.name = x.name, r.class = x.class -- update existing
  WHEN NOT MATCHED THEN INSERT (roll, name, class) VALUES (x.roll, x.name, x.class);
END;
/

-- Example usage block
-- Demo usage
BEGIN
  INSERT INTO stud_marks(roll, name, total_marks) VALUES (1, 'Riya', 1200);
  INSERT INTO stud_marks(roll, name, total_marks) VALUES (2, 'Dev',   940);
  INSERT INTO stud_marks(roll, name, total_marks) VALUES (3, 'Neha',  860);
  COMMIT;

  proc_grade(1);
  proc_grade(2);
  proc_grade(3);
  COMMIT;
END;
/
