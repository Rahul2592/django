-- To get list Of Databases
show databases;

/*
To create Database
*/
CREATE DATABASE batch3to4APMarch;
-- To select Database
Use batch3to4APMarch;

-- Create Table
CREATE TABLE unit
(id int primary key,
city varchar(10) unique,
capacity int); 

-- to get List of tables
show Tables;

-- to get Table Info
desc unit;
Describe unit;

-- Create Table with FK
Create Table parts(
id int, 
name varchar(10), 
color varchar(10),
unit_id int,
primary key (id),
foreign key parts(unit_id) references unit(id)

);


Create Table Department(did int primary key, name varchar(10));
Create Table Employee (
eid int ,
name varchar(10),
address varchar(10),
did int,
primary key(eid),
foreign key(did) references department(did)
);

/*
Alter: after creation of the table if you want to make Changes 
in Definition 

ADD 
DROP
Modify
Rename
*/
-- add column at the end
Alter table department ADD location varchar(20);
describe department;
-- add column at specific location
Alter table department ADD  contact_Number bigint after did;
-- Add Multiple Columns at once
Alter Table department ADD (email varchar(12), fname varchar(20));

-- to delete existing column
Alter table department Drop fname;

-- Modify Size
Alter table department modify name varchar(20);
-- Modify DAta type
Alter table department modify contact_number int;

-- Rename
Alter table department change name Dept_Name varchar(20);
-- Alter table department Rename name To Dept_Name varchar(20);

/*
Create Table User with Columns
Uid(pk) 	name	address
2. Add email column in User Table
3. Rename name column to UserNAme
4. REdine the size for the Address column
5. Delete the column email
*/
-- Delete DataBase
Drop database batch3to4apmarch;
-- Delete Table
Drop table unit;

-- DML: Data Manipulation Language
/*
Insert
Update
DElete
*/
-- DQL: Select 
-- Single row with Predefined columns sequence
Insert into unit values(1,'Indore',9080);

 Insert into units (capacity, id, city) values(2000,2,"Bhopal"); 
Insert into unit ( id, city) values("Delhi",5); 

Insert Into parts values
(1,"Nut","Black",1),
(2,"Bolt","Black",1),
(3,'Screw','Red',4),
(4,"Gear","Red",2),
(5,'Plates','Blue',2);

/*
Insert 5 rows in mArksheet table
rollno name phy chem maths
*/

-- Insert Into table_name values(v1,v2,v3);

Update unit set capacity=3000 where id=3;
Update unit set capacity=4000, city="Pune" where id=3;

-- delete single row
delete from parts where id= 5;
-- delete whole data of table at once. 
truncate parts;

-- DQL: data Query Language

-- Select all data 
select * from unit;

-- get 1 row
select * from unit where id=1;

-- get Single column
select city from unit;

-- more than 1 columns
select id,city from unit;

-- Relational Opeartors
select * from unit where capacity>2000;
select * from unit where capacity>=2000;
select * from unit where capacity<2000;
select * from unit where capacity<=2000;
select * from unit where capacity=2000;
select * from unit where capacity!=2000;
select * from unit where capacity<>2000;

-- Logical Opeartors
select * from unit where id=1 and city="Ujjain";
select * from unit where id=1 and city="Indore";
select * from unit where id=1 OR city="Pune";
Select * from unit where Not city="INdore";

-- In ,Between Clouse
Select * from unit where capacity>=3000 and capacity<=8000;
Select * from unit where capacity Between 3000 and 8000;
select * from unit where city='Indore' or city='Pune' or city='Delhi';

select * from unit where city IN('INdore',"Pune","Delhi");


-- Arithmetic Operators
select id, capacity, id+capacity from unit;
select capacity+10 , capacity from unit;
select capacity-10 , capacity from unit;
select capacity/10 , capacity from unit;
select capacity*10 , capacity from unit;
select capacity%10 , capacity from unit;

-- sort
select * from unit order by capacity;
select * from unit order by capacity Asc;
select * from unit order by capacity DESC;

-- Limit index,count clouse
select * from unit limit 3;
select * from unit limit 0,2; -- 0,1
select * from unit limit 2,3;

