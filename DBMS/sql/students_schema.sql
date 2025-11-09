-- Oracle schema for student grading example
-- Tables: Stud_Marks(name, total_marks), Result(roll, name, class)

CREATE SEQUENCE seq_roll START WITH 1 INCREMENT BY 1 NOCACHE;

CREATE TABLE Stud_Marks (
  name        VARCHAR2(100) NOT NULL,
  total_marks NUMBER(4) NOT NULL CHECK (total_marks BETWEEN 0 AND 1500)
);

CREATE TABLE Result (
  roll   NUMBER PRIMARY KEY,
  name   VARCHAR2(100) NOT NULL,
  class  VARCHAR2(30)  NOT NULL
);

-- Sample data
INSERT INTO Stud_Marks(name, total_marks) VALUES ('Asha', 1490);
INSERT INTO Stud_Marks(name, total_marks) VALUES ('Bhavesh', 930);
INSERT INTO Stud_Marks(name, total_marks) VALUES ('Chetan', 860);
INSERT INTO Stud_Marks(name, total_marks) VALUES ('Deepa', 720);

COMMIT;

