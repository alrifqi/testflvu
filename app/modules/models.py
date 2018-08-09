from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import Enum


db = SQLAlchemy()

class GenderEnum(Enum):
    m = 'Man'
    w = 'Woman'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    name = db.Column(db.String(200))
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    handphone = db.Column(db.String(25), nullable=False, unique=True)
    address = db.Column(db.Text, nullable=True)
    gender = db.Column(db.String(1), nullable=True, default='n')
    photo = db.Column(db.String(255), nullable=True)