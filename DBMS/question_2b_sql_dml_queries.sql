-- 10 SQL DML queries against the library schema
-- Quick guide:
-- - INSERT: add rows
-- - UPDATE: modify rows
-- - SELECT: read rows
-- - DELETE: remove rows

-- 1) Insert a student
INSERT INTO student(student_id, roll_no, name, email)
VALUES (seq_student.NEXTVAL, 'CS-001', 'Alice', 'alice@example.com');

-- 2) Insert another student
INSERT INTO student(student_id, roll_no, name, email)
VALUES (seq_student.NEXTVAL, 'CS-002', 'Bob', 'bob@example.com');

-- 3) Insert books
INSERT INTO book(book_id, title, author, published_year, available_copies)
VALUES (seq_book.NEXTVAL, 'Database Systems', 'Elmasri', 2016, 3);
INSERT INTO book(book_id, title, author, published_year, available_copies)
VALUES (seq_book.NEXTVAL, 'Operating Systems', 'Silberschatz', 2018, 2);

-- 4) Issue a book to Alice for 14 days (I = issued)
INSERT INTO issue(issue_id, student_id, book_id, date_of_issue, due_date, status)
SELECT seq_issue.NEXTVAL, s.student_id, b.book_id, TRUNC(SYSDATE), TRUNC(SYSDATE)+14, 'I'
FROM student s JOIN book b ON b.title='Database Systems'
WHERE s.roll_no='CS-001' AND ROWNUM=1;

-- 5) Reduce available copies after issuing (simple stock decrease)
UPDATE book SET available_copies = available_copies - 1
WHERE title = 'Database Systems' AND available_copies > 0;

-- 6) List all current issues with student and book (join three tables)
SELECT i.issue_id, s.roll_no, s.name, b.title, i.date_of_issue, i.due_date
FROM issue i
JOIN student s ON s.student_id = i.student_id
JOIN book b    ON b.book_id    = i.book_id
WHERE i.status = 'I'
ORDER BY i.due_date;

-- 7) Mark a return for an issue (set status to R)
UPDATE issue SET status='R' WHERE issue_id = (
  SELECT MIN(issue_id) FROM issue WHERE status='I'
);

-- 8) Insert a fine for a returned issue (example flat 50)
INSERT INTO fine(fine_id, student_id, issue_id, fine_date, amount)
SELECT seq_fine.NEXTVAL, i.student_id, i.issue_id, TRUNC(SYSDATE), 50
FROM issue i
WHERE i.status='R' AND ROWNUM=1;

-- 9) Aggregate: count issues per student (GROUP BY)
SELECT s.roll_no, s.name, COUNT(*) AS issue_count
FROM issue i JOIN student s ON s.student_id = i.student_id
GROUP BY s.roll_no, s.name
HAVING COUNT(*) >= 1
ORDER BY issue_count DESC;

-- 10) Delete a student with no issues (NOT EXISTS)
DELETE FROM student s
WHERE NOT EXISTS (
  SELECT 1 FROM issue i WHERE i.student_id = s.student_id
)
AND s.roll_no='CS-002';
