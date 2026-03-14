from . import consultas  
from flask import render_template, request, redirect, url_for, flash
import forms
from models import db
from models import Alumno, Maestros, Curso 

@consultas.route("/consultas", methods=['GET','POST'])
@consultas.route("/consultaCursos", methods=['GET', 'POST'])
def consultaCursos():
    create_form = forms.ConsultasCursosForm(request.form)
    alumnos_filtrados = [] 
    
    if request.method == 'POST':
        id_curso_seleccionado = create_form.curso_id.data
        
        if id_curso_seleccionado and id_curso_seleccionado != 0:
            curso_objeto = Curso.query.get(id_curso_seleccionado)
            
            if curso_objeto:
                alumnos_filtrados = curso_objeto.alumnos

    return render_template("consultas/consultaCursos.html",forms=create_form,alumnos=alumnos_filtrados)

@consultas.route("/consultaAlumnos", methods=['GET', 'POST'])
def consultaAlumnos():
    create_form = forms.ConsultasAlumnosForm(request.form)
    alumnos_filtrados = [] 
    
    if request.method == 'POST':
        id_alumno_seleccionado = create_form.alumno_id.data
        
        if id_alumno_seleccionado and id_alumno_seleccionado != 0:
            alumno_objeto = Alumno.query.get(id_alumno_seleccionado)
            
            if alumno_objeto:
                alumnos_filtrados = alumno_objeto.cursos

    return render_template("consultas/consultaAlumnos.html",forms=create_form,cursos=alumnos_filtrados)