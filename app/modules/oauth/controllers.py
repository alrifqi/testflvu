from bson.json_util import dumps
from flask import Blueprint

from app.modules.models import User
from app.libs.OauthHandler import oauth

mod_oauth = Blueprint('oauth', __name__, url_prefix='/oauth', template_folder='templates')

@mod_oauth.route('/sample')
def sample():
    results = User.get()
    res = dumps(results)
    return res, 200

# @mod_oauth.route('/insert', methods=['GET'])
# def insert():
#     user = conn.User()
#     user['name'] = unicode('reza')
#     user['username'] = unicode('admin')
#     user['email'] = unicode('reza.nurrifqi@aersure.com')
#     user['password'] = unicode('test')
#     user.save()
#
#     client = conn.Client()
#     client['name'] = unicode('confidential')
#     client['client_id'] = unicode('confidential')
#     client['client_secret'] = unicode('confidential')
#     # client['client_type'] = unicode('confidential')
#     client['_redirect_uris'] = unicode('http://localhost:8080/authorized')
#     client['user'] = user
#     client.save()
#
#     access_token = conn.Token()
#     access_token['user'] = user
#     access_token['client'] = client
#     access_token.save()
#     return 'success', 200

@mod_oauth.route('/token')
@oauth.token_handler
def access_token():
    return None

@mod_oauth.route('/authorize')
@oauth.authorize_handler
def authorize_handler():
    return None

# def default_provider(app):
#     oauth = OAuth2Provider(app)
#     @oauth.clientgetter
#     def get_client(client_id):
#         return conn.Client.one()
#
#     @oauth.clientgetter
#     def get_grant(client_id, code):
#         grant = conn.Grant.find_one({'client_id': client_id, 'code': code})
#         return grant
#
#     @oauth.tokengetter
#     def get_token(access_token=None, refresh_token=None):
#         if access_token:
#             return conn.Token.find_one({'access_token': access_token})
#         if refresh_token:
#             return conn.Token.find_one({'refresh_token': refresh_token})
#
#     @oauth.grantsetter
#     def set_grant(client_id, code, request, *args, **kwargs):
#         expires = datetime.utcnow() + timedelta(seconds=100)
#         grant = conn.Grant()
#         grant['client_id'] = client_id
#         grant['code'] = code
#         grant['redirect_uri'] = request.redirect_uri
#         grant['scope'] = ''.join(request.scopes)
#         grant['user_id'] = g.user.id
#         grant.save()
#
#     @oauth.tokensetter
#     def set_token(token, request, *args, **kwargs):
#         tok = conn.Token.find_one({'access_token': token})
#         tok['user_id'] = request.user.id
#         tok['client_id'] = request.client.client_id
#         tok.save()
#
#     @oauth.usergetter
#     def get_user(username, password, *args, **kwargs):
#         return conn.User.find_one({'username': username})
#
#     return oauth
