-- Anonymous PL/SQL block: fine calculation on return
-- Short guide:
-- - &roll_no and &book_name are input prompts
-- - Use IF/ELSIF for fine rules
-- - Handle missing rows with NO_DATA_FOUND
-- - COMMIT on success, ROLLBACK on error

-- Minimal tables for this problem statement
CREATE TABLE borrower (
  roll_no       NUMBER       NOT NULL,
  name          VARCHAR2(100) NOT NULL,
  date_of_issue DATE         NOT NULL,
  name_of_book  VARCHAR2(200) NOT NULL,
  status        CHAR(1)      DEFAULT 'I' NOT NULL,
  CONSTRAINT ck_borrower_status CHECK (status IN ('I','R'))
);

CREATE TABLE fine (
  roll_no   NUMBER       NOT NULL,
  fine_date DATE         DEFAULT SYSDATE NOT NULL,
  amt       NUMBER(10,2) NOT NULL
);

DECLARE
  p_roll     NUMBER      := &roll_no;
  p_book     VARCHAR2(200) := '&book_name';
  v_issue_dt DATE;
  v_days     NUMBER := 0;
  v_amt      NUMBER := 0;
BEGIN
  -- Get date_of_issue for this borrower and book
  SELECT date_of_issue
    INTO v_issue_dt
    FROM borrower
   WHERE roll_no = p_roll
     AND LOWER(name_of_book) = LOWER(p_book)
     AND status = 'I';

  v_days := TRUNC(SYSDATE) - TRUNC(v_issue_dt);

  -- Fine rules
  IF v_days BETWEEN 15 AND 30 THEN
    v_amt := v_days * 5;
  ELSIF v_days > 30 THEN
    v_amt := v_days * 50;
  ELSE
    v_amt := 0;
  END IF;

  -- Mark returned
  UPDATE borrower
     SET status = 'R'
   WHERE roll_no = p_roll
     AND LOWER(name_of_book) = LOWER(p_book)
     AND status = 'I';

  -- Record fine when applicable
  IF v_amt > 0 THEN
    INSERT INTO fine(roll_no, fine_date, amt)
    VALUES (p_roll, TRUNC(SYSDATE), v_amt);
  END IF;

  COMMIT;
EXCEPTION
  WHEN NO_DATA_FOUND THEN
    ROLLBACK;
    RAISE_APPLICATION_ERROR(-20001, 'No matching issued record found.');
  WHEN OTHERS THEN
    ROLLBACK;
    RAISE;
END;
/
