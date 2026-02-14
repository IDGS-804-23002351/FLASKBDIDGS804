from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField
from wtforms import EmailField
from wtforms import validators
class UserForm(Form):
    id = IntegerField('id', [validators.NumberRange(min=1, max=100, message='Valor no válido')])
    nombre = StringField('nombre',[validators.DataRequired(message='nombre es requerido'),
                                   validators.Length(min=4, max=20, message='longitud minimo 4, maximo 20')])
    apaterno = StringField('apaterno',[validators.DataRequired(message='apernado es requerido')])
    email = EmailField('email',[validators.DataRequired(message='email es requerido'),
                                validators.email(message='email no valido')])
    