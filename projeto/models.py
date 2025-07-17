from projeto import db
from datetime import datetime

class Teste(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_envio = db.Column(db.DateTime, default=datetime.utcnow())
    nome = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    assunto = db.Column(db.String, nullable=True)
    mensagem = db.Column(db.String, nullable=True)
    

class ItensBazar(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    tamanho = db.Column(db.String(50), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)