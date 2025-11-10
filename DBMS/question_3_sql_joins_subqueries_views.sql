-- 10 SQL queries: joins, subqueries, views
-- Quick guide to joins:
-- - INNER: only matching rows
-- - LEFT: keep all left rows (fill missing right with NULL)
-- - RIGHT: keep all right rows
-- - FULL: keep both sides
-- - CROSS: Cartesian product

-- 1) INNER JOIN: only matching student/book with open issues
SELECT s.roll_no, s.name, b.title, i.date_of_issue, i.due_date
FROM issue i
JOIN student s ON s.student_id = i.student_id
JOIN book b    ON b.book_id    = i.book_id
WHERE i.status='I';

-- 2) LEFT JOIN: lists all students, issues may be NULL
SELECT s.roll_no, s.name, i.issue_id
FROM student s
LEFT JOIN issue i ON i.student_id = s.student_id AND i.status='I'
ORDER BY s.roll_no;

-- 3) RIGHT JOIN: lists all books, issues may be NULL
SELECT i.issue_id, b.title
FROM issue i
RIGHT JOIN book b ON b.book_id = i.book_id AND i.status='I'
ORDER BY b.title;

-- 4) FULL OUTER JOIN: keeps all from both sides
SELECT NVL(s.roll_no,'-') AS roll_no, b.title, i.issue_id
FROM issue i
FULL OUTER JOIN student s ON s.student_id = i.student_id
FULL OUTER JOIN book b    ON b.book_id    = i.book_id
ORDER BY 3 NULLS LAST;

-- 5) CROSS JOIN: pairs each student with one picked book
SELECT s.roll_no, b.title
FROM student s CROSS JOIN (
  SELECT b.* FROM book b WHERE ROWNUM <= 1
) b;

-- 6) Subquery (IN): filter by book borrowed
SELECT roll_no, name FROM student
WHERE student_id IN (
  SELECT i.student_id FROM issue i JOIN book b ON b.book_id = i.book_id
  WHERE b.title = 'Database Systems'
);

-- 7) EXISTS: check if a related overdue row exists
SELECT s.roll_no, s.name
FROM student s
WHERE EXISTS (
  SELECT 1 FROM issue i
  WHERE i.student_id = s.student_id AND i.status='I' AND i.due_date < TRUNC(SYSDATE)
);

-- 8) Scalar subquery: compute days since issue
SELECT i.issue_id,
       (SELECT TRUNC(SYSDATE - i.date_of_issue) FROM dual) AS days_since_issue
FROM issue i
WHERE i.status='I';

-- 9) View usage: read from saved SELECT
SELECT * FROM vw_overdue_issues;

-- 10) WITH (CTE): precompute counts then select
WITH student_issue AS (
  SELECT s.student_id, s.roll_no, s.name, COUNT(*) AS cnt
  FROM student s LEFT JOIN issue i ON i.student_id = s.student_id AND i.status='I'
  GROUP BY s.student_id, s.roll_no, s.name
)
SELECT roll_no, name, cnt FROM student_issue WHERE cnt >= 0 ORDER BY cnt DESC;
