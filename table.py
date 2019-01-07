from dbInit import db
import json
import os


class Singer(db.Model):
    __tablename__ = 'singer'
    id = db.Column(db.Integer,  autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    singermid = db.Column(db.String(30), primary_key=True, nullable=False)
    area = db.Column(db.Integer, nullable=True)


class Song(db.Model):
    __tablename__ = 'song'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    singer = db.Column(db.String(255), nullable=False)
    songmid = db.Column(db.String(30), nullable=False)
    albummid = db.Column(db.String(30), nullable=False)


class Album(db.Model):
    __tablename__ = 'album'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    albummid = db.Column(db.String(30), nullable=False)
    singermid = db.Column(db.String(30), nullable=False)


class Top(db.Model):
    __tablename__ = 'top'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    area = db.Column(db.String(11), nullable=False)
    songname = db.Column(db.String(255), nullable=False)
    singename = db.Column(db.String(255), nullable=False)


class Area(db.Model):
    __tablename__ = 'area'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    num = db.Column(db.Integer, nullable=False)
    place = db.Column(db.String(30), nullable=False)
