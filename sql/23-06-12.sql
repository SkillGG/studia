show databases;

create database `zajecia612232`;

use `zajecia612232`;

show tables;

describe `studenci`;

drop table `studenci`;

create table studenci(
	id int auto_increment,
	imie varchar(50),
    nazwisko varchar(50),
	wiek int,
    hobby varchar(50),
    primary key(id)
);