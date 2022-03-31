# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Hauptsponsor(db.Model):
    __tablename__ = 'hauptsponsor'

    SponsorID = db.Column(db.Integer, primary_key=True, unique=True)
    Name = db.Column(db.String(64))
    Sponsorbetrag = db.Column(db.Integer)
    Werbungsart = db.Column(db.Text)
    Land = db.Column(db.String(64))


class Radrennen(db.Model):
    __tablename__ = 'radrennen'

    RennenID = db.Column(db.Integer, primary_key=True, unique=True)
    Land = db.Column(db.Text)
    Titel = db.Column(db.String(64))
    Datum = db.Column(db.Date)
    LaengeInKM = db.Column(db.Integer)


class Sportler(db.Model):
    __tablename__ = 'sportler'

    SportlerID = db.Column(db.Integer, primary_key=True, unique=True)
    Land = db.Column(db.String(64))
    Vorname = db.Column(db.String(64))
    Nachname = db.Column(db.String(64))
    Radmarke = db.Column(db.String(128))


class SportlerRadrennen(db.Model):
    __tablename__ = 'sportler_radrennen'

    Sportler_Radrennen_ID = db.Column(
        db.Integer, primary_key=True, unique=True)
    SportlerID = db.Column(db.ForeignKey('sportler.SportlerID'), index=True)
    RennenID = db.Column(db.ForeignKey('radrennen.RennenID'), index=True)
    Best_Zeit = db.Column(db.DateTime)

    radrennen = db.relationship(
        'Radrennen', primaryjoin='SportlerRadrennen.RennenID == Radrennen.RennenID', backref='sportler_radrennens')
    sportler = db.relationship(
        'Sportler', primaryjoin='SportlerRadrennen.SportlerID == Sportler.SportlerID', backref='sportler_radrennens')
