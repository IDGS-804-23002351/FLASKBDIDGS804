from flask import Flask, render_template, request,redirect,url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask_migrate import Migrate
from flask import g
import forms
from models import db
from models import Alumno
from maestros.routes import maestros
from cursos.routes import cursos
from alumnos.routes import alumnos
from consultas.routes import consultas
from inscripciones.routes import inscripciones


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(maestros)
app.register_blueprint(cursos)
app.register_blueprint(consultas)
app.register_blueprint(alumnos)
app.register_blueprint(inscripciones)

app.secret_key='clave_secreta'
csrf = CSRFProtect(app) 
db.init_app(app)
migrate = Migrate(app,db)
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route("/", methods=['GET', 'POST'])
def index():
	return render_template("index.html")
if __name__ == '__main__':
    app.run(debug=True)