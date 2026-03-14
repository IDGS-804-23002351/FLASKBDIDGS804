from . import cursos  
from flask import render_template, request, redirect, url_for, flash
import forms
from models import db
from models import Alumno, Maestros, Curso 

@cursos.route("/cursos", methods=['GET','POST'])
@cursos.route("/cusos")
def indexCursos():
    create_form = forms.CursoForm(request.form)
    lista_cursos = Curso.query.all()
    return render_template("cursos/listadoCursos.html", 
                         form=create_form, 
                         cursos=lista_cursos)

@cursos.route("/agregar_curso", methods=['GET','POST'])
def agregar_curso():
    create_form = forms.CursoForm(request.form)
    if request.method == 'POST':
        nuevo_curso = Curso(
            nombre=create_form.nombre.data,
            descripcion=create_form.descripcion.data,
            maestro_id=create_form.maestro_id.data
        )
        db.session.add(nuevo_curso)
        db.session.commit()
        return redirect(url_for('cursos.indexCursos'))
    return render_template("cursos/agregar_curso.html", forms=create_form)

@cursos.route("/detallesCursos", methods=['GET','POST'])
def detallesCursos():
    create_form = forms.CursoForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        curso1 = db.session.query(Curso).filter(Curso.id == id).first()
        
        if curso1:
            maestro = db.session.query(Maestros).filter(Maestros.matricula == curso1.maestro_id).first()
            nombre = curso1.nombre
            descripcion = curso1.descripcion
            maestro_id = f"{maestro.nombre} {maestro.apellidos}" if maestro else "No asignado"
            
            return render_template("cursos/detallesCursos.html",forms=create_form,id=id,nombre=nombre, descripcion=descripcion,maestro_id=maestro_id)
    
    return redirect(url_for('cursos.indexCursos'))

@cursos.route("/modificarCurso",methods=['GET','POST'])
def modificarCurso():
	create_form = forms.CursoForm(request.form)
	if request.method == 'GET':
		id=request.args.get('id')
		curso1 = db.session.query(Curso).filter(Curso.id==id).first()
		create_form.id.data = request.args.get('id')
		create_form.nombre.data = curso1.nombre
		create_form.descripcion.data = curso1.descripcion
		create_form.maestro_id.data = curso1.maestro_id
	if request.method == 'POST':
		id=request.args.get('id')
		curso1 = db.session.query(Curso).filter(Curso.id==id).first()
		curso1.id = id
		curso1.nombre = create_form.nombre.data
		curso1.descripcion = create_form.descripcion.data
		curso1.maestro_id = create_form.maestro_id.data
		db.session.add(curso1)
		db.session.commit()
		return redirect(url_for('cursos.indexCursos'))
	return render_template("cursos/modificarCurso.html",forms=create_form)

@cursos.route("/eliminarCursos",methods=['GET','POST'])
def eliminarCursos():
	create_form = forms.CursoForm(request.form)
	if request.method == 'GET':
		id=request.args.get('id')
		curso1 = db.session.query(Curso).filter(Curso.id==id).first()
		create_form.id.data = request.args.get('id')
		create_form.nombre.data = curso1.nombre
		create_form.descripcion.data = curso1.descripcion
		create_form.maestro_id.data = curso1.maestro_id
	if request.method == 'POST':
		id=create_form.id.data
		curs = Curso.query.get(id)
		db.session.delete(curs)
		db.session.commit()
		return redirect(url_for('cursos.indexCursos'))
	return render_template("cursos/eliminarCursos.html",forms=create_form)

@cursos.route('/cursos/perfil/<nombre>')
def perfil(nombre):
    return f"Cursos de {nombre}"