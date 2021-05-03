from flask import Blueprint
from flask import jsonify
from flask import request
from flask_cors import CORS, cross_origin
from model.Doctor import Doctor

doctores = []
doctores.append(Doctor("Armando","Contreras","01/02/2001","M","drCon","456","huesos","71258565",))
doctores.append(Doctor("Mauricia","Anastacia","07/06/1994","F","mauriAna","789","bebes","4617624",))


urlDoctor = Blueprint('doctor', __name__,)

@urlDoctor.route('/api/addDoctor', methods=['POST'])
def addDoctor():
    repetido = True

    json = request.get_json(force=True)

    nombre = json['nombre']
    apellido = json['apellido']
    fecha = json['fecha']
    genero = json['genero']
    usuario = json['usuario']
    contrasena = json['contrasena']
    especialidad = json['especialidad']
    telefono = json['telefono']

    if nombre is None and apellido is None and fecha is None and genero is None and usuario is None and contrasena is None and especialidad is None:
        return jsonify({'res': 'Campos Vacios'})
    else:
        for i in doctores:
            if i.usuario == usuario:
                repetido = False
                return jsonify({'res': 'Usuario ya repetido'})
                break

        if repetido == True:
            if telefono is None:
                telefono = 'Ninguno'

            doctores.append(Doctor(nombre, apellido, fecha, genero, usuario, contrasena, especialidad, telefono))
            return jsonify({'res': 'Doctor agregado correctamente'})

@urlDoctor.route('/api/getDoctores', methods=['GET'])
def getDoctores():
    response = []
    for i in doctores:
        response.append({
            'nombre': i.nombre,
            'apellido': i.apellido,
            'fecha': i.fecha,
            'genero': i.genero,
            'usuario': i.usuario,
            'contrasena': i.contrasena,
            'especialidad': i.especialidad,
            'telefono': i.telefono
        })
    return jsonify(response)

@urlDoctor.route('/api/getDoctor/<usuario>', methods=['GET'])
def getDoctor(usuario):
    encontrado = False
    res = {}
    for doctor in doctores:
        if doctor.usuario == usuario:
            res = {
                'nombre': doctor.nombre,
                'apellido': doctor.apellido,
                'fecha': doctor.fecha,
                'genero': doctor.genero,
                'usuario': doctor.usuario,
                'contrasena': doctor.contrasena,
                'especialidad': doctor.especialidad,
                'telefono': doctor.telefono
            }
            encontrado = True
            break
    
    if encontrado:
        return jsonify(res)
    else:
        return jsonify({'res':'No encontrado'})

@urlDoctor.route('/api/getUpdateDoctor/<usuario>', methods=['GET'])
def getUpdateDoctor(usuario):
    encontrado = False
    for i in doctores:
        if i.usuario == usuario:
            encontrado = True
    
    if encontrado == True:
        return jsonify({'res':'existe'})
    else:
        return jsonify({'res':'no existe'})

@urlDoctor.route('/api/updateDoctor', methods=['POST'])
def updateDoctor():
    json = request.get_json(force=True)

    nombre = json['nombre']
    apellido = json['apellido']
    fecha = json['fecha']
    genero = json['genero']
    usuario = json['usuario']
    contrasena = json['contrasena']
    especialidad = json['especialidad']
    telefono = json['telefono']

    for i in doctores:
        if i.usuario == usuario:
            i.nombre = nombre
            i.apellido = apellido
            i.fecha = fecha
            i.genero = genero
            i.usuario = usuario
            i.contrasena = contrasena
            i.especialidad = especialidad
            i.telefono = telefono
            return jsonify({'res':'modificado'})
            
@urlDoctor.route('/api/deleteDoctor/<usuario>',methods=['GET'])
def deleteDoctor(usuario):
    encontrado = False
    for i in doctores:
        if i.usuario == usuario:
            doctores.remove(i)
            encontrado = True
            break
        
    if encontrado:
        return jsonify({'res': 'eliminado'})
    else:
        return jsonify({'res':'usuario no encontrado'})
    
