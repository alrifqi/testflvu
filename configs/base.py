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
    JWT_SECRET_KEY = '2cb9fe15e18957192aa0e01e8b2aad8226cf697aa0019acd'

    # Secret key for signing cookies
    SECRET_KEY = "secret"
    MONGODB_HOST = "localhost"
    MONGODB_PORT = 27017

    package_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_dir = os.path.join(package_dir, 'testflvu.db')

    SQLALCHEMY_DATABASE_URI = ''.join(['sqlite:///', db_dir])
    SQLALCHEMY_TRACK_MODIFICATIONS = True