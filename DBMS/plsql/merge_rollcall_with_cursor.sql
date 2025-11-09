-- PL/SQL: Parameterized cursor to merge N_RollCall into O_RollCall
-- Tables:
--   O_RollCall (RollNo NUMBER PRIMARY KEY, Name VARCHAR2(100))
--   N_RollCall (RollNo NUMBER PRIMARY KEY, Name VARCHAR2(100))

-- Sample DDL (uncomment if creating fresh):
-- CREATE TABLE O_RollCall (RollNo NUMBER PRIMARY KEY, Name VARCHAR2(100));
-- CREATE TABLE N_RollCall (RollNo NUMBER PRIMARY KEY, Name VARCHAR2(100));
-- INSERT INTO N_RollCall VALUES (1, 'Alice');
-- INSERT INTO N_RollCall VALUES (2, 'Bob');
-- INSERT INTO O_RollCall VALUES (2, 'Bob');
-- COMMIT;

SET SERVEROUTPUT ON;
DECLARE
  -- Parameterized cursor: only process rows with RollNo >= p_min_roll
  CURSOR c_new(p_min_roll NUMBER) IS
    SELECT RollNo, Name FROM N_RollCall WHERE RollNo >= p_min_roll ORDER BY RollNo;

  v_inserted PLS_INTEGER := 0;
  v_skipped  PLS_INTEGER := 0;
BEGIN
  FOR rec IN c_new(1) LOOP -- example parameter value
    BEGIN
      -- Try to insert; if duplicate, skip
      INSERT INTO O_RollCall(RollNo, Name) VALUES (rec.RollNo, rec.Name);
      v_inserted := v_inserted + 1;
    EXCEPTION
      WHEN DUP_VAL_ON_INDEX THEN
        v_skipped := v_skipped + 1; -- already exists
    END;
  END LOOP;

  DBMS_OUTPUT.PUT_LINE('Inserted: ' || v_inserted);
  DBMS_OUTPUT.PUT_LINE('Skipped (already exists): ' || v_skipped);
  DBMS_OUTPUT.PUT_LINE('Total O_RollCall rows: ' || SQL%ROWCOUNT); -- implicit cursor info from last DML
  COMMIT;
END;
/

