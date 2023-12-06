create database if not exists marmaj;

use marmaj;

create table if not exists produkty (
    id int primary key,
    nazwa varchar(255) not null,
    cena float not null,
    stan int default 0
);

alter table
    produkty
modify
    column id int auto_increment;

insert into
    produkty
values
    (null, "krzesło", 100, 20),
    (null, "stół", 200, 50),
    (null, "lampa", 50, 200);

create table klienci (
    id int auto_increment primary key,
    imie varchar(64),
    nazwisko varchar(64),
    pesel varchar(11)
);

alter table
    klienci
add
    constraint pesellen check (length(pesel) = 11);

insert into
    klienci
values
    (null, "Adam", "Mierzeja", "02030467819");

insert into
    klienci
values
    (null, "Agata", "Druza", "12378946783");

create table zakupy (
    id int primary key auto_increment,
    klient_id int,
    produkt_id int,
    foreign key k_id (klient_id) references klienci (id),
    foreign key p_id (produkt_id) references produkty (id)
);

insert into
    zakupy
values
    (null, 1, 3);

insert into
    zakupy
values
    (null, 2, 1);

select
    z.id,
    k.imie,
    p.nazwa
from
    zakupy as z
    left join klienci as k on k.id = z.klient_id
    left join produkty as p on p.id = z.produkt_id;

alter table
    zakupy
add
    column ilosc int not null default 0;

select
    z.id as "ID zakupu",
    k.imie as "Kupujący",
    p.nazwa as "Produkt",
    z.ilosc as "Sztuki"
from
    zakupy as z
    left join klienci as k on k.id = z.klient_id
    left join produkty as p on p.id = z.produkt_id;