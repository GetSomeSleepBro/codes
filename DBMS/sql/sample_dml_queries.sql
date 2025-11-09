-- Oracle SQL DML Queries (at least 10)
-- Uses schema created in sql/oracle_ddl_objects.sql

-- 1) Insert a new member
INSERT INTO members(member_id, roll_no, name, email)
VALUES (seq_members.NEXTVAL, 'R003', 'Charlie', 'charlie@example.com');

-- 2) Upsert (MERGE) a member by roll_no
MERGE INTO members m
USING (
  SELECT 'R004' AS roll_no, 'Diana' AS name, 'diana@example.com' AS email FROM dual
) s
ON (m.roll_no = s.roll_no)
WHEN MATCHED THEN UPDATE SET m.name = s.name, m.email = s.email, m.status = 'A'
WHEN NOT MATCHED THEN INSERT (member_id, roll_no, name, email, status)
VALUES (seq_members.NEXTVAL, s.roll_no, s.name, s.email, 'A');

-- 3) Issue a book to Alice (R001) for 14 days
INSERT INTO borrowings (borrow_id, member_id, book_id, date_of_issue, due_date, status)
SELECT seq_borrowings.NEXTVAL, m.member_id, b.book_id, TRUNC(SYSDATE), TRUNC(SYSDATE)+14, 'I'
  FROM members m
  JOIN books b ON b.title = 'Harry Potter and the Philosopher''s Stone'
 WHERE m.roll_no = 'R001';

-- 4) Decrease copies_available for the issued book
UPDATE books
   SET copies_available = copies_available - 1
 WHERE title = 'Harry Potter and the Philosopher''s Stone'
   AND copies_available > 0;

-- 5) Query current borrowings using the view
SELECT * FROM v_current_borrowings;

-- 6) List members who have never borrowed a book (anti-join via NOT EXISTS)
SELECT m.*
  FROM members m
 WHERE NOT EXISTS (SELECT 1 FROM borrowings b WHERE b.member_id = m.member_id);

-- 7) Insert a fine for an overdue borrowing (example logic)
INSERT INTO fines (fine_id, borrow_id, member_id, amount, reason)
SELECT seq_fines.NEXTVAL, b.borrow_id, b.member_id, 50, 'Overdue example'
  FROM borrowings b
 WHERE b.status = 'I'
   AND b.due_date < TRUNC(SYSDATE)
   AND ROWNUM = 1;

-- 8) Mark a borrowing as returned and set return_date
UPDATE borrowings
   SET status = 'R', return_date = TRUNC(SYSDATE)
 WHERE borrow_id = (
   SELECT MIN(borrow_id) FROM borrowings WHERE status = 'I'
 );

-- 9) Delete a member with no borrowings by roll number
DELETE FROM members m
 WHERE m.roll_no = 'R003'
   AND NOT EXISTS (SELECT 1 FROM borrowings b WHERE b.member_id = m.member_id);

-- 10) Insert a new book
INSERT INTO books(book_id, title, author_id, published_year, category, copies_total, copies_available)
VALUES (seq_books.NEXTVAL, 'Clean Code', 1, 2008, 'Software', 5, 5);

-- 11) Increase available copies for returned books (data fix pattern)
UPDATE books bk
   SET copies_available = copies_available + 1
 WHERE bk.book_id IN (
   SELECT b.book_id FROM borrowings b WHERE b.status = 'R' AND b.return_date = TRUNC(SYSDATE)
 );

-- 12) Top 5 most borrowed books (order by borrow count)
SELECT bk.title, COUNT(*) borrow_count
  FROM borrowings b
  JOIN books bk ON bk.book_id = b.book_id
 GROUP BY bk.title
 ORDER BY borrow_count DESC
 FETCH FIRST 5 ROWS ONLY;

COMMIT;

