-- PL/SQL Anonymous Block: Calculate area of circle for radius 5 to 9
-- Stores results in table: areas(radius NUMBER PRIMARY KEY, area NUMBER)

-- Run once to create table (uncomment if needed):
-- CREATE TABLE areas (
--   radius NUMBER PRIMARY KEY,
--   area   NUMBER(20,6)
-- );

SET SERVEROUTPUT ON;
DECLARE
  c_pi CONSTANT NUMBER := 3.14159265358979323846;
  v_area NUMBER(20,6);
BEGIN
  FOR r IN 5..9 LOOP
    v_area := c_pi * r * r;
    BEGIN
      INSERT INTO areas(radius, area) VALUES (r, v_area);
      DBMS_OUTPUT.PUT_LINE('Inserted radius=' || r || ', area=' || v_area);
    EXCEPTION
      WHEN DUP_VAL_ON_INDEX THEN
        UPDATE areas SET area = v_area WHERE radius = r;
        DBMS_OUTPUT.PUT_LINE('Updated radius=' || r || ' with area=' || v_area);
    END;
  END LOOP;
  COMMIT;
END;
/

