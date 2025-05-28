from flask_wtf import FlaskForm
from wtforms import DateField, SelectField, StringField, PasswordField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class loginCliente(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Login')
    
class loginProfessional(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Login')

class cadastroProfessional(FlaskForm):
    nome = StringField('Nome',render_kw={'placeholder':'Nome Completo'}, validators=[DataRequired()])
    email = StringField('Email', render_kw={'placeholder':'E-mail'}, validators=[DataRequired(), Email()])
    localidade = StringField('Localidade', render_kw={'placeholder':'Província, Município'}, validators=[DataRequired()])
    service = StringField('Área Especializada', render_kw={'placeholder':'Tipo de serviço a prestar'}, validators=[DataRequired()])
    telefone = IntegerField('Telefone', render_kw={'placeholder':'9xx xxx xxx', 'id':'telefoneProfessional'}, validators=[DataRequired()])
    senha = PasswordField('Senha', render_kw={'placeholder':'Senha'}, validators=[DataRequired()])
    nascimento = DateField('Data de nascimento', render_kw={'placeholder':'Data de Nascimento'}, validators=[DataRequired()])
    submit = SubmitField('Adicionar Produto')


class cadastroCliente(FlaskForm):
    nome = StringField('Nome',render_kw={'placeholder':'Nome Completo'}, validators=[DataRequired()])
    email = StringField('Email', render_kw={'placeholder':'E-mail'}, validators=[DataRequired(), Email()])
    localidade = StringField('Localidade', render_kw={'placeholder':'Província, Município'}, validators=[DataRequired()])
    telefone = IntegerField('Telefone', render_kw={'placeholder':'9xx xxx xxx', 'id':'telefoneCliente'}, validators=[DataRequired()])
    senha = PasswordField('Senha', render_kw={'placeholder':'Senha'}, validators=[DataRequired()])
    nascimento = DateField('Data de nascimento', render_kw={'placeholder':'Data de Nascimento'}, validators=[DataRequired()])
    submit = SubmitField('Adicionar Produto')