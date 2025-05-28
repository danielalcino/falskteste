from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from config import Config
from models import Professional, Cliente
from forms import cadastroProfessional, cadastroCliente
from datetime import datetime
import os
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()
app = Flask(__name__)

# Geração de chave secreta aleatória para segurança
app.config['SECRET_KEY'] = os.urandom(24)
app.config.from_object(Config)

db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def dashboard():
    return render_template('dash.html')

@app.route('/addProfessional', methods=['GET', 'POST'])
def addProfessional():
    form = cadastroProfessional()

    if form.validate_on_submit():
        professional_existente = Professional.query.filter_by(email=form.email.data).first()
        
        if professional_existente :
            flash('Este email já foi registrado')
        else:
            nome_professional = form.nome.data
            email_professional = form.email.data
            services = form.service.data
            telefone_professional = form.telefone.data
            senha_professional = form.senha.data
            localidade_professional = form.localidade.data
            data_professional = form.nascimento.data
            
            # Verificar se o produto existe e se a quantidade no estoque é suficiente
            
            cadastrarProfessional = cadastroProfessional(
                nome=nome_professional,
                email=email_professional,
                localidade=localidade_professional,
                nascimento=data_professional,
                telefone=telefone_professional,
                especialidade=services,
                senha=senha_professional,
            )

            db.session.add(cadastrarProfessional)
            db.session.commit()
            flash('Cadstro realizado com sucesso!', 'success') 
            return redirect(url_for('addProfessional'))

    return render_template('addProfessional.html', form=form)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8080)
