
from werkzeug.utils import secure_filename
import os
#

class Config:
    SECRET_KEY = secure_filename(os.urandom(24).hex())
    SQLALCHEMY_DATABASE_URI = os.getenv("MYSQL_URL").replace("mysql://", "mysql+pymysql://")

    SQLALCHEMY_TRACK_MODIFICATIONS = False

