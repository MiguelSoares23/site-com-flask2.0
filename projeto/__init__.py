from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'AS5DFTYU4JKM4RF65TGB-FEW3267UI4RFKVM'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from projeto.views import homepage
from projeto.models import Teste