from mongokit import Document
from app.helpers import Model as ModelHelper
from app import connection

# @connection.register
class User(Document):
    structure = {
        'name': unicode,
        'email': unicode
    }
    validators = {
        'name': ModelHelper.max_length(50),
        'email': ModelHelper.max_length(120)
    }
    use_dot_notation = True

    @staticmethod
    def get():
        res = connection.aersure.users.find()
        return res

class Tracking(Document):
    structure = {
        'order_id': str,
        'mawb': int,
        'shipper_name': unicode,
        'shipper_contact': unicode,
        'shipper_address': unicode,
        'cnee_name': unicode,
        'cnee_contact': unicode,
        'cnee_email': unicode,
        'cnee_address': unicode,
        'cnee_city': unicode,
        'cnee_state': unicode,
        'cnee_country': unicode,
        'cnee_postcode': unicode,
        'cn_weight': float,
        'cn_dims': unicode,
        'cn_value': float,
        'cn_cod': float,
        'cn_desc': unicode,
        'cn_qty': int
    }

connection.register([User])