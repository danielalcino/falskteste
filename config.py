
import os
from werkzeug.utils import secure_filename
#
class Config:
    SECRET_KEY = secure_filename(os.urandom(24).hex())
    # Troque os valores abaixo pelos dados reais do Railway ou Render
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:cWjRToxNDJyuNosnQkqNRLkKLzqVVLhO@maglev.proxy.rlwy.net:40818/railway'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
