import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SQLALCHEMY_ECHO = True
WTF_CSRF_ENABLED = True
SECRET_KEY = 'secretkey'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'cadoption.db')

SQLALCHEMY_TRACK_MODIFICATIONS = False


