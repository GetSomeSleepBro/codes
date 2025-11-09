-- PL/SQL Anonymous Block: Borrower fine calculation with control structures and exception handling
-- Problem tables (assumed existing):
--   Borrower (Roll_no VARCHAR2(20), Name VARCHAR2(100), Date_of_Issue DATE, Name_of_Book VARCHAR2(200), Status CHAR(1))
--   Fine     (Roll_no VARCHAR2(20), Fine_Date DATE, Amt NUMBER(10,2))
--
-- Notes:
-- - Status: 'I' = Issued, 'R' = Returned
-- - Fine rules assumed:
--     <= 14 days: no fine
--     15..30 days: Rs 5 per day
--     > 30 days:  Rs 50 per day
-- - Provide values via substitution variables when running in SQL*Plus/SQLcl:
--     DEFINE p_roll_no = 'R001'
--     DEFINE p_book    = 'Harry Potter and the Philosopher''s Stone'

SET SERVEROUTPUT ON;
DECLARE
  v_roll_no      Borrower.Roll_no%TYPE := '&p_roll_no';
  v_book_name    Borrower.Name_of_Book%TYPE := '&p_book';
  v_issue_date   Borrower.Date_of_Issue%TYPE;
  v_name         Borrower.Name%TYPE;
  v_days         PLS_INTEGER;
  v_fine         NUMBER(10,2) := 0;

  e_not_issued EXCEPTION;
  PRAGMA EXCEPTION_INIT(e_not_issued, -20001);
BEGIN
  -- Fetch the borrow record
  SELECT Name, Date_of_Issue
    INTO v_name, v_issue_date
    FROM Borrower
   WHERE Roll_no = v_roll_no
     AND Name_of_Book = v_book_name
     AND Status = 'I';

  v_days := TRUNC(SYSDATE) - TRUNC(v_issue_date);

  -- Compute fine based on rules
  IF v_days <= 14 THEN
    v_fine := 0;
  ELSIF v_days BETWEEN 15 AND 30 THEN
    v_fine := v_days * 5;
  ELSE
    v_fine := v_days * 50;
  END IF;

  -- Update status to Returned
  UPDATE Borrower
     SET Status = 'R'
   WHERE Roll_no = v_roll_no
     AND Name_of_Book = v_book_name
     AND Status = 'I';

  IF SQL%ROWCOUNT = 0 THEN
    RAISE_APPLICATION_ERROR(-20001, 'No active issued record found to return.');
  END IF;

  -- Insert fine if applicable
  IF v_fine > 0 THEN
    INSERT INTO Fine (Roll_no, Fine_Date, Amt)
    VALUES (v_roll_no, TRUNC(SYSDATE), v_fine);
    DBMS_OUTPUT.PUT_LINE('Fine levied: Rs ' || v_fine);
  ELSE
    DBMS_OUTPUT.PUT_LINE('No fine. Days kept: ' || v_days);
  END IF;

  COMMIT;
  DBMS_OUTPUT.PUT_LINE('Returned book: ' || v_book_name || ' by ' || v_name);

EXCEPTION
  WHEN NO_DATA_FOUND THEN
    DBMS_OUTPUT.PUT_LINE('Error: Borrower/book not found or not currently issued.');
  WHEN TOO_MANY_ROWS THEN
    DBMS_OUTPUT.PUT_LINE('Error: Multiple borrow records found. Please resolve duplicates.');
  WHEN e_not_issued THEN
    DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
  WHEN OTHERS THEN
    DBMS_OUTPUT.PUT_LINE('Unexpected error: ' || SQLCODE || ' - ' || SQLERRM);
    ROLLBACK;
END;
/

