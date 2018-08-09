from mongokit import Document, DocumentMigration
from app.helpers import Model as ModelHelper
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

# @connection.register
# class User(Document):
#     __collection__ = 'user'
#     __database__ = 'aersure'
#     structure = {
#         'name': unicode,
#         'username': unicode,
#         'email': unicode,
#         'password': unicode,
#         'created_at': datetime.datetime,
#         'updated_at': datetime.datetime
#     }
#     default_values = {'created_at': datetime.datetime.utcnow, 'updated_at': datetime.datetime.utcnow}
#     indexes = [
#         {'fields': 'email', 'unique': True},
#         {'fields': 'username', 'unique': True}
#     ]
#
# @connection.register
# class Client(Document):
#     __collection__ = 'client'
#     __database__ = 'aersure'
#     structure = {
#         'name': unicode,
#         'description': unicode,
#         'user': User,
#         'client_id': unicode,
#         'client_secret': unicode,
#         'is_confidential': bool,
#         '_redirect_uris': unicode,
#         '_default_scopes': unicode,
#         'active': bool,
#         'created_at': datetime.datetime,
#         'updated_at': datetime.datetime
#     }
#     validators = {
#         'name': ModelHelper.max_length(50),
#         'client_id': ModelHelper.max_length(40),
#         'client_secret': ModelHelper.max_length(55)
#     }
#     default_values = {'created_at': datetime.datetime.utcnow, 'updated_at': datetime.datetime.utcnow}
#     # use_dot_notation = True
#     use_autorefs = True
#
# @connection.register
# class Grant(Document):
#     __collection__ = 'grant'
#     __database__ = 'aersure'
#     structure = {
#         'user': User,
#         'client': Client,
#         'code': unicode,
#         'redirect_uri': unicode,
#         'expires': datetime.datetime,
#         '_scopes': unicode,
#         'active': bool
#     }
#     validators = {
#         'code': ModelHelper.max_length(255),
#         'redirect_uri': ModelHelper.max_length(255)
#     }
#     use_autorefs = True
#
# @connection.register
# class Token(Document):
#     __collection__ = 'token'
#     __database__ = 'aersure'
#     structure = {
#         'client': Client,
#         'user': User,
#         'token_type': unicode,
#         'access_token': unicode,
#         'refresh_token': unicode,
#         'expires': datetime.datetime,
#         '_scopes': unicode
#     }
#     use_autorefs = True

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, index=True,
                         nullable=False)
    name = db.Column(db.String(200))
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100))

    def check_password(self, password):
        return True

class Client(db.Model):
    # human readable name, not required
    name = db.Column(db.String(40))

    # human readable description, not required
    description = db.Column(db.String(400))

    # creator of the client, not required
    user_id = db.Column(db.ForeignKey('user.id'))
    # required if you need to support client credential
    user = db.relationship('User')

    client_id = db.Column(db.String(40), primary_key=True)
    client_secret = db.Column(db.String(55), unique=True, index=True,
                              nullable=False)

    # public or confidential
    is_confidential = db.Column(db.Boolean)

    _redirect_uris = db.Column(db.Text)
    _default_scopes = db.Column(db.Text)

    @property
    def client_type(self):
        if self.is_confidential:
            return 'confidential'
        return 'public'

    @property
    def redirect_uris(self):
        if self._redirect_uris:
            return self._redirect_uris.split()
        return []

    @property
    def default_redirect_uri(self):
        return self.redirect_uris[0]

    @property
    def default_scopes(self):
        if self._default_scopes:
            return self._default_scopes.split()
        return []

class Grant(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer, db.ForeignKey('user.id', ondelete='CASCADE')
    )
    user = db.relationship('User')

    client_id = db.Column(
        db.String(40), db.ForeignKey('client.client_id'),
        nullable=False,
    )
    client = db.relationship('Client')

    code = db.Column(db.String(255), index=True, nullable=False)

    redirect_uri = db.Column(db.String(255))
    expires = db.Column(db.DateTime)

    _scopes = db.Column(db.Text)

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self

    @property
    def scopes(self):
        if self._scopes:
            return self._scopes.split()
        return []

class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(
        db.String(40), db.ForeignKey('client.client_id'),
        nullable=False,
    )
    client = db.relationship('Client')

    user_id = db.Column(
        db.Integer, db.ForeignKey('user.id')
    )
    user = db.relationship('User')

    # currently only bearer is supported
    token_type = db.Column(db.String(40))

    access_token = db.Column(db.String(255), unique=True)
    refresh_token = db.Column(db.String(255), unique=True)
    expires = db.Column(db.DateTime)
    _scopes = db.Column(db.Text)

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self

    @property
    def scopes(self):
        if self._scopes:
            return self._scopes.split()
        return []