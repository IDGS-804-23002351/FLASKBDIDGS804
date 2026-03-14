from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField
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

class CursoForm(FlaskForm):
    id = IntegerField('id', [validators.NumberRange(min=1, max=100, message='Valor no válido')])
    nombre = StringField('nombre',[validators.DataRequired(message='nombre es requerido'),
                                   validators.Length(min=4, max=20, message='longitud minimo 4, maximo 20')])
    descripcion = StringField('descripcion',[validators.DataRequired(message='descripcion es requerido')])
    maestro_id = SelectField('Maestro', coerce=int, choices=[])
    
    def __init__(self, *args, **kwargs):
        super(CursoForm, self).__init__(*args, **kwargs)
        from models import Maestros
        self.maestro_id.choices = [(0, 'Selecciona un maestro')] + [
            (maestro.matricula, f'{maestro.nombre} {maestro.apellidos} - {maestro.especialidad}')
            for maestro in Maestros.query.all()
        ]

class InscripcionesForm(FlaskForm):
    id = IntegerField('id', [validators.NumberRange(min=1, max=100, message='Valor no válido')])
    alumno_id = SelectField('Alumno', coerce=int, choices=[])  
    curso_id = SelectField('Curso', coerce=int, choices=[])
    
    def __init__(self, *args, **kwargs):
        super(InscripcionesForm, self).__init__(*args, **kwargs)
        
        from models import Alumno
        self.alumno_id.choices = [(0, 'Selecciona un alumno')] + [
            (alumno.id, f'{alumno.nombre} {alumno.apellidos}')
            for alumno in Alumno.query.all()
        ]
        from models import Curso
        self.curso_id.choices = [(0, 'Selecciona un curso')] + [
            (curso.id, f'{curso.nombre}')
            for curso in Curso.query.all()
        ]

class ConsultasCursosForm(FlaskForm):
    curso_id = SelectField('Curso', coerce=int, choices=[])
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from models import Curso
        self.curso_id.choices = [(0, 'Selecciona un curso')] + [
            (curso.id, f'{curso.nombre}')
            for curso in Curso.query.all()
        ]

class ConsultasAlumnosForm(FlaskForm):
    alumno_id = SelectField('Alumno', coerce=int, choices=[])  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        from models import Alumno
        self.alumno_id.choices = [(0, 'Selecciona un alumno')] + [
            (alumno.id, f'{alumno.nombre} {alumno.apellidos}')
            for alumno in Alumno.query.all()
        ]