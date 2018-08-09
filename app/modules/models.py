import re
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import Enum
from sqlalchemy.orm import validates
from werkzeug.security import generate_password_hash


db = SQLAlchemy()

class GenderEnum(Enum):
    m = 'Male'
    f = 'Female'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    name = db.Column(db.String(200))
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    handphone = db.Column(db.String(25), nullable=False, unique=True)
    address = db.Column(db.Text, nullable=True)
    gender = db.Column(db.String(1), nullable=True, default='m')
    photo = db.Column(db.String(255), nullable=True)

    # def set_password(self, password):
    #     self.password = generate_password_hash(password)

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise AssertionError("No Name provided")

        return name

    @validates('username')
    def validate_username(self, key, username):
        if not username or username == '':
            raise AssertionError("No Username provided")

        if User.query.filter(User.username == username).first():
            raise AssertionError("Username number is already in use")

        return username

    @validates("handphone")
    def validate_handphone(self, key, handphone):
        if not handphone or handphone == '':
            raise AssertionError("No Handphone provided")

        if User.query.filter(User.handphone == handphone).first():
            raise AssertionError("Handphone number is already in use")

        return handphone

    @validates('email')
    def validata_email(self, key, email):
        if not email:
            raise AssertionError("No Email Provided")
        if User.query.filter(User.email == email).first():
            raise AssertionError("Email is already in use")

        if not re.match("[^@]+@[^@]+\.[^@]+", email):
            raise AssertionError('Provided email is not an email address')

        return email

    @validates('password')
    def validate_password(self, key, password):
        if not password or password == '':
            raise AssertionError('No Password provided')

        if len(password) < 8:
            raise AssertionError("Password length less than 8")

        passcheck = bool(re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])', password))
        if not passcheck:
            raise AssertionError("Password must contain letters and number")

        return generate_password_hash(password)