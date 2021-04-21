from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
from flask import request
from api.doctor import urlDoctor
from api.login import urlLogin

def create_app(): 
    app = Flask(__name__)
    app.register_blueprint(urlDoctor)
    app.register_blueprint(urlLogin)
    CORS(app) 
    return app 

app = create_app()

@app.route('/')
def index():
    return 'index aqui estoy'

#app.create_app()

if __name__ == '__main__': 
    app.run(debug=True) 

