from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

from projeto import db
from projeto.models import ItensBazar

class Testeform(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    assunto = StringField('Assunto', validators=[DataRequired()])
    mensagem = StringField('Mensagem', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')
    

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
        db.session.commit()