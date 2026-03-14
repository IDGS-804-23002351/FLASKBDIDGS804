from . import inscripciones
from flask import render_template,request,redirect,url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
import forms
from inscripciones.routes import inscripciones, inscripciones
from models import db
from models import Alumno, Maestros, Curso,Inscripcion


@inscripciones.route("/inscripciones",methods=['GET','POST'])
@inscripciones.route("/Inscripciones")
def indexInscripciones():
    create_form = forms.InscripcionesForm(request.form)
    lista_inscripciones = Inscripcion.query.all()
    alumnos = Alumno.query.all() 
    cursos = Curso.query.all()    
    return render_template("inscripciones/listadoInscripciones.html", 
                         form=create_form, 
                         inscripciones=lista_inscripciones,
                         alumnos=alumnos,   
                         cursos=cursos)       
@inscripciones.route("/agregar_Inscripciones", methods=['GET','POST'])
def agregar_Inscripciones():
    create_form = forms.InscripcionesForm(request.form)
    if request.method == 'POST':
        nuevo_inscripcion = Inscripcion(
            alumno=create_form.alumno_id.data,
            curso_id=create_form.curso_id.data
        )
        db.session.add(nuevo_inscripcion)
        db.session.commit()
        return redirect(url_for('inscripciones.indexInscripciones'))
    return render_template("inscripciones/agregar_Inscripciones.html", forms=create_form)

@inscripciones.route("/modificarInscripciones",methods=['GET','POST'])
def modificarInscripciones():
	create_form = forms.InscripcionesForm(request.form)
	if request.method == 'GET':
		id=request.args.get('id')
		inc1 = db.session.query(Inscripcion).filter(Inscripcion.id==id).first()
		create_form.id.data = request.args.get('id')
		create_form.alumno_id.data = inc1.alumno
		create_form.curso_id.data = inc1.curso_id
	if request.method == 'POST':
		id=request.args.get('id')
		inc1 = db.session.query(Inscripcion).filter(Inscripcion.id==id).first()
		inc1.id = id
		inc1.alumno = create_form.alumno_id.data
		inc1.curso_id = create_form.curso_id.data
		db.session.add(inc1)
		db.session.commit()
		return redirect(url_for('inscripciones.indexInscripciones'))
	return render_template("inscripciones/modificarInscripciones.html",forms=create_form)

@inscripciones.route("/eliminarInscripciones",methods=['GET','POST'])
def eliminarInscripciones():
	create_form = forms.InscripcionesForm(request.form)
	if request.method == 'GET':
		id=request.args.get('id')
		inscr1 = db.session.query(Inscripcion).filter(Inscripcion.id==id).first()
		create_form.id.data = request.args.get('id')
		create_form.alumno_id.data = inscr1.alumno
		create_form.curso_id.data = inscr1.curso_id
	if request.method == 'POST':
		id=create_form.id.data
		inscr = Inscripcion.query.get(id)
		db.session.delete(inscr)
		db.session.commit()
		return redirect(url_for('inscripciones.indexInscripciones'))
	return render_template("inscripciones/eliminarInscripciones.html",forms=create_form)

@inscripciones.route("/detallesInscripciones", methods=['GET','POST'])
def detallesCursos():
    create_form = forms.InscripcionesForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        inscr1 = db.session.query(Inscripcion).filter(Inscripcion.id == id).first()
        
        if inscr1:
            alumno = db.session.query(Alumno).filter(Alumno.id == inscr1.alumno).first()
            cursos = db.session.query(Curso).filter(Curso.id == inscr1.curso_id).first()
            alumnoNombre = f"{alumno.nombre} {alumno.apellidos}" if alumno else "No asignado"
            cursoNombre = f"{cursos.nombre}" if cursos else "No asignado"
            fecha = inscr1.fecha_inscripcion
            return render_template("inscripciones/detallesInscripciones.html",forms=create_form,id=id,alumnoNombre=alumnoNombre, cursoNombre=cursoNombre,fecha=fecha)
    
    return redirect(url_for('inscripciones.indexInscripciones'))
@inscripciones.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Inscripcioes de {nombre}"