from . import maestros
from flask import render_template,request,redirect,url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
import forms
from maestros.routes import maestros, maestros
from models import db
from models import Alumno, Maestros


@maestros.route("/maestros",methods=['GET','POST'])
@maestros.route("/index")
def index():
    create_form = forms.UserForm(request.form)
    maestros = Maestros.query.all()
    return render_template("maestros/listadoMaes.html",form = create_form, maestros= maestros)

@maestros.route("/Maestro",methods=['GET','POST'])
def Maestro():
    create_form = forms.UserForm(request.form)
    if request.method == 'POST':
        maes = Maestros(
            nombre = create_form.nombre.data,
            apellidos = create_form.apellidos.data,
            especialidad = create_form.especialidad.data,
            email = create_form.email.data
        )
        db.session.add(maes)
        db.session.commit()
        return redirect(url_for('maestros.index'))
    return render_template("maestros/Maestro.html",forms = create_form)
@maestros.route("/detalles",methods=['GET','POST'])
def detalles():
	create_form = forms.UserForm(request.form)
	if request.method == 'GET':
		matricula=request.args.get('id')
		maes1 = db.session.query(Maestros).filter(Maestros.matricula==id).first()
		nombre = maes1.nombre
		apellidos = maes1.apellidos
		especialidad = especialidad.especialidad
		email = maes1.email
	return render_template("maestros/detalles.html",forms=create_form,matricula=id,nombre=nombre,apellidos=apellidos,especialidad=especialidad,email=email)
@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"