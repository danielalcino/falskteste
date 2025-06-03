
from werkzeug.utils import secure_filename
import os
#

class Config:
    SECRET_KEY = secure_filename(os.urandom(24).hex())
    SQLALCHEMY_DATABASE_URI = os.getenv('MYSQL_URL')  # ou o nome da variável que você criar no Railway
    SQLALCHEMY_TRACK_MODIFICATIONS = False

