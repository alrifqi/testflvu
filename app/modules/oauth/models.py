from mongokit import Document, DocumentMigration
from app.helpers import Model as ModelHelper
from app import connection
import datetime

@connection.register
class User(Document):
    __collection__ = 'user'
    __database__ = 'aersure'
    structure = {
        'name': unicode,
        'username': unicode,
        'email': unicode,
        'password': unicode,
        'created_at': datetime.datetime,
        'updated_at': datetime.datetime
    }
    default_values = {'created_at': datetime.datetime.utcnow, 'updated_at': datetime.datetime.utcnow}
    indexes = [
        {'fields': 'email', 'unique': True},
        {'fields': 'username', 'unique': True}
    ]

@connection.register
class Client(Document):
    __collection__ = 'client'
    __database__ = 'aersure'
    structure = {
        'name': unicode,
        'description': unicode,
        'user': User,
        'client_id': unicode,
        'client_secret': unicode,
        'is_confidential': bool,
        '_redirect_uris': unicode,
        '_default_scopes': unicode,
        'active': bool,
        'created_at': datetime.datetime,
        'updated_at': datetime.datetime
    }
    validators = {
        'name': ModelHelper.max_length(50),
        'client_id': ModelHelper.max_length(40),
        'client_secret': ModelHelper.max_length(55)
    }
    default_values = {'created_at': datetime.datetime.utcnow, 'updated_at': datetime.datetime.utcnow}
    # use_dot_notation = True
    use_autorefs = True

@connection.register
class Grant(Document):
    __collection__ = 'grant'
    __database__ = 'aersure'
    structure = {
        'user': User,
        'client': Client,
        'code': unicode,
        'redirect_uri': unicode,
        'expires': datetime.datetime,
        '_scopes': unicode,
        'active': bool
    }
    validators = {
        'code': ModelHelper.max_length(255),
        'redirect_uri': ModelHelper.max_length(255)
    }
    use_autorefs = True

@connection.register
class Token(Document):
    __collection__ = 'token'
    __database__ = 'aersure'
    structure = {
        'client': Client,
        'user': User,
        'token_type': unicode,
        'access_token': unicode,
        'refresh_token': unicode,
        'expires': datetime.datetime,
        '_scopes': unicode
    }
    use_autorefs = True