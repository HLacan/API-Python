from flask import Blueprint

urlDoctor = Blueprint('doctor', __name__,)

@urlDoctor.route('/agregarDoctor')
def addDoctor():
    return 'Agregar Doctores'