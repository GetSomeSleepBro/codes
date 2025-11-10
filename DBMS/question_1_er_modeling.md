Conceptual Design: College Library Lending

- Entities
  - Student(student_id, roll_no, name, email)
  - Book(book_id, title, author, published_year, available_copies)
  - Issue(issue_id, date_of_issue, due_date, status)
  - Fine(fine_id, fine_date, amount)

- Relationships
  - Student borrows Book via Issue: Student(1) — Issue(M) — Book(1)
  - Issue may incur Fine: Issue(1) — Fine(0..M)

- Keys and Cardinalities
  - Student: PK student_id; roll_no UNIQUE
  - Book: PK book_id
  - Issue: PK issue_id; FK student_id→Student, book_id→Book
  - Fine: PK fine_id; FK issue_id→Issue, student_id→Student
  - Issue.status in {'I','R'} for Issued/Returned

- Attributes
  - Student: name NOT NULL; email optional, simple validation
  - Book: title, author NOT NULL; published_year; available_copies ≥ 0
  - Issue: date_of_issue, due_date; status default 'I'
  - Fine: fine_date default current date; amount ≥ 0

ER→Relational Mapping (3NF)

- STUDENT(student_id PK, roll_no UNIQUE NOT NULL, name NOT NULL, email)
- BOOK(book_id PK, title NOT NULL, author NOT NULL, published_year, available_copies DEFAULT 0)
- ISSUE(issue_id PK, student_id FK NOT NULL, book_id FK NOT NULL, date_of_issue NOT NULL, due_date NOT NULL, status CHECK('I','R') DEFAULT 'I')
- FINE(fine_id PK, student_id FK NOT NULL, issue_id FK NOT NULL, fine_date NOT NULL, amount NOT NULL)

Normalization Notes

- 1NF: All attributes atomic; repeating groups removed (Issue and Fine separated)
- 2NF: No partial dependency on composite keys (each table uses a single-column surrogate PK)
- 3NF: No transitive dependencies (e.g., Student email not stored elsewhere; Fine does not store book details)

Additional Objects (for SQL practice)

- Sequence objects to generate IDs
- View for overdue issues
- Indexes for common lookups (issue status/student)
- Synonym for convenient access to BOOK

