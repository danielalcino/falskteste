from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from config import Config
from models import db, Professional, Cliente
from forms import cadastroProfessional, cadastroCliente
from datetime import datetime
import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

# Geração de chave secreta aleatória para segurança
app.config['SECRET_KEY'] = os.urandom(24)
app.config.from_object(Config)
csrf = CSRFProtect(app)

db.init_app(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dash.html')

@app.route('/addProfessional', methods=['GET', 'POST'])
def addProfessional():
    form = cadastroProfessional()
    print("Método:", request.method)
    print("Validou?", form.validate_on_submit())
    print("Erros:", form.errors)
    if form.validate_on_submit():
        # Captura os dados
        nome_professional = form.nome.data
        email_professional = form.email.data
        services = form.service.data
        telefone_professional = form.telefone.data
        senha_professional = generate_password_hash(form.senha.data)
        localidade_professional = form.localidade.data
        data_professional = form.nascimento.data

        # Verifica se o email já existe
        existente = Professional.query.filter_by(email=email_professional).first()
        if existente:
            
            return redirect(url_for('addProfessional'))
        else:
            # Cria o novo registro
            novo_profissional = Professional(
                nome=nome_professional,
                email=email_professional,
                localidade=localidade_professional,
                nascimento=data_professional,
                telefone=telefone_professional,
                especialidade=services,
                senha=senha_professional,
            )

            # Adiciona no banco de dados
            db.session.add(novo_profissional)
            db.session.commit()
            return redirect(url_for('addProfessional'))  # Evita duplicações com o PRG

    return render_template('addProfessional.html', form=form)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
