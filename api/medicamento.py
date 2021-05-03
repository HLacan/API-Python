from flask import Blueprint
from flask import jsonify
from flask import request
from flask_cors import CORS, cross_origin
from model.Medicamento import Medicamento

medicamentos = []
medicamentos.append(Medicamento("Lanzoprazol","5.50","alivia el dolor","100"))
medicamentos.append(Medicamento("Acetaminofen","10.75","dolores de cabeza","75"))


urlMedicamento = Blueprint('medicamento', __name__,)

@urlMedicamento.route('/api/getMedicamentos', methods=['GET'])
def getMedicamentos():
    res = []
    for i in medicamentos:
        res.append({
            'nombre': i.nombre,
            'precio': i.precio,
            'descripcion': i.descripcion,
            'cantidad': i.cantidad,
        })
    return jsonify(res)

@urlMedicamento.route('/api/addMedicamento', methods=['POST'])
def addMedicamento():
    repetido = True
    json = request.get_json(force=True)
    nombre = json['nombre']
    precio = json['precio']
    descripcion = json['descripcion']
    cantidad = json['cantidad']

    if nombre is None and precio is None and descripcion is None and cantidad is None:
        return jsonify({'res': 'Campos Vacios'})
    else:
        for i in medicamentos:
            if i.nombre == nombre:
                repetido = False
                return jsonify({'res': 'medicamento ya repetido'})
                break
            else:
                medicamentos.append(Medicamento(nombre, precio, descripcion, cantidad))
                return jsonify({'res': 'medicamento agregada correctamente'})

@urlMedicamento.route('/api/getMedicamento/<nombre>', methods=['GET'])
def getMedicamento(nombre):
    encontrado = False
    res = {}
    for i in medicamentos:
        if i.nombre == nombre:
            res = {
                'nombre': i.nombre,
                'precio': i.precio,
                'descripcion': i.descripcion,
                'cantidad': i.cantidad,
            }
            encontrado = True
            break
    
    if encontrado:
        return jsonify(res)
    else:
        return jsonify({'res':'No encontrado'})

@urlMedicamento.route('/api/updateMedicamento', methods=['POST'])
def updateMedicamento():
    json = request.get_json(force=True)

    oldNombre = json['oldNombre']
    newNombre = json['newNombre']
    precio = json['precio']
    descripcion = json['descripcion']
    cantidad = json['cantidad']

    for i in medicamentos:
        if i.nombre == oldNombre:
            i.nombre = newNombre
            i.precio = precio
            i.descripcion = descripcion
            i.cantidad = cantidad
            return jsonify({'res':'modificado'})
    
    return jsonify({'res':'no ok'})