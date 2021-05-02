from flask import Blueprint
from flask import jsonify
from flask import request
from model.Paciente import Paciente

urlPaciente = Blueprint('paciente', __name__,)

pacientes = []

@urlPaciente.route('/api/getPacientes', methods=['GET'])
def getPacientes():
    res = []
    for i in pacientes:
        res.append({
            'nombre': i.nombre,
            'apellido': i.apellido,
            'fecha': i.fecha,
            'genero': i.genero,
            'usuario': i.usuario,
            'contrasena': i.contrasena,
            'telefono': i.telefono
        })
    return jsonify(res)