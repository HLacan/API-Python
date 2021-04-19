from flask import Blueprint

urlDoctor = Blueprint('doctor', __name__,)

@urlDoctor.route('/addDoctor')
def addDoctor():
    return 'Agregar Doctores'

@urlDoctor.route('/getDoctores')
def getDoctores():
    return 'Obteniendo Doctores'

@urlDoctor.route('/updateDoctor')
def updateDoctor():
    return 'Actualizando Doctor'

@urlDoctor.route('/deleteDoctor')
def deleteDoctor():
    return 'Eliminando Doctor'