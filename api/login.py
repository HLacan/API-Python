from flask import Blueprint
from flask import jsonify
from flask import request
from flask_cors import CORS, cross_origin
from flask import Blueprint
from api.doctor import doctores

urlLogin = Blueprint('login', __name__,)

@urlLogin.route('/api/login', methods=['POST'])
def login():
    encontrado = True
    json = request.get_json(force=True)

    usuario = json['usuario']
    contrasena = json['contrasena']

    if usuario == 'admin' and contrasena == '1234':
        return jsonify({'res':'admin'})
    else:
        for i in doctores:
            if(usuario == i.usuario and contrasena == i.contrasena):
                return jsonify({'res': 'doctor'})

