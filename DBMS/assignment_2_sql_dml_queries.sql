conn system
CREATE TABLE Employ(EmpId INT PRIMARY KEY,Name VARCHAR(10),Dept VARCHAR(5), Salary 
decimal (8,2),City VARCHAR(5));
insert into Employ values(1,'Ravi Patil','HR',40000,'Pune');
insert into Employ values(2,'Sneha','IT',60000,'Latur');
insert into Employ values(3,'Payal','ENTC',40000,'Pune');
insert into Employ values(4,'Mansi','MECH',91000,'Latur');
insert into Employ values(5,'Shaili','ENTC',40000,'Nagar');
desc Employ
select * from Employ;
update Employ set Salary = Salary + (Salary  * 0.10);
delete from Employ where Dept = 'IT';
select * from Employ;
select * from Employ where Salary>45000;
select * from Employ where name LIKE 's%';
select * from Employ where name LIKE 'S%';
select Distinct Dept from Employ;
update Employ set Salary = Salary + 2000 where City = 'Latur';
select max(Salary) from Employ;
select avg(Salary) from Employ where Dept = 'HR';
