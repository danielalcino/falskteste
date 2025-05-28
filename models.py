from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Professional(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    localidade = db.Column(db.String(200), nullable=False)
    nascimento = db.Column(db.DateTime)
    telefone = db.Column(db.Integer, nullable=False)
    especialidade = db.Column(db.String(300), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    fotoPerfil = db.Column(db.LargeBinary, nullable=True)

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    localidade = db.Column(db.String(200), nullable=False)
    telefone = db.Column(db.Integer, nullable=False)
    nascimento = db.Column(db.DateTime)
    senha = db.Column(db.String(200), nullable=False)
    fotoPerfil = db.Column(db.LargeBinary, nullable=True)
    