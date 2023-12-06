show databases;

create database `zajecia612232`;

use `zajecia612232`;

show tables;

create table studenci(
	id int auto_increment,
	imie varchar(50),
    nazwisko varchar(50),
	wiek int,
    hobby varchar(50),
    primary key(id)
);

describe `studenci`;

select * from `studenci`;

insert into `studenci`(imie,nazwisko,wiek,hobby) values ("Ada", "Śmietańska", 24, "Rosyjski");

insert into `studenci` values ("Marcin", "Adamczyk", 21, "Piłka nożna");

insert into `studenci` values (null, "Marcin", "Pluta", 20, "Planszówki");

insert into `studenci`(imie, nazwisko) values ("Agata", "Kiszewska");