from . import alumnos  
from flask import render_template, request, redirect, url_for, flash
import forms
from models import db
from models import Alumno, Maestros, Curso 

@alumnos.route("/alumnos", methods=['GET','POST'])
@alumnos.route("/Alumnos")
def indexAlumnos():
	create_form = forms.UserForm(request.form)
	#tem = Alumno.query('SELECT * FROM alumnos')
	alumno = Alumno.query.all()
	return render_template("alumnos/listadoAlumnos.html",form=create_form,alumno=alumno)

@alumnos.route("/agregar_alumno",methods=['GET','POST'])
def Alumnos():
	create_form = forms.UserForm(request.form)
	if request.method == 'POST':
		alum = Alumno(nombre=create_form.nombre.data,
						apellidos=create_form.apellidos.data,
						email=create_form.email.data,
						telefono=create_form.telefono.data)
		db.session.add(alum)
		db.session.commit()
		return redirect(url_for('alumnos.indexAlumnos'))
	return render_template("alumnos/agregar_alumno.html",forms=create_form)

@alumnos.route("/detallesAlumnos",methods=['GET','POST'])
def detallesAlumnos():
	create_form = forms.UserForm(request.form)
	if request.method == 'GET':
		id=request.args.get('id')
		alum1 = db.session.query(Alumno).filter(Alumno.id==id).first()
		nombre = alum1.nombre
		apellidos = alum1.apellidos
		email = alum1.email
		telefono = alum1.telefono
	return render_template("alumnos/detallesAlumnos.html",forms=create_form,id=id,nombre=nombre,apellidos=apellidos,email=email,telefono=telefono)

@alumnos.route("/modificarAlumnos",methods=['GET','POST'])
def modificarAlumnos():
	create_form = forms.UserForm(request.form)
	if request.method == 'GET':
		id=request.args.get('id')
		alum1 = db.session.query(Alumno).filter(Alumno.id==id).first()
		create_form.id.data = request.args.get('id')
		create_form.nombre.data = alum1.nombre
		create_form.apellidos.data = alum1.apellidos
		create_form.email.data = alum1.email
		create_form.telefono.data = alum1.telefono
	if request.method == 'POST':
		id=request.args.get('id')
		alum1 = db.session.query(Alumno).filter(Alumno.id==id).first()
		alum1.id = id
		alum1.nombre = create_form.nombre.data
		alum1.apellidos = create_form.apellidos.data
		alum1.email = create_form.email.data
		alum1.telefono = create_form.telefono.data
		db.session.add(alum1)
		db.session.commit()
		return redirect(url_for('alumnos.indexAlumnos'))
	return render_template("alumnos/modificarAlumnos.html",forms=create_form)

@alumnos.route("/eliminarAlumnos",methods=['GET','POST'])
def eliminarAlumnos():
	create_form = forms.UserForm(request.form)
	if request.method == 'GET':
		id=request.args.get('id')
		alum1 = db.session.query(Alumno).filter(Alumno.id==id).first()
		create_form.id.data = request.args.get('id')
		create_form.nombre.data = alum1.nombre
		create_form.apellidos.data = alum1.apellidos
		create_form.email.data = alum1.email
		create_form.telefono.data = alum1.telefono
	if request.method == 'POST':
		id=create_form.id.data
		alum = Alumno.query.get(id)
		db.session.delete(alum)
		db.session.commit()
		return redirect(url_for('alumnos.indexAlumnos'))
	return render_template("alumnos/eliminarAlumnos.html",forms=create_form)
