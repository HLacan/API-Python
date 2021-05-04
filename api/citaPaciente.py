from flask import Blueprint
from flask import jsonify
from flask import request
from api.paciente import pacientes
from model.CitaPaciente import CitaPaciente
from api.doctor import doctores

urlCitaPaciente = Blueprint('citaPaciente', __name__,)

@urlCitaPaciente.route('/api/addCitaPaciente', methods=['POST'])
def addCitaPaciente():
    json = request.get_json(force=True)

    fecha = json['fecha']
    hora = json['hora']
    descripcion = json['descripcion']
    usuario = json['usuario']
    estado = json['estado']

    for i in pacientes:
        if i.usuario == usuario:
            if len(i.cita) == 0:
                i.cita.append(CitaPaciente(fecha,hora,descripcion, estado, usuario))
                return jsonify({'res':'agregado'})
            else:
                for j in i.cita:
                    if j.estado == 'pendiente' or j.estado == 'aceptado':
                        return jsonify({'res':'ya hay citas'})
                    else:
                        i.cita.append(CitaPaciente(fecha,hora,descripcion, estado,  usuario))
                        return jsonify({'res':'agregado'})
    return jsonify({'res':'nel'})
    
@urlCitaPaciente.route('/api/getCitasPaciente/<usuario>', methods=['GET'])
def getCitasPaciente(usuario):
    encontrado = False
    response = []
    for i in pacientes:
        if i.usuario == usuario:
            for j in i.cita:
                response.append({
                    'fecha': j.fecha,
                    'hora': j.hora,
                    'descripcion': j.descripcion,
                    'estado': j.estado,
                    'usuario':  j.usuario
                })
    return jsonify(response)

@urlCitaPaciente.route('/api/getCitasPendientes', methods=['GET'])
def getCitasPendientes():
    response = []
    for i in pacientes:
            for j in i.cita:
                if j.estado == 'pendiente':
                    response.append({
                        'fecha': j.fecha,
                        'hora': j.hora,
                        'descripcion': j.descripcion,
                        'estado': j.estado,
                        'usuario': j.usuario
                    })
    return jsonify(response)

@urlCitaPaciente.route('/api/updateEstado', methods=['POST'])
def updateEstado():
    json = request.get_json(force=True)

    estado = json['estado']
    usuario = json['usuario']
    doctor = json['doctor']

    if estado == 'rechazado':
        for l in pacientes:
            if l.usuario == usuario:
                for j in l.cita:
                    if j.estado == 'pendiente':
                        j.estado = 'rechazado'
                        return jsonify({'res':'rechazado'})
                        break

    elif estado == 'completado':
        for i in doctores:
            if i.usuario == doctor:
                for j in i.cita:
                    if j.usuario == usuario and j.doctor == j.doctor:
                        j.estado = 'completado'

        for i in doctores:
            if i.usuario == doctor:
                for j in pacientes:
                    if j.usuario == usuario:
                        for k in j.cita:
                            if k.estado == 'aceptado':
                                k.estado = 'completado'
                                return({'res':'completado'})
                

    else:
        for i in doctores:
            if i.usuario == doctor:
                for j in pacientes:
                    if j.usuario == usuario:
                        for k in j.cita:
                            if k.estado == 'pendiente':
                                k.estado = 'aceptado'
                                i.cita.append(CitaPaciente(k.fecha, k.hora, k.descripcion, k.estado, k.usuario, i.usuario))
                                return({'res':'agregado'})



    return jsonify({'res':'modificado'})

@urlCitaPaciente.route('/api/getCitasAceptadas/<usuario>', methods=['GET'])
def getCitasAceptadas(usuario):
    response = []
 
    for i in doctores:
        if i.usuario == usuario:
            for j in i.cita:
                if j.estado == 'aceptado' or j.estado == 'completado':
                    response.append({
                        'fecha': j.fecha,
                        'hora': j.hora,
                        'descripcion': j.descripcion,
                        'estado': j.estado,
                        'usuario': j.usuario,
                        'doctor': j.doctor
                    })

    return jsonify(response)

@urlCitaPaciente.route('/api/getCitasAceptadas', methods=['GET'])
def getCitasAceptadasE():
    response = []
 
    for i in doctores:
            for j in i.cita:
                if j.estado == 'aceptado':
                    response.append({
                        'fecha': j.fecha,
                        'hora': j.hora,
                        'descripcion': j.descripcion,
                        'estado': j.estado,
                        'usuario': j.usuario,
                        'doctor': j.doctor
                    })

    return jsonify(response)

@urlCitaPaciente.route('/api/getCitasAceptadasD', methods=['GET'])
def getCitasAceptadasD():
    response = []
 
    for i in doctores:
            for j in i.cita:
                if j.estado == 'aceptado' or j.estado == 'completado':
                    response.append({
                        'fecha': j.fecha,
                        'hora': j.hora,
                        'descripcion': j.descripcion,
                        'estado': j.estado,
                        'usuario': j.usuario,
                        'doctor': j.doctor
                    })

    return jsonify(response)

