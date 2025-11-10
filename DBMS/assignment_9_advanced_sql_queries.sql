-- Create sample tables
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    dept VARCHAR(20)
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50),
    credits INT
);

CREATE TABLE enrollments (
    student_id INT,
    course_id INT,
    grade CHAR(2),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Insert sample data
INSERT INTO students VALUES (1, 'Alice', 'CS');
INSERT INTO students VALUES (2, 'Bob', 'EE');
INSERT INTO courses VALUES (101, 'DBMS', 3);
INSERT INTO courses VALUES (102, 'OS', 4);
INSERT INTO enrollments VALUES (1, 101, 'A');
INSERT INTO enrollments VALUES (1, 102, 'B');
INSERT INTO enrollments VALUES (2, 101, 'C');

-- Query 1: Inner Join - Students and their courses
SELECT s.name, c.course_name
FROM students s
INNER JOIN enrollments e ON s.student_id = e.student_id
INNER JOIN courses c ON e.course_id = c.course_id;

-- Query 2: Subquery - Students with grades > average
SELECT name
FROM students
WHERE student_id IN (
    SELECT student_id
    FROM enrollments
    WHERE grade > (SELECT AVG(grade) FROM enrollments)
);

-- Query 3: GROUP BY - Average credits per department
SELECT s.dept, AVG(c.credits) AS avg_credits
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id
GROUP BY s.dept
HAVING AVG(c.credits) > 3;

-- Query 4: Set Operation - Union of high-grade students from two courses
SELECT s.name FROM students s
JOIN enrollments e ON s.student_id = e.student_id
WHERE e.course_id = 101 AND e.grade = 'A'
UNION
SELECT s.name FROM students s
JOIN enrollments e ON s.student_id = e.student_id
WHERE e.course_id = 102 AND e.grade = 'A';
