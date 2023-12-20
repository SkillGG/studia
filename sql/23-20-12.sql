show databases;

create database if not exists mm_zajecia1;

use mm_zajecia1;

create table zamowienie(
	id int primary key auto_increment,
    cena decimal(10,2),
    klient varchar(100),
    data_zam date,
    przedmiot varchar(50),
    ilosc int,
    wzrost int,
    kolor varchar(30)
);

describe zamowienie;