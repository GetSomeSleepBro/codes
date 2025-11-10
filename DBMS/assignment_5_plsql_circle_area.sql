-- Create table first (run separately)
CREATE TABLE areas (
    radius NUMBER,
    area NUMBER
);

DECLARE
    v_radius    NUMBER;
    v_area      NUMBER;
    pi          CONSTANT NUMBER := 3.14159265359;
BEGIN
    FOR v_radius IN 5..9 LOOP
        v_area := pi * POWER(v_radius, 2);
        INSERT INTO areas (radius, area)
        VALUES (v_radius, v_area);
        DBMS_OUTPUT.PUT_LINE('Radius: ' || v_radius || ', Area: ' || v_area);
    END LOOP;
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
        ROLLBACK;
END;
/
-- View results
SELECT * FROM areas;assignment_5_plsql_circle_area.sql
