from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

from projeto import db
<<<<<<< HEAD
from projeto.models import ItensBazar

class Testeform(FlaskForm):
=======
from projeto.models import Teste

class TesteForm(FlaskForm):
>>>>>>> 2438c21e811e21400253cca18e66d2ab1b5165e3
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    assunto = StringField('Assunto', validators=[DataRequired()])
    mensagem = StringField('Mensagem', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')
<<<<<<< HEAD
    

class ItensBazarform(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    tamanho = StringField('Tamanho', validators=[DataRequired()])
    tipo = StringField('Tipo', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')   
    
    def save(self):
        itensBazar = ItensBazar(
            nome = self.nome.data,
            tamanho = self.tamanho.data,
            tipo = self.tipo.data
        )
        
        db.session.add(itensBazar)
=======

    def save(self):
        teste = Teste(
            nome = self.nome.data,
            email = self.email.data,
            assunto = self.assunto.data,
            mensagem = self.mensagem.data
        )

        db.session.add(teste)
>>>>>>> 2438c21e811e21400253cca18e66d2ab1b5165e3
        db.session.commit()