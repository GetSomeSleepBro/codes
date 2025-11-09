-- Oracle SQL: Joins, Subqueries, and View usage (10+ examples)
-- Uses schema from sql/oracle_ddl_objects.sql

-- 1) INNER JOIN: books with authors
SELECT bk.title, au.name AS author, bk.published_year
  FROM books bk
  JOIN authors au ON au.author_id = bk.author_id;

-- 2) LEFT OUTER JOIN: members with any borrowings
SELECT m.name AS member_name, b.borrow_id, b.status
  FROM members m
  LEFT JOIN borrowings b ON b.member_id = m.member_id
 ORDER BY m.name;

-- 3) RIGHT OUTER JOIN: borrowings with member details (demonstration)
SELECT m.name AS member_name, b.borrow_id, b.book_id
  FROM members m
  RIGHT JOIN borrowings b ON b.member_id = m.member_id
 ORDER BY b.borrow_id;

-- 4) FULL OUTER JOIN: authors and their books (shows authors without books and books without authors)
SELECT au.name AS author, bk.title
  FROM authors au
  FULL OUTER JOIN books bk ON bk.author_id = au.author_id;

-- 5) CROSS JOIN: produce combinations (limit output)
SELECT au.name, bk.title
  FROM authors au
 CROSS JOIN books bk
 FETCH FIRST 5 ROWS ONLY;

-- 6) SELF JOIN: authors from the same country (pairs)
SELECT a1.name AS author1, a2.name AS author2, a1.country
  FROM authors a1
  JOIN authors a2 ON a1.country = a2.country AND a1.author_id < a2.author_id;

-- 7) Correlated subquery: books that are currently fully checked out (no available copies)
SELECT bk.title
  FROM books bk
 WHERE bk.copies_available = 0
   AND EXISTS (
         SELECT 1 FROM borrowings b
          WHERE b.book_id = bk.book_id AND b.status = 'I'
       );

-- 8) Scalar subquery: latest issue date per member
SELECT m.name,
       (SELECT MAX(b.date_of_issue) FROM borrowings b WHERE b.member_id = m.member_id) AS last_issue
  FROM members m
 ORDER BY last_issue DESC NULLS LAST;

-- 9) EXISTS: authors who have any currently borrowed book
SELECT DISTINCT au.name
  FROM authors au
 WHERE EXISTS (
   SELECT 1
     FROM books bk
     JOIN borrowings b ON b.book_id = bk.book_id
    WHERE bk.author_id = au.author_id
      AND b.status = 'I'
 );

-- 10) WITH clause (subquery factoring): overdue items with days overdue
WITH overdue AS (
  SELECT b.borrow_id, m.name AS member_name, bk.title,
         TRUNC(SYSDATE) - b.due_date AS days_overdue
    FROM borrowings b
    JOIN members m ON m.member_id = b.member_id
    JOIN books   bk ON bk.book_id = b.book_id
   WHERE b.status = 'I' AND b.due_date < TRUNC(SYSDATE)
)
SELECT * FROM overdue ORDER BY days_overdue DESC;

-- 11) View usage: list current borrowings (from v_current_borrowings)
SELECT member_name, title, date_of_issue, due_date
  FROM v_current_borrowings
 ORDER BY due_date;

-- 12) Anti-join: members without any current borrowings
SELECT m.*
  FROM members m
 WHERE NOT EXISTS (
   SELECT 1 FROM borrowings b WHERE b.member_id = m.member_id AND b.status = 'I'
 );

