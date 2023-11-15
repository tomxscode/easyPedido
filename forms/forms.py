from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, PasswordField, validators, SubmitField

class RegistroForm(FlaskForm):
  usuario = StringField('Usuario', validators=[DataRequired()])
  contrasena = PasswordField('Contraseña', validators=[DataRequired()])
  confirmar_contrasena = PasswordField('Confirmar contraseña', validators=[DataRequired(), validators.EqualTo('contrasena', message='Las contraseñas deben coincidir')])
  email = StringField('Email', validators=[DataRequired()])
  submit = SubmitField('Registrar')
  
class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired()])
  contrasena = PasswordField('Contraseña', validators=[DataRequired()])
  submit = SubmitField('Iniciar sesión')
  
class CategoriaMenuForm(FlaskForm):
  nombre = StringField('Nombre', validators=[DataRequired()])
  descripcion = StringField('Descripcion', validators=[DataRequired()])
  submit = SubmitField('Registrar')