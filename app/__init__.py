# Import flask and template operators
from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from mongokit import Connection
from flask_oauthlib.provider import OAuth2Provider
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
# from app.libs.OauthHandler import default_provider

def create_app(config=None):
    from configs import DevConfig, ProdConfig, Config
    from app.libs.OauthHandler import oauth
    from app.modules.models import db

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(ProdConfig)

    jwt = JWTManager(app)
    connection = Connection(host=Config.MONGODB_HOST, port=Config.MONGODB_PORT)
    db.init_app(app)
    oauth.init_app(app)
    # default_provider(app, oauth)

    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    # Import a module / component using its blueprint handler variable (mod_auth)
    from app.modules.api.controllers import mod_api as api_module
    from app.modules.auth.controllers import mod_auth as auth_module
    from app.modules.oauth.controllers import mod_oauth as oauth_module

    # Register blueprint(s)
    app.register_blueprint(api_module)
    app.register_blueprint(auth_module)
    app.register_blueprint(oauth_module)

    return app, oauth

app, oauth = create_app()


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Define the WSGI application object
# app = Flask(__name__, instance_relative_config=True)

# Configurations
# app.config.from_object(ProdConfig)
# jwt = JWTManager(app)
# connection = Connection(host=Config.MONGODB_HOST, port=Config.MONGODB_PORT)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# manager = Manager(app)
# manager.add_command('db', MigrateCommand)
# oauth = OAuth2Provider(app)

# oauth = default_provider(app)
# Sample HTTP error handling
