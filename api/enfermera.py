from flask import Blueprint
from flask import jsonify
from flask import request
from flask_cors import CORS, cross_origin
from model.Enfermera import Enfermera


enfermeras = []
enfermeras.append(Enfermera("Shay","Hurtado","02/05/1996","F","shay01","trol","22537520"))

urlEnfermera = Blueprint('enfermera', __name__,)

@urlEnfermera.route('/api/addEnfermera', methods=['POST'])
def addEnfermera():
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
        for i in enfermeras:
            if i.usuario == usuario:
                repetido = False
                return jsonify({'res': 'Usuario ya repetido'})
                break

        if repetido == True:
            if telefono is None:
                telefono = 'Ninguno'

            enfermeras.append(Enfermera(nombre, apellido, fecha, genero, usuario, contrasena, telefono))
            return jsonify({'res': 'Enfermera agregada correctamente'})

@urlEnfermera.route('/api/getEnfermeras', methods=['GET'])
def getEnfermeras():
    response = []
    for i in enfermeras:
        response.append({
            'nombre': i.nombre,
            'apellido': i.apellido,
            'fecha': i.fecha,
            'genero': i.genero,
            'usuario': i.usuario,
            'contrasena': i.contrasena,
            'telefono': i.telefono
        })
    return jsonify(response)

@urlEnfermera.route('/api/getEnfermera/<usuario>', methods=['GET'])
def getEnfermera(usuario):
    encontrado = False
    res = {}
    for i in enfermeras:
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

@urlEnfermera.route('/api/getUpdateEnfermera/<usuario>', methods=['GET'])
def getUpdateEnfermera(usuario):
    encontrado = False
    for i in enfermeras:
        if i.usuario == usuario:
            encontrado = True
    
    if encontrado == True:
        return jsonify({'res':'existe'})
    else:
        return jsonify({'res':'no existe'})

@urlEnfermera.route('/api/updateEnfermera', methods=['POST'])
def updateEnfermera():
    json = request.get_json(force=True)

    nombre = json['nombre']
    apellido = json['apellido']
    fecha = json['fecha']
    genero = json['genero']
    usuario = json['usuario']
    contrasena = json['contrasena']
    telefono = json['telefono']

    print(usuario)

    for i in enfermeras:
        if i.usuario == usuario:
            i.nombre = nombre
            i.apellido = apellido
            i.fecha = fecha
            i.genero = genero
            i.usuario = usuario
            i.contrasena = contrasena
            i.telefono = telefono
            return jsonify({'res':'modificado'})
    
    return jsonify({'res':'no ok'})
            
@urlEnfermera.route('/api/deleteEnfermera/<usuario>',methods=['GET'])
def deleteEnfermera(usuario):
    encontrado = False
    for i in enfermeras:
        if i.usuario == usuario:
            enfermeras.remove(i)
            encontrado = True
            break
        
    if encontrado:
        return jsonify({'res': 'eliminado'})
    else:
        return jsonify({'res':'usuario no encontrado'})
    
