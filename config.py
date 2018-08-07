# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = "secret"
    JWT_SECRET_KEY = 'super-secret'

    # Secret key for signing cookies
    SECRET_KEY = "secret"
    MONGODB_HOST = "localhost"
    MONGODB_PORT = 27017

class ProdConfig(Config):
    DEBUG = False

class DevConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True