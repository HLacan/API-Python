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

@urlPaciente.route('/api/addPaciente', methods=['POST'])
def addPaciente():
    repetido = True
    json = request.get_json(force=True)
    nombre = json['nombre']
    apellido = json['apellido']
    fecha = json['fecha']
    genero = json['genero']
    usuario = json['usuario']
    contrasena = json['contrasena']
    telefono = json['telefono']

    if nombre is None and apellido is None and fecha is None and genero is None and usuario is None and contrasena is None:
        return jsonify({'res': 'Campos Vacios'})
    else:
        for i in pacientes:
            if i.usuario == usuario:
                repetido = False
                return jsonify({'res': 'Usuario ya repetido'})
                break

        if repetido == True:
            if telefono is None:
                telefono = 'Ninguno'

            pacientes.append(Paciente(nombre, apellido, fecha, genero, usuario, contrasena, telefono))
            return jsonify({'res': 'Paciente agregada correctamente'})

@urlPaciente.route('/api/getPaciente/<usuario>', methods=['GET'])
def getPaciente(usuario):
    encontrado = False
    res = {}
    for i in pacientes:
        if i.usuario == usuario:
            res = {
                'nombre': i.nombre,
                'apellido': i.apellido,
                'fecha': i.fecha,
                'genero': i.genero,
                'usuario': i.usuario,
                'contrasena': i.contrasena,
                'telefono': i.telefono
            }
            encontrado = True
            break
    
    if encontrado:
        return jsonify(res)
    else:
        return jsonify({'res':'No encontrado'})