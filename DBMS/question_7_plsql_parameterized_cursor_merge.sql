-- Parameterized cursor to merge N_RollCall into O_RollCall
-- Short guide:
-- - Cursor takes a range of roll numbers
-- - Skips rows that already exist in O_ROLLCALL

-- Base tables
CREATE TABLE o_rollcall (
  roll_no NUMBER PRIMARY KEY,
  name    VARCHAR2(100) NOT NULL
);

CREATE TABLE n_rollcall (
  roll_no NUMBER,
  name    VARCHAR2(100)
);

-- Sample new data
INSERT INTO n_rollcall(roll_no, name) VALUES (1, 'Riya');
INSERT INTO n_rollcall(roll_no, name) VALUES (2, 'Dev');
INSERT INTO n_rollcall(roll_no, name) VALUES (3, 'Neha');
COMMIT;

DECLARE
  CURSOR c_new(p_min NUMBER, p_max NUMBER) IS
    SELECT roll_no, name FROM n_rollcall
    WHERE roll_no BETWEEN p_min AND p_max;
  v_cnt NUMBER;
BEGIN
  FOR r IN c_new(1, 9999) LOOP
    -- Check if target already has the roll
    SELECT COUNT(*) INTO v_cnt FROM o_rollcall o WHERE o.roll_no = r.roll_no;
    IF v_cnt = 0 THEN
      -- Only insert missing rows
      INSERT INTO o_rollcall(roll_no, name) VALUES (r.roll_no, r.name);
    END IF;
  END LOOP;
  COMMIT;
END;
/
