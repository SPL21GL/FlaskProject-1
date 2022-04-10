create database if not exists Sportverein;
use Sportverein;

create table if not exists Radrennen
(
	RadrennenID int auto_increment unique key primary key,
    Land text,
    Titel varchar(64),
    Datum date,
    LaengeInKm int
);

create table if not exists Hauptsponsor
(
    SponsorID int auto_increment unique key primary key,
    Name varchar(64),
    Sponsorbetrag int,
    Werbungsart text,
    Land varchar(64)
);

create table if not exists Sportler
(
    SportlerID int auto_increment unique key primary key,
    Land varchar(64),
    Vorname varchar(64),
    Nachname varchar(64),
    Radmarke varchar(128)
);

create table if not exists Sportler_Radrennen
(
    Sportler_Radrennen_ID int auto_increment unique key primary key,
    SportlerID int,
    RadrennenID int,
    Best_Zeit timestamp
);

alter table Sportler_Radrennen add constraint SportlerID foreign key (SportlerID) references Sportler(SportlerID);
alter table Sportler_Radrennen add constraint RadrennenID foreign key (RadrennenID) references Radrennen(RadrennenID);
