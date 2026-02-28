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
    create_form = forms.MaestroForm(request.form)
    maestros = Maestros.query.all()
    return render_template("maestros/listadoMaes.html",form = create_form, maestros= maestros)

@maestros.route("/Maestro",methods=['GET','POST'])
def Maestro():
    create_form = forms.MaestroForm(request.form)
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
	create_form = forms.MaestroForm(request.form)
	if request.method == 'GET':
		matricula=request.args.get('id')
		maes1 = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		nombre = maes1.nombre
		apellidos = maes1.apellidos
		especialidad = maes1.especialidad
		email = maes1.email
	return render_template("maestros/detalles.html",forms=create_form,matricula=matricula,nombre=nombre,apellidos=apellidos,especialidad=especialidad,email=email)
@maestros.route("/modificar",methods=['GET','POST'])
def modificar():
	create_form = forms.MaestroForm(request.form)
	if request.method == 'GET':
		matricula=request.args.get('id')
		maes1 = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		create_form.matricula.data = request.args.get('id')
		create_form.nombre.data = maes1.nombre
		create_form.apellidos.data = maes1.apellidos
		create_form.especialidad.data = maes1.especialidad
		create_form.email.data = maes1.email
	if request.method == 'POST':
		matricula=request.args.get('id')
		maes1 = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		maes1.matricula = matricula
		maes1.nombre = create_form.nombre.data
		maes1.apellidos = create_form.apellidos.data
		maes1.email = create_form.email.data
		maes1.email = create_form.email.data
		db.session.add(maes1)
		db.session.commit()
		return redirect(url_for('maestros.index'))
	return render_template("maestros/modificar.html",forms=create_form)

@maestros.route("/eliminar",methods=['GET','POST'])
def eliminar():
	create_form = forms.MaestroForm(request.form)
	if request.method == 'GET':
		matricula=request.args.get('id')
		alum1 = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		create_form.matricula.data = request.args.get('id')
		create_form.nombre.data = alum1.nombre
		create_form.apellidos.data = alum1.apellidos
		create_form.especialidad.data = alum1.especialidad
		create_form.email.data = alum1.email
	if request.method == 'POST':
		matricula=create_form.matricula.data
		alum = Maestros.query.get(matricula)
		db.session.delete(alum)
		db.session.commit()
		return redirect(url_for('maestros.index'))
	return render_template("maestros/eliminar.html",forms=create_form)

@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"