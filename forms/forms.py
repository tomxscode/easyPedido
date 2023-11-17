from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, PasswordField, validators, SubmitField, IntegerField
from flask_wtf.file import FileField, FileAllowed
from wtforms import SelectField

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
  
class ProductoMenuForm(FlaskForm):
  nombre = StringField('Nombre', validators=[DataRequired()])
  descripcion = StringField('Descripcion', validators=[DataRequired()])
  precio = IntegerField('Precio', validators=[DataRequired()])
  imagen = FileField('Imagen', validators=[DataRequired(), FileAllowed(['jpg', 'png'], 'Solo se permiten imágenes')])
  categoria = SelectField('Categoria', coerce=str, validators=[DataRequired()])
  submit = SubmitField('Registrar')