from . import app 
from .models import Medico
from .models import Paciente
from .models import Consultorio
from .models import Cita
from flask import render_template

#crear ruta para ver los medicos 
@app.route("/medicos")
def get_all_medicos():
    medicos = Medico.query.all()
    return render_template("medicos.html", medicos=medicos  )

#crear ruta para ver los pacientes
@app.route("/pacientes")
def get_all_pacientes():
    pacientes = Paciente.query.all()
    return render_template("pacientes.html", pacientes=pacientes  )

#crear ruta para ver los consultorios
@app.route("/consultorio")
def get_all_consultorio():
    consultorio = Consultorio.query.all()
    return render_template("consultorio.html", consultorio=consultorio  )

#crear ruta para ver las citas
@app.route("/cita")
def get_all_cita():
    cita = Cita.query.all()
    return render_template("cita.html", cita=cita  )