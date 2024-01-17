use mm_zajecia2;

drop table zamowienia;

drop table klienci;

create table if not exists klienci (
	id int primary key auto_increment,
    nazwa varchar(50),
    adres varchar(50),
    nip varchar(50)
);

describe klienci;

create table if not exists zamowienia(
	id int primary key auto_increment,
    kwota decimal(10,2),
    data date,
    id_klienta int,
    constraint fk_klient foreign key(id_klienta) references klienci(`id`)
);

describe zamowienia;

insert into klienci values(null, "Adam Pisak", "Sikorskiego 1", "1234567890123456789"),
(null, "Adam Pasak", "Sikorskiego 2", "0234567890123456789"),
(null, "Adam Posak", "Sikorskiego 3", "1224567890123456789"),
(null, "Adam Pusak", "Sikorskiego 4", "1244567890123456789"),
(null, "Adam Pósak", "Sikorskiego 5", "1254567890123456789");

select * from klienci;

insert into zamowienia values (null, 2000, "2023-02-02", 2);
insert into zamowienia values (null, 2000, "2023-02-02", 2),
(null, 1000, "2023-02-02", 3),
(null, 3000, "2023-02-02", 3),
(null, 2213, "2023-02-02", 4),
(null, 432, "2023-02-02", 4),
(null, 34, "2023-02-02", 3),
(null, 23423, "2023-02-02", 2);


select * from zamowienia;

select k.nazwa, z.kwota from zamowienia as z left join klienci as k on k.id = z.id_klienta;

select k.nazwa, z.kwota from zamowienia as z right join klienci as k on k.id = z.id_klienta;

select k.nazwa, z.kwota from zamowienia as z inner join klienci as k on k.id = z.id_klienta;

select k.nazwa, count(z.id) as "liczba zamowien" from zamowienia as z right join klienci as k on k.id = z.id_klienta group by k.id;

