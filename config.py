import os
from werkzeug.utils import secure_filename

class Config:
    SECRET_KEY = secure_filename(os.urandom(24).hex())
    SQLALCHEMY_DATABASE_URI = 'sqlite:///estoque.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