-- Write a query to get topper of the physics;
select * from unit order by capacity desc limit 1;
select * from unit order by capacity desc limit 1,1;
select * from unit order by capacity  limit 1;

-- Like
/*
_ : single charctaer replacement
% : Multi character replacement
*/
select * from parts where name like "b%";

select * from parts where name like "_c%";
select * from parts where name like "%t";
select * from parts where name like "_u_";


-- Aggregated Function
select sum(capacity) from unit;
select max(capacity),min(capacity) from unit;
select max(city),min(city) from unit;
select count(*) from unit;
select count(capacity) from unit;
select avg(capacity) from unit;

-- Aliases
select sum(capacity) from unit;
select sum(capacity) as Total_cap from unit;
select max(capacity) Max_cap from unit;

select p.id , u.id from unit as u,parts as p;

-- Group By
select color , count(color) as Part_Count from parts group by color;
-- select color, count(color) 
-- as Part_Count from parts group by color
-- where Part_Count>=2;

-- Having 

select color , count(color) as Part_count from parts
group by color having part_count>=2;

insert into orderdata values(1,200,"2023-3-12",1);
-- Nested Query
select * from parts where id IN(
select parts_id from orderdata where qty>100
);
Select * from unit where id 
in(select unit_id from parts where id 
in(select parts_id from orderdata where qty>100));

select * from parts where unit_id=(
select id from unit where city="Indore");
select * from parts where id IN(
select parts_id from orderdata where orderdate="2023-03-12" and qty>100);

# create a duplicate table
create table unit_copy like Unit;

# Create duplicate Table with Data
create Table parts_copy as Select * from parts;

# create Views
create View Parts_info_order_Date as
select * from parts where id IN(
select parts_id from orderdata where orderdate="2023-03-12" and qty>100);

select * from Parts_info_order_Date;

# Stored Procedure
DElimiter $$
Create Procedure getPartsName(In i int , Out n varchar(20))
Begin
SElect name from parts where id=i into n;
End$$


Delimiter $$
create Procedure getAllData()
Begin
Select * from unit;
End$$

Call GetAllData()


Call getPartsName(1,@name);
Select @name;

Call getPartsName(3,@name);
Select @name as Name;

Delimiter ##
Create procedure getMaxCap(Out cap int)
begin
SElect max(capacity) from unit into cap;
end##

Call getMaxCap(@c);
select @c Capacity;

delimiter $$
Create Procedure getNameAndColor(IN i int, Out n varchar(20), Out c Varchar(20))
Begin
SElect name, color from parts where id=i into n,c;
End$$

Call getNameAndColor(1,@n,@c);
Select @n as Name, @c as color;

-- Stored Function
DElimiter $$
create Function getCity(i int) Returns varchar(20)
deterministic reads sql data
Begin
declare c varchar(20);
select city from unit where id=i into c;
Return c;
End$$

Select getCity(1);
Select getCity(2);

-- Trigger: executes automaticaly on a certain events
/*
Before Insert 			After Insert
Before Update			After Update
Before Delete			After Delete

*/

delimiter $$
Create trigger partsDelete Before Delete on parts
for each row
begin
Insert into parts_copy
values(
OLD.id,old.name,old.color,old.unit_id,now(),"Delete"
);
end$$

Delete from parts where id=5;


-- joins 
-- Left Join
-- select * from unit,parts;
select * from unit Left Join parts on unit.id=parts.unit_id;

-- Left Outer Join
select * from unit Left Join parts on unit.id=parts.unit_id where parts.id is null;

-- right join
select * from unit Right Join parts on unit.id=parts.unit_id;

-- outer right join
select * from unit Right Join parts
on unit.id=parts.unit_id where unit.id is null;

-- Innner Join
select * from unit Inner Join parts on unit.id=parts.unit_id;

-- select * from unit Outer Join parts on unit.id=parts.unit_id;
select * from unit Left Join parts on unit.id=parts.unit_id
union
select * from unit Right Join parts on unit.id=parts.unit_id;


select * from unit Left Join parts 
on unit.id=parts.unit_id where parts.id is null
union

select * from unit Right Join parts
on unit.id=parts.unit_id where unit.id is null;
