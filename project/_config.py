# configuration file

import os

# grab folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = "flasktasker.db"
USERNAME = "admin"
PASSWORD = "admin"
WTF_CSRF_ENABLED = True  # for cross-site request forgery prevention
SECRET_KEY = "my_precious"  # this should be generated by random key gen.

# define full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)