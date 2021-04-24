from flask import Blueprint
from flask import jsonify
from flask import request
from flask_cors import CORS, cross_origin
from model.Doctor import Doctor

doctores = []

#doctores = [Doctor("Herbert","Lacan","31/05/1999",'M',"hlacan","abc123","Huesos","22537520")]
# doctores.append(Doctor("Hellen","Hernandez","06/07/1994",'F',"helcan","zxc789","Corazon","47345057"))


urlDoctor = Blueprint('doctor', __name__,)


@urlDoctor.route('/api/addDoctor', methods=['POST'])
def addDoctor():
    repetido = True

    json = request.get_json(force=True)

    nombre = json['nombre']
    apellido = json['apellido']
    fecha = json['fecha']
    sexo = json['sexo']
    usuario = json['usuario']
    contrasena = json['contrasena']
    especialidad = json['especialidad']
    telefono = json['telefono']

    if nombre is None and apellido is None and fecha is None and sexo is None and usuario is None and contrasena is None and especialidad is None:
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

            doctores.append(Doctor(nombre, apellido, fecha, sexo,
                            usuario, contrasena, especialidad, telefono))
            return jsonify({'res': 'Doctor agregado correctamente'})


@urlDoctor.route('/api/getDoctores', methods=['GET'])
def getDoctores():
    response = []
    for i in doctores:
        response.append({
            'nombre': i.nombre,
            'apellido': i.apellido,
            'fecha': i.fecha,
            'sexo': i.sexo,
            'usuario': i.usuario,
            'contrasena': i.password,
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
                'sexo': doctor.sexo,
                'usuario': doctor.usuario,
                'contrasena': doctor.password,
                'especialidad': doctor.especialidad,
                'telefono': doctor.telefono
            }
            encontrado = True
            break
    
    if encontrado:
        return jsonify(res)
    else:
        return jsonify({'res':'No encontrado'})
    


@urlDoctor.route('/api/updateDoctor/<usuario>')
def updateDoctor(usuario):
    return 'Actualizando Doctor'


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
    
