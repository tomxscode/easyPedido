from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'XXXXXX'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from routes.usuario import usuario
app.register_blueprint(usuario)

with app.app_context():
  db.create_all()

if __name__ == '__main__':
  app.run(debug=True)