from . import login_manager, db
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  usuario = db.Column(db.String(20), unique=True, nullable=False)
  contrasena = db.Column(db.String(60), nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)