-- Row-level trigger to audit updates/deletes on Library
-- Short guide:
-- - BEFORE UPDATE/DELETE: capture OLD row
-- - Write a copy into LIBRARY_AUDIT with action 'U' or 'D'

-- Tables
CREATE TABLE library (
  lib_id NUMBER PRIMARY KEY,
  title  VARCHAR2(200) NOT NULL,
  author VARCHAR2(100) NOT NULL,
  price  NUMBER(10,2)  NOT NULL,
  qty    NUMBER        DEFAULT 0 NOT NULL
);

CREATE TABLE library_audit (
  audit_id NUMBER PRIMARY KEY,
  lib_id   NUMBER,
  title    VARCHAR2(200),
  author   VARCHAR2(100),
  price    NUMBER(10,2),
  qty      NUMBER,
  action   CHAR(1) NOT NULL,
  changed_at DATE   DEFAULT SYSDATE NOT NULL
);

CREATE SEQUENCE seq_library START WITH 1 INCREMENT BY 1 NOCACHE;
CREATE SEQUENCE seq_library_audit START WITH 1 INCREMENT BY 1 NOCACHE;

-- Trigger
-- Trigger: fires per row on change
CREATE OR REPLACE TRIGGER trg_library_audit
BEFORE UPDATE OR DELETE ON library
FOR EACH ROW
DECLARE
  v_action CHAR(1);
BEGIN
  IF UPDATING THEN
    v_action := 'U';
  ELSIF DELETING THEN
    v_action := 'D';
  END IF;

  INSERT INTO library_audit(
    audit_id, lib_id, title, author, price, qty, action, changed_at
  ) VALUES (
    seq_library_audit.NEXTVAL,
    :OLD.lib_id, :OLD.title, :OLD.author, :OLD.price, :OLD.qty,
    v_action,
    SYSDATE
  );
END;
/
