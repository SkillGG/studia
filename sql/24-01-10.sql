create database if not exists mm_zajecia2;
use mm_zajecia2;
create table if not exists pracownicy(
	id int primary key auto_increment,
	imie varchar(50),
	nazwisko varchar(50),
	dzial varchar(50),
	pensja decimal(10,2),
	wzrost int,
	waga int);
describe pracownicy;

insert into pracownicy values (null,"imie 1", "nazw 1", 	"zakupy", 3200.00, 170, 90)
	,(null,"imie 2", "nazw 2", 	"magazyn", 10900.00, 169, 69)
	,(null,"imie 3", "nazw 3", 	"magazyn", 25500.00, 150, 80)
	,(null,"imie 4", "nazw 4", 	"sprzedaż", 5000.00, 183, 120)
	,(null,"imie 5", "nazw 5", 	"sprzedaż", 4700.00, 159, 100)
	,(null,"imie 6", "nazw 6", 	"zakupy", 3200.00, 180, 100)
	,(null,"imie 7", "nazw 7", 	"magazyn", 27800.00, 139, 180)
	,(null,"imie 8", "nazw 8", 	"magazyn", 9000.00, 189, 92)
	,(null,"imie 9", "nazw 9", 	"sprzedaż", 4500.00, 176, 67)
	,(null,"imie 10", "nazw 10", "zakupy", 7800.00, 200, 100)
	,(null,"imie 11", "nazw 11", "magazyn", 17000.00, 165, 90)
	,(null,"imie 12", "nazw 12", "zakupy", 59300.00, 172, 90)
	,(null,"imie 13", "nazw 13", "zakupy", 6100.00, 136, 90)
	,(null,"imie 14", "nazw 14", "sprzedaż", 6700.00, 212, 90)
	,(null,"imie 15", "nazw 15", "zakupy", 7120.00, 176, 90)
	,(null,"imie 16", "nazw 16", "magazyn", 7400.00, 176, 90);
    
select * from pracownicy;

drop table knigi;

create table knigi(
	id int auto_increment,
    title varchar(300) not null,
    author varchar(100) not null,
    format varchar(50) default 'hardcover',
    pages int,
    primary key (id), 
    constraint pages_more_than_one check (`pages` > 0) );
    
describe knigi;

insert into knigi (title, author, pages) values ("tyt abc", "aut01", 100);

insert into knigi (title, author, pages) values ("tyt abc", "aut01", -100);

insert into knigi (title, author,format, pages) values ("tyt abc", "aut01","paperback", 100);

select * from knigi;