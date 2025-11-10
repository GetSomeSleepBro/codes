-- Oracle SQL DDL: library schema objects
-- Short guide:
-- - Sequences: auto-generate numeric IDs
-- - Tables: core data with constraints for safety
-- - Indexes: speed up lookups
-- - View: handy saved SELECT
-- - Synonym: shorter name/alias

-- Sequences
-- Sequences (ID generators)
CREATE SEQUENCE seq_student START WITH 1 INCREMENT BY 1 NOCACHE; -- for STUDENT.student_id
CREATE SEQUENCE seq_book    START WITH 1 INCREMENT BY 1 NOCACHE; -- for BOOK.book_id
CREATE SEQUENCE seq_issue   START WITH 1 INCREMENT BY 1 NOCACHE; -- for ISSUE.issue_id
CREATE SEQUENCE seq_fine    START WITH 1 INCREMENT BY 1 NOCACHE; -- for FINE.fine_id

-- Tables
-- Core tables
CREATE TABLE student (
  student_id   NUMBER       PRIMARY KEY,
  roll_no      VARCHAR2(20) NOT NULL UNIQUE,
  name         VARCHAR2(100) NOT NULL,
  email        VARCHAR2(200),
  CONSTRAINT ck_student_email CHECK (email IS NULL OR INSTR(email,'@') > 0) -- simple email check
);

CREATE TABLE book (
  book_id          NUMBER        PRIMARY KEY,
  title            VARCHAR2(200) NOT NULL,
  author           VARCHAR2(100) NOT NULL,
  published_year   NUMBER(4),
  available_copies NUMBER        DEFAULT 0 NOT NULL,
  CONSTRAINT ck_book_year CHECK ( -- allow null or realistic years
    published_year IS NULL OR (published_year BETWEEN 1900 AND EXTRACT(YEAR FROM SYSDATE))
  ),
  CONSTRAINT ck_book_copies CHECK (available_copies >= 0) -- no negative stock
);

CREATE TABLE issue (
  issue_id      NUMBER      PRIMARY KEY,
  student_id    NUMBER      NOT NULL,
  book_id       NUMBER      NOT NULL,
  date_of_issue DATE        DEFAULT SYSDATE NOT NULL,
  due_date      DATE        NOT NULL,
  status        CHAR(1)     DEFAULT 'I' NOT NULL,
  CONSTRAINT fk_issue_student FOREIGN KEY(student_id) REFERENCES student(student_id), -- who
  CONSTRAINT fk_issue_book    FOREIGN KEY(book_id)    REFERENCES book(book_id),      -- what
  CONSTRAINT ck_issue_status  CHECK (status IN ('I','R'))                               -- issued/returned
);

CREATE TABLE fine (
  fine_id   NUMBER    PRIMARY KEY,
  student_id NUMBER   NOT NULL,
  issue_id   NUMBER   NOT NULL,
  fine_date  DATE     DEFAULT SYSDATE NOT NULL,
  amount     NUMBER(10,2) NOT NULL,
  CONSTRAINT ck_fine_amt CHECK (amount >= 0), -- fine cannot be negative
  CONSTRAINT fk_fine_student FOREIGN KEY(student_id) REFERENCES student(student_id),
  CONSTRAINT fk_fine_issue   FOREIGN KEY(issue_id)   REFERENCES issue(issue_id) ON DELETE CASCADE
);

-- Indexes
-- Helpful indexes
CREATE INDEX idx_issue_student ON issue(student_id); -- filter by student quickly
CREATE INDEX idx_issue_status  ON issue(status);     -- filter by open/closed issues

-- View: overdue issues (due_date before today and not returned)
-- View of overdue (past due) open issues
CREATE OR REPLACE VIEW vw_overdue_issues AS
SELECT i.issue_id, s.roll_no, s.name AS student_name, b.title AS book_title,
       i.date_of_issue, i.due_date
FROM issue i
JOIN student s ON s.student_id = i.student_id
JOIN book b    ON b.book_id    = i.book_id
WHERE i.status = 'I' AND i.due_date < TRUNC(SYSDATE);

-- Synonym (private) for book
CREATE SYNONYM book_syn FOR book; -- shorter alias
