-- Oracle DDL Objects: Tables, Views, Indexes, Sequences, Synonym, Constraints
-- Schema: Library Management (Authors, Books, Members, Borrowings, Fines)
-- Notes:
-- - Designed for Oracle Database.
-- - Run this script in a schema you control.

PROMPT Creating sequences...
CREATE SEQUENCE seq_authors START WITH 1 INCREMENT BY 1 NOCACHE;
CREATE SEQUENCE seq_books   START WITH 1 INCREMENT BY 1 NOCACHE;
CREATE SEQUENCE seq_members START WITH 1 INCREMENT BY 1 NOCACHE;
CREATE SEQUENCE seq_borrowings START WITH 1 INCREMENT BY 1 NOCACHE;
CREATE SEQUENCE seq_fines   START WITH 1 INCREMENT BY 1 NOCACHE;

PROMPT Creating tables...
CREATE TABLE authors (
  author_id   NUMBER PRIMARY KEY,
  name        VARCHAR2(100) NOT NULL,
  country     VARCHAR2(50),
  created_at  DATE DEFAULT SYSDATE NOT NULL,
  CONSTRAINT uq_authors_name UNIQUE (name)
);

CREATE TABLE books (
  book_id         NUMBER PRIMARY KEY,
  title           VARCHAR2(200) NOT NULL,
  author_id       NUMBER NOT NULL,
  published_year  NUMBER(4) CHECK (published_year >= 1500),
  category        VARCHAR2(50),
  copies_total    NUMBER(4) DEFAULT 0 CHECK (copies_total >= 0),
  copies_available NUMBER(4) DEFAULT 0 CHECK (copies_available >= 0),
  CONSTRAINT fk_books_author FOREIGN KEY (author_id) REFERENCES authors(author_id),
  CONSTRAINT ck_books_copies CHECK (copies_available <= copies_total)
);

CREATE TABLE members (
  member_id  NUMBER PRIMARY KEY,
  roll_no    VARCHAR2(20),
  name       VARCHAR2(100) NOT NULL,
  email      VARCHAR2(100),
  joined_on  DATE DEFAULT TRUNC(SYSDATE) NOT NULL,
  status     CHAR(1) DEFAULT 'A' CHECK (status IN ('A','I')),
  CONSTRAINT uq_members_roll UNIQUE (roll_no)
);

CREATE TABLE borrowings (
  borrow_id     NUMBER PRIMARY KEY,
  member_id     NUMBER NOT NULL,
  book_id       NUMBER NOT NULL,
  date_of_issue DATE DEFAULT TRUNC(SYSDATE) NOT NULL,
  due_date      DATE NOT NULL,
  return_date   DATE,
  status        CHAR(1) DEFAULT 'I' CHECK (status IN ('I','R','O')),
  CONSTRAINT fk_bor_member FOREIGN KEY (member_id) REFERENCES members(member_id),
  CONSTRAINT fk_bor_book   FOREIGN KEY (book_id)   REFERENCES books(book_id),
  CONSTRAINT ck_due_after_issue CHECK (due_date >= date_of_issue)
);

CREATE TABLE fines (
  fine_id    NUMBER PRIMARY KEY,
  borrow_id  NUMBER,
  member_id  NUMBER NOT NULL,
  amount     NUMBER(10,2) NOT NULL CHECK (amount >= 0),
  fine_date  DATE DEFAULT TRUNC(SYSDATE) NOT NULL,
  reason     VARCHAR2(200),
  CONSTRAINT fk_fines_member FOREIGN KEY (member_id) REFERENCES members(member_id),
  CONSTRAINT fk_fines_borrow FOREIGN KEY (borrow_id) REFERENCES borrowings(borrow_id)
);

PROMPT Creating indexes...
CREATE INDEX idx_books_author_id ON books(author_id);
CREATE UNIQUE INDEX ux_books_title_author ON books(title, author_id);
CREATE INDEX idx_bor_member_book ON borrowings(member_id, book_id);
CREATE INDEX idx_fines_member ON fines(member_id);

PROMPT Creating view...
CREATE OR REPLACE VIEW v_current_borrowings AS
SELECT b.borrow_id,
       m.member_id,
       m.name AS member_name,
       bk.book_id,
       bk.title,
       b.date_of_issue,
       b.due_date,
       b.status
  FROM borrowings b
  JOIN members m ON m.member_id = b.member_id
  JOIN books   bk ON bk.book_id = b.book_id
 WHERE b.status = 'I';

PROMPT Creating synonym...
-- Public/private synonym. Use private synonym here.
CREATE OR REPLACE SYNONYM syn_books FOR books;

PROMPT Adding comments...
COMMENT ON TABLE books IS 'Books catalog for the library';
COMMENT ON COLUMN books.copies_available IS 'Must be <= copies_total';

PROMPT Sample seed data using sequences...
INSERT INTO authors(author_id, name, country)
VALUES (seq_authors.NEXTVAL, 'J. K. Rowling', 'UK');
INSERT INTO authors(author_id, name, country)
VALUES (seq_authors.NEXTVAL, 'George R. R. Martin', 'USA');

INSERT INTO books(book_id, title, author_id, published_year, category, copies_total, copies_available)
VALUES (seq_books.NEXTVAL, 'Harry Potter and the Philosopher''s Stone', 1, 1997, 'Fantasy', 10, 10);
INSERT INTO books(book_id, title, author_id, published_year, category, copies_total, copies_available)
VALUES (seq_books.NEXTVAL, 'A Game of Thrones', 2, 1996, 'Fantasy', 8, 8);

INSERT INTO members(member_id, roll_no, name, email)
VALUES (seq_members.NEXTVAL, 'R001', 'Alice', 'alice@example.com');
INSERT INTO members(member_id, roll_no, name, email)
VALUES (seq_members.NEXTVAL, 'R002', 'Bob', 'bob@example.com');

COMMIT;

