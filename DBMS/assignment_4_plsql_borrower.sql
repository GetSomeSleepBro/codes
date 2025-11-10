DECLARE
    v_roll_no       VARCHAR2(20);
    v_book_name     VARCHAR2(100);
    v_date_issue    DATE;
    v_status        CHAR(1);
    v_days          NUMBER;
    v_fine_amt      NUMBER(10,2);
    e_no_borrower   EXCEPTION;
    PRAGMA EXCEPTION_INIT(e_no_borrower, -01403);
BEGIN
    v_roll_no := '&Roll_no';
    v_book_name := '&Name_of_Book';
    SELECT date_of_issue, status
    INTO v_date_issue, v_status
    FROM borrower
    WHERE roll_no = v_roll_no AND name_of_book = v_book_name;
    IF v_status != 'I' THEN
        RAISE e_no_borrower;
    END IF;
    v_days := TRUNC(SYSDATE - v_date_issue);
    IF v_days > 30 THEN
        v_fine_amt := v_days * 50;
    ELSIF v_days <= 30 AND v_days >= 15 THEN
        v_fine_amt := v_days * 5;
    ELSIF v_days < 15 THEN
        v_fine_amt := v_days * 5;
    ELSE
        v_fine_amt := 0;
    END IF;
    UPDATE borrower
    SET status = 'R'
    WHERE roll_no = v_roll_no AND name_of_book = v_book_name;
    IF v_fine_amt > 0 THEN
        INSERT INTO fine (roll_no, date, amt)
        VALUES (v_roll_no, SYSDATE, v_fine_amt);
    END IF;
    COMMIT;
    DBMS_OUTPUT.PUT_LINE('Book returned. Fine: Rs ' || v_fine_amt);
EXCEPTION
    WHEN e_no_borrower THEN
        DBMS_OUTPUT.PUT_LINE('Error: No active borrow record.');
        ROLLBACK;
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
        ROLLBACK;
END;
/
