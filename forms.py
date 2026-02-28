from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField
from wtforms import EmailField
from wtforms import validators
class UserForm(FlaskForm):
    id = IntegerField('id', [validators.NumberRange(min=1, max=100, message='Valor no válido')])
    nombre = StringField('nombre',[validators.DataRequired(message='nombre es requerido'),
                                   validators.Length(min=4, max=20, message='longitud minimo 4, maximo 20')])
    apellidos = StringField('apellidos',[validators.DataRequired(message='apernado es requerido')])
    especialidad = StringField('especialidad',[validators.DataRequired(message='especialidad es requerido')])
    email = EmailField('email',[validators.DataRequired(message='email es requerido'),
                                validators.email(message='email no valido')])
    telefono = StringField('telefono',[validators.DataRequired(message='telefono es requerido'),
                                   validators.Length(min=4, max=20, message='longitud minimo 4, maximo 20')])
    
class MaestroForm(FlaskForm):
    matricula = IntegerField('matricula', [validators.NumberRange(min=1, max=100, message='Valor no válido')])
    nombre = StringField('nombre',[validators.DataRequired(message='nombre es requerido'),
                                   validators.Length(min=4, max=20, message='longitud minimo 4, maximo 20')])
    apellidos = StringField('apellidos',[validators.DataRequired(message='apernado es requerido')])
    especialidad = StringField('especialidad',[validators.DataRequired(message='especialidad es requerido')])
    email = EmailField('email',[validators.DataRequired(message='email es requerido'),
                                validators.email(message='email no valido')])