from flask import Blueprint
from flask import jsonify
from flask import request
from flask_cors import CORS, cross_origin
from flask import Blueprint
from api.doctor import doctores
from api.enfermera import enfermeras
from api.admin import admin
from api.paciente import pacientes

urlLogin = Blueprint('login', __name__,)


@urlLogin.route('/api/login', methods=['POST'])
def login():
    encontrado = True
    json = request.get_json(force=True)

    usuario = json['usuario']
    contrasena = json['contrasena']

    for i in admin:
        if(usuario == i['usuario'] and contrasena == i['contrasena']):
            res = {
                'nombre': i['nombre'],
                'apellido': i['apellido'],
                'usuario': i['usuario'],
                'contrasena': i['contrasena'],
                'tipo':'admin' 
            }
            return jsonify(res)
            break

    for i in doctores:
        if(usuario == i.usuario and contrasena == i.contrasena):
            res = {
                'nombre': i.nombre,
                'apellido': i.apellido,
                'fecha': i.fecha,
                'genero': i.genero,
                'usuario': i.usuario,
                'contrasena': i.contrasena,
                'especialidad': i.especialidad,
                'telefono': i.telefono,
                'tipo':'doctor'
            }
            return jsonify(res)
            break

    for i in enfermeras:
        if(usuario == i.usuario and contrasena == i.contrasena):
            res = {
                'nombre': i.nombre,
                'apellido': i.apellido,
                'fecha': i.fecha,
                'genero': i.genero,
                'usuario': i.usuario,
                'contrasena': i.contrasena,
                'telefono': i.telefono,
                'tipo':'enfermero'
            }
            return jsonify(res)
            break

    for i in pacientes:
        if(usuario == i.usuario and contrasena == i.contrasena):
            res = {
                'nombre': i.nombre,
                'apellido': i.apellido,
                'fecha': i.fecha,
                'genero': i.genero,
                'usuario': i.usuario,
                'contrasena': i.contrasena,
                'telefono': i.telefono,
                'tipo':'paciente'
            }
            return jsonify(res)
            break

    return jsonify({'res': 'no existe'})
