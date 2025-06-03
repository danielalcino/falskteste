
import os
from werkzeug.utils import secure_filename

class Config:
    SECRET_KEY = secure_filename(os.urandom(24).hex())
    # Troque os valores abaixo pelos dados reais do Railway ou Render
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://USUARIO:SENHA@HOST:PORTA/NOME_DO_BANCO'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
