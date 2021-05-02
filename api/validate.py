from flask import Blueprint
from flask import jsonify
from flask import request
from api.doctor import doctores
from api.enfermera import enfermeras
from api.paciente import pacientes 

urlValidate = Blueprint('validate', __name__,)

@urlValidate.route('/api/validar', methods=['GET'])
def validarUsuario():
    json = json