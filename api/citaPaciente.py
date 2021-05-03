from flask import Blueprint
from flask import jsonify
from flask import request
from api.paciente import pacientes
from model.CitaPaciente import CitaPaciente

urlCitaPaciente = Blueprint('citaPaciente', __name__,)

@urlCitaPaciente.route('/api/addCitaPaciente', methods=['POST'])
def addCitaPaciente():
    json = request.get_json(force=True)

    fecha = json['fecha']
    hora = json['hora']
    descripcion = json['descripcion']
    usuario = json['usuario']
    estado = json['estado']

    print(fecha)
    print(hora)
    print(descripcion)
    print(estado)

    for i in pacientes:
        if i.usuario == usuario:
            i.cita.append(CitaPaciente(fecha,hora,descripcion, estado))
            return jsonify({'res':'agregado'})

    return jsonify({'res':'nel'})

@urlCitaPaciente.route('/api/getCitasPaciente/<usuario>', methods=['GET'])
def getCitasPaciente(usuario):
    response = []
    for i in pacientes:
        if i.usuario == usuario:
            for j in i.cita:
                response.append({
                    'fecha': j.fecha,
                    'hora': j.hora,
                    'descripcion': j.descripcion,
                    'estado': j.estado
                })
    return jsonify(response)

