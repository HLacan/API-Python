from flask import Blueprint
from flask import jsonify
from flask import request
from model.Doctor import Doctor

doctores = [Doctor("Herbert","Lacan","31/05/1999",'M',"hlacan","abc123","Huesos","22537520")]
doctores.append(Doctor("Hellen","Hernandez","06/07/1994",'F',"helcan","zxc789","Corazon","47345057"))


urlDoctor = Blueprint('doctor', __name__,)

@urlDoctor.route('/api/addDoctor', methods=['POST'])
def addDoctor():
    data = json.loads(request.data)
    text = data.get("text", None)
    if text is None:
        return jsonify({"message":"text not found"})
    else:
        return jsonify(data)

@urlDoctor.route('/api/getDoctores' ,methods=['GET'])
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

@urlDoctor.route('/updateDoctor')
def updateDoctor():
    return 'Actualizando Doctor'

@urlDoctor.route('/deleteDoctor')
def deleteDoctor():
    return 'Eliminando Doctor'