# Import flask and template operators
from flask import Flask, render_template
from configs import DevConfig, ProdConfig, Config
from flask_jwt_extended import JWTManager
from mongokit import Connection, Document
from flask_oauthlib.provider import OAuth2Provider
from datetime import datetime, timedelta


# Define the WSGI application object
app = Flask(__name__, instance_relative_config=True)

# Configurations
app.config.from_object(ProdConfig)
jwt = JWTManager(app)
connection = Connection(host=Config.MONGODB_HOST, port=Config.MONGODB_PORT)
# oauth = OAuth2Provider(app)
def default_provider(app):
    oauth = OAuth2Provider(app)
    @oauth.clientgetter
    def get_client(client_id):
        return connection.Client.one()

    @oauth.clientgetter
    def get_grant(client_id, code):
        grant = connection.Grant.find_one({'client_id': client_id, 'code': code})
        return grant

    @oauth.tokengetter
    def get_token(access_token=None, refresh_token=None):
        if access_token:
            return connection.Token.find_one({'access_token': access_token})
        if refresh_token:
            return connection.Token.find_one({'refresh_token': refresh_token})

    @oauth.grantsetter
    def set_grant(client_id, code, request, *args, **kwargs):
        expires = datetime.utcnow() + timedelta(seconds=100)
        grant = connection.Grant()
        grant['client_id'] = client_id
        grant['code'] = code
        grant['redirect_uri'] = request.redirect_uri
        grant['scope'] = ''.join(request.scopes)
        grant['user_id'] = g.user.id
        grant.save()

    @oauth.tokensetter
    def set_token(token, request, *args, **kwargs):
        tok = connection.Token.find_one({'access_token': token})
        tok['user_id'] = request.user.id
        tok['client_id'] = request.client.client_id
        tok.save()

    @oauth.usergetter
    def get_user(username, password, *args, **kwargs):
        return connection.User.find_one({'username': username})

    return oauth

oauth = default_provider(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.modules.api.controllers import mod_api as api_module
from app.modules.auth.controllers import mod_auth as auth_module
from app.modules.oauth.controllers import mod_oauth as oauth_module

# Register blueprint(s)
app.register_blueprint(api_module)
app.register_blueprint(auth_module)
app.register_blueprint(oauth_module)
