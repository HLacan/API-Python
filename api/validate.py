from flask import Blueprint
from flask import jsonify
from flask import request
from api.admin import admin
from api.doctor import doctores
from api.enfermera import enfermeras
from api.paciente import pacientes 

urlValidate = Blueprint('validate', __name__,)

@urlValidate.route('/api/validar/<oldUsuario>/<newUsuario>', methods=['GET'])
def validarUsuario(oldUsuario, newUsuario):
    
    for i in admin:
        if newUsuario == i['usuario']:
            return jsonify({'res':'existe'})
            break
    
    for i in doctores:
        if newUsuario == i.usuario:
            return jsonify({'res':'existe'})
            break

    for i in enfermeras:
        if newUsuario == i.usuario:
            return jsonify({'res':'existe'})
            break

    for i in pacientes:
        if newUsuario == i.usuario:
            return jsonify({'res':'existe'})
            break

    return jsonify({'res':'libre'})