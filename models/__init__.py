from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'usuario_route.login'

def init_app(app):
  db.init_app(app)
  login_manager.init_app(app)