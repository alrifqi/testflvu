from mongokit import Document
from app.helpers import Model as ModelHelper
import datetime

class User(Document):
    structure = {
        'name': unicode,
        'email': unicode,
        'password': unicode,
        'created_at': datetime.datetime,
        'updated_at': datetime.datetime
    }
    validators = {
        'name': ModelHelper.max_length(50),
        'email': ModelHelper.max_length(120)
    }
    default_values = {'created_at': datetime.datetime.utcnow, 'updated_at': datetime.datetime.utcnow }
    use_dot_notation = True