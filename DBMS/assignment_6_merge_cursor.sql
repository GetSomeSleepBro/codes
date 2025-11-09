DECLARE
    CURSOR c_newroll(p_dept_id NUMBER) IS
        SELECT roll_no, student_name, dept_id
        FROM N_RollCall
        WHERE dept_id = p_dept_id;
    v_roll_no       N_RollCall.roll_no%TYPE;
    v_student_name  N_RollCall.student_name%TYPE;
    v_dept_id       N_RollCall.dept_id%TYPE;
    v_exists NUMBER;
BEGIN
    FOR rec_dept IN (SELECT DISTINCT dept_id FROM N_RollCall) LOOP
        OPEN c_newroll(rec_dept.dept_id);
        LOOP
            FETCH c_newroll INTO v_roll_no, v_student_name, v_dept_id;
            EXIT WHEN c_newroll%NOTFOUND;
            SELECT COUNT(*)
            INTO v_exists
            FROM O_RollCall
            WHERE roll_no = v_roll_no
              AND dept_id = v_dept_id;
            IF v_exists = 0 THEN
                INSERT INTO O_RollCall (roll_no, student_name, dept_id)
                VALUES (v_roll_no, v_student_name, v_dept_id);
            END IF;
        END LOOP;
        CLOSE c_newroll;
    END LOOP;
    DBMS_OUTPUT.PUT_LINE('Data merged successfully.');
END;
/
