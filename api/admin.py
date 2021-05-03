from flask import Blueprint
from flask import jsonify
from flask import request

admin = []
admin.append({'nombre':'Carlos', 'apellido':'Campaneros','usuario':'admin', 'contrasena':'1234'})

urlAdmin = Blueprint('admin', __name__,)

@urlAdmin.route('/api/getAdmin', methods=['GET'])
def getAdmin():
    return jsonify(admin)
