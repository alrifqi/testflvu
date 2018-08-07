# Import flask and template operators
from flask import Flask, render_template
import config
from config import ProdConfig
from flask_jwt_extended import JWTManager
from mongokit import Connection, Document
from flask_oauthlib.provider import OAuth2Provider


# Define the WSGI application object
app = Flask(__name__, instance_relative_config=True)

# Configurations
app.config.from_object(ProdConfig)
jwt = JWTManager(app)
connection = Connection(host=config.Config.MONGODB_HOST, port=config.Config.MONGODB_PORT)
oauth = OAuth2Provider(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.modules.api.controllers import mod_api as api_module
from app.modules.auth.controllers import mod_auth as auth_module

# Register blueprint(s)
app.register_blueprint(api_module)
app.register_blueprint(auth_module)
