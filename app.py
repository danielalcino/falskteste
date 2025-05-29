from flask import Flask, jsonify, request, render_template, redirect, url_for, request, flash
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
    
    if request.method == 'POST':
        if form.validate_on_submit():
            email_professional = form.email.data
            existente = Professional.query.filter_by(email=email_professional).first()
            
            if existente:            
                return redirect(url_for('addProfessional'))
            
            else:
                try:
                    # Cria o novo registro
                    novo_profissional = Professional(
                        nome=form.nome.data,
                        email=form.email.data,
                        localidade=form.localidade.data,
                        nascimento=form.nascimento.data,
                        telefone=form.telefone.data,
                        especialidade=form.service.data,
                        senha=generate_password_hash(form.senha.data),
                    )

                    # Adiciona no banco de dados
                    db.session.add(novo_profissional)
                    db.session.commit()
                    return jsonify({'success': True, 'message': 'Cadastro realizado com sucesso!'})
                
                except Exception as e:
                    db.session.rollback()
                    return jsonify({'success': False, 'message': 'Erro ao cadastrar cliente.'})
                
        else:
            return jsonify({'success': False, 'message': 'Dados inválidos. Verifique os campos.'})

    return render_template('addProfessional.html', form=form)

@app.route('/addCliente', methods=['GET', 'POST'])
def addCliente():
    form = cadastroCliente()

    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                novo_cliente = Cliente(
                    nome=form.nome.data,
                    email=form.email.data,
                    localidade=form.localidade.data,
                    telefone=form.telefone.data,
                    senha=generate_password_hash(form.senha.data),
                    nascimento=form.nascimento.data,
                )
                db.session.add(novo_cliente)
                db.session.commit()
                return jsonify({'success': True, 'message': 'Cadastro realizado com sucesso!'})
            except Exception as e:
                db.session.rollback()
                return jsonify({'success': False, 'message': 'Erro ao cadastrar cliente.'})
        else:
            return jsonify({'success': False, 'message': 'Dados inválidos. Verifique os campos.'})

    return render_template('addCliente.html', form=form)


#start app bbbgf
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
