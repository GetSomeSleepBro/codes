-- Create tables
CREATE TABLE Student2 (
    student_id INT PRIMARY KEY,
    name VARCHAR(10),
    age INT,
    dept VARCHAR(10)
);

CREATE TABLE Enrollment2 (
    enroll_id INT PRIMARY KEY,
    student_id INT,
    course_name VARCHAR(10),
    marks INT,
    FOREIGN KEY (student_id) REFERENCES Student2(student_id)
);

-- Insert sample data
INSERT INTO Student2 VALUES (1, 'Amit', 21, 'CSE');
INSERT INTO Student2 VALUES (2, 'Sneha', 20, 'IT');
INSERT INTO Student2 VALUES (3, 'Rahul', 22, 'ECE');
INSERT INTO Student2 VALUES (4, 'Pooja', 21, 'CSE');

INSERT INTO Enrollment2 VALUES (101, 1, 'SQL', 85);
INSERT INTO Enrollment2 VALUES (102, 2, 'SQL', 78);
INSERT INTO Enrollment2 VALUES (103, 3, 'Java', 90);
INSERT INTO Enrollment2 VALUES (104, 4, 'Python', 88);
INSERT INTO Enrollment2 VALUES (105, 1, 'Java', 82);
INSERT INTO Enrollment2 VALUES (106, 4, 'SQL', 95);

-- 1. Display all students and their enrolled courses (LEFT JOIN)
SELECT s.name, e.course_name
FROM Student2 s
LEFT JOIN Enrollment2 e ON s.student_id = e.student_id
ORDER BY s.name;

-- 2. List students who have scored more than 80 marks in any course (Subquery)
SELECT name
FROM Student2
WHERE student_id IN (
    SELECT student_id
    FROM Enrollment2
    WHERE marks > 80
);

-- 3. Display the highest marks obtained in the SQL course (Aggregate + Subquery)
SELECT MAX(marks) AS Highest_SQL_Marks
FROM Enrollment2
WHERE course_name = 'SQL';

-- 4. List all departments and average marks scored by their students (JOIN + GROUP BY)
SELECT s.dept, AVG(e.marks) AS Avg_Marks
FROM Student2 s
JOIN Enrollment2 e ON s.student_id = e.student_id
GROUP BY s.dept;

-- Bonus: CREATE VIEW for reusable query (e.g., High Performers)
CREATE OR REPLACE VIEW v_high_performers AS
SELECT s.name, e.course_name, e.marks
FROM Student2 s
JOIN Enrollment2 e ON s.student_id = e.student_id
WHERE e.marks > 85;

-- Query the view
SELECT * FROM v_high_performers;
