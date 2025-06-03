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
#muitas alterações
app = Flask(__name__)

# Geração de chave secreta aleatória para segurança
app.config['SECRET_KEY'] = os.urandom(24)
app.config.from_object(Config)
csrf = CSRFProtect(app)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dash.html')

@app.route("/verificar_professionals")
def verificar_professionals():
    profissionais = Professional.query.all()
    return "<br>".join([f"{p.nome} - {p.email}" for p in profissionais]) or "Nenhum profissional encontrado."


@app.route('/addProfessional', methods=['POST'])
def addProfessional():
    # Receber dados diretamente do `FormData`, não via `form`
    nome = request.form.get('nome')
    email = request.form.get('email')
    telefone = request.form.get('telefone')
    nascimento = request.form.get('nascimento')
    localidade = request.form.get('localidade')
    especialidade = request.form.get('especialidade')
    senha = request.form.get('senha')

    existente = Professional.query.filter_by(email=email).first()
    if existente:
        return jsonify({'success': False, 'message': 'E-mail já cadastrado!'})

    try:
        novo_profissional = Professional(
            nome=nome,
            email=email,
            telefone=telefone,
            nascimento=datetime.strptime(nascimento, "%Y-%m-%d"),
            localidade=localidade,
            especialidade=especialidade,
            senha=generate_password_hash(senha)
        )

        db.session.add(novo_profissional)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Cadastro realizado com sucesso!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': 'Erro ao cadastrar profissional.'})

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

    # Só renderiza a página se for acesso via GET
    return render_template('addCliente.html', form=form)


#start app bbbgf
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
