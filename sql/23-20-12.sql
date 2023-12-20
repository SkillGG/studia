show databases;

create database if not exists mm_zajecia1;

use mm_zajecia1;

create table zamowienia(
	id int primary key auto_increment,
    cena decimal(10,2),
    klient varchar(100),
    data_zam date,
    przedmiot varchar(50),
    ilosc int,
    wzrost int,
    kolor varchar(30)
);

describe zamowienia;

insert into zamowienia values(null, 800.00, "Klient1", "2023-12-10", "garnitur", 1, 180, "czarny");

select * from `zamowienia`;

insert into zamowienia values
	(null, 200, "Klient6", "2023-12-10","garnitur", 1, 180, "szary"),
    (null, 600, "Klient5", "2023-12-10","koszula", 1, 200, "beżowy"),
    (null, 500, "Klient4", "2023-12-10","spodnie", 1, 150, "zielony"),
    (null, 250, "Klient3", "2023-12-10","spodnie", 1, 160, "beżowy"),
    (null, 150, "Klient2", "2023-12-10","koszula", 1, 173, "beżowy"),
    (null, 900, "Klient1", "2023-12-10","marynarka", 1, 177, "opalowy"),
    (null, 1000, "Klient4", "2023-12-11","koszula", 1, 178, "różowy"),
    (null, 670, "Klient8", "2023-12-11","czapka", 1, 179, "zółty"),
    (null, 420, "Klient6", "2023-12-11","czapka", 1, 180, "zielony"),
    (null, 250, "Klient3", "2023-12-11","spodnie", 2, 181, "niebieski"),
    (null, 520, "Klient4", "2023-12-11","koszula", 2, 182, "fioletowy"),
    (null, 600, "Klient5", "2023-12-11","czapka", 2, 183, "szary"),
    (null, 500, "Klient7", "2023-12-11","spodnia", 5, 184, "czarny"),
    (null, 550, "Klient3", "2023-12-11","garnitur", 10, 185, "biały"),
    (null, 120, "Klient1", "2023-12-11","czapka", 1, 143, "zielony");
    
select * from zamowienia where wzrost > 170 order by wzrost desc;

select distinct przedmiot from zamowienia where przedmiot != "garnitur" order by przedmiot asc;

select * from zamowienia where przedmiot = "garnitur" and wzrost >= 180;

select przedmiot, klient, wzrost from zamowienia where kolor in ("szary", "czarny");

select distinct kolor from zamowienia where kolor not in ("szary", "czarny");

update zamowienia set kolor = "zielony" where id = 4;

select * from zamowienia where kolor is null;

update zamowienia set kolor = null where kolor = "opalowy";

alter table zamowienia add termin int;

alter table zamowienia drop termin;

describe zamowienia;



