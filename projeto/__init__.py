from flask import Flask
from flask_sqlalchemy import FlaskSQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)


from projeto.views import homepage