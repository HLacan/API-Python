from flask import Blueprint
from flask import jsonify
from flask import request

admin = []
admin.append({'nombre':'Carlos', 'apellido':'Campaneros','usuario':'admin', 'contrasena':'1234'})

urlAdmin = Blueprint('admin', __name__,)

@urlAdmin.route('/api/getAdmin', methods=['GET'])
def getAdmin():
    return jsonify(admin)

@urlAdmin.route('/api/updateAdmin', methods=['POST'])
def updateAdmin():
    json = request.get_json(force=True)

    nombre = json['nombre']
    apellido = json['apellido']
    oldUsuario = json['oldUsuario']
    newUsuario = json['newUsuario']
    contrasena = json['contrasena']

    for i in admin:
        if i['usuario'] == oldUsuario:
            i['nombre'] = nombre
            i['apellido'] = apellido
            i['usuario'] = newUsuario
            i['contrasena'] = contrasena
            return jsonify({'res':'modificado'})

    return jsonify({'res':'error'})
