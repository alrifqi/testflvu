# Import flask and template operators
from flask import Flask, render_template, url_for
from flask_jwt_extended import JWTManager
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.modules.models import db
from flask_cors import CORS

def create_app(config=None):
    from configs import DevConfig, ProdConfig, Config
    from app.helpers.JWT import jwt

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(ProdConfig)
    CORS(app)

    db.init_app(app)
    db.create_all(app=app)
    jwt.init_app(app)

    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    # Import a module / component using its blueprint handler variable (mod_auth)
    from app.modules.api.controllers import mod_api as api_module
    from app.modules.auth.controllers import mod_auth as auth_module
    from app.modules.frontend.controllers import mod_fe as fe_module

    # Register blueprint(s)
    app.register_blueprint(api_module)
    app.register_blueprint(auth_module)
    app.register_blueprint(fe_module)

    return app, manager, jwt

app, manager, jwt = create_app()


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

