from flask_login import UserMixin
from flask_migrate import Migrate
from . import db

class User(UserMixin, db.Model): #Tabel User
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Pasien(UserMixin, db.Model): #Table Mahasiswa
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    nama_depan = db.Column(db.String(50))
    nama_belakang = db.Column(db.String(50))