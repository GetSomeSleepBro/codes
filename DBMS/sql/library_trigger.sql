-- Oracle Triggers: Row-level and Statement-level for Library auditing
-- Tables: Library, Library_Audit

PROMPT Creating sequences...
CREATE SEQUENCE seq_library START WITH 1 INCREMENT BY 1 NOCACHE;
CREATE SEQUENCE seq_library_audit START WITH 1 INCREMENT BY 1 NOCACHE;

PROMPT Creating tables...
CREATE TABLE Library (
  library_id NUMBER PRIMARY KEY,
  title      VARCHAR2(200) NOT NULL,
  author     VARCHAR2(100),
  category   VARCHAR2(50),
  last_updated DATE DEFAULT SYSDATE NOT NULL
);

CREATE TABLE Library_Audit (
  audit_id    NUMBER PRIMARY KEY,
  library_id  NUMBER,
  title       VARCHAR2(200),
  author      VARCHAR2(100),
  category    VARCHAR2(50),
  action      VARCHAR2(10) NOT NULL,
  changed_at  DATE DEFAULT SYSDATE NOT NULL,
  changed_by  VARCHAR2(100)
);

PROMPT Creating row-level BEFORE trigger...
CREATE OR REPLACE TRIGGER trg_library_row_bu
BEFORE UPDATE OR DELETE ON Library
FOR EACH ROW
BEGIN
  INSERT INTO Library_Audit(
    audit_id, library_id, title, author, category, action, changed_at, changed_by
  ) VALUES (
    seq_library_audit.NEXTVAL,
    :OLD.library_id, :OLD.title, :OLD.author, :OLD.category,
    CASE WHEN DELETING THEN 'DELETE' ELSE 'UPDATE' END,
    SYSDATE,
    USER
  );

  IF UPDATING THEN
    :NEW.last_updated := SYSDATE;
  END IF;
END;
/

PROMPT Creating statement-level AFTER trigger (summary log)...
CREATE OR REPLACE TRIGGER trg_library_stmt_ad
AFTER UPDATE OR DELETE ON Library
DECLARE
BEGIN
  INSERT INTO Library_Audit(audit_id, library_id, title, author, category, action, changed_at, changed_by)
  VALUES (seq_library_audit.NEXTVAL, NULL, NULL, NULL, NULL,
          CASE WHEN ORA_SYSEVENT = 'UPDATE' THEN 'STMT_UPDATE' ELSE 'STMT_DELETE' END,
          SYSDATE, USER);
END;
/

PROMPT Sample data and demo DML...
INSERT INTO Library(library_id, title, author, category) VALUES (seq_library.NEXTVAL, 'The Pragmatic Programmer', 'Andrew Hunt', 'Software');
INSERT INTO Library(library_id, title, author, category) VALUES (seq_library.NEXTVAL, 'Clean Code', 'Robert C. Martin', 'Software');
COMMIT;

-- Trigger demo operations
UPDATE Library SET author = 'R. Martin' WHERE title = 'Clean Code';
DELETE FROM Library WHERE title = 'The Pragmatic Programmer';
COMMIT;

-- View audit
SELECT action, library_id, title, changed_at, changed_by FROM Library_Audit ORDER BY audit_id;

