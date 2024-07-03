from flask import Flask
from app.views import *
from app.database import init_app #inicializa la conexion de la base de datos
from flask_cors import CORS

#inicializacion del proyecto flask
app = Flask(__name__)
#app = Flask(__name__,template_folder='path/to/templates')

init_app(app)
CORS(app)  # Habilita CORS para todas las rutas

#rutas de la api_rest
app.route('/', methods=['GET'])(index)
app.route('/registro', methods=['GET'])(registro)
app.route('/sesion', methods=['GET'])(inicio_sesion)
app.route('/api/libro', methods=['GET'])(libro)
app.route('/edicion', methods=['GET'])(edicion)

#app.route('/api/lista/libro', methods=['GET'])(buscar_libro)

#----------------------------------------------------
app.route('/api/lista/libro', methods=['GET'])(get_all)
app.route('/api/libro', methods=['POST'])(create_objeto)
app.route('/api/libro/<int:objeto_id>',methods=['GET'])(get_objeto)
app.route('/api/libro/<int:objeto_id>',methods=['PUT'])(update_objeto)
app.route('/api/libro/<int:objeto_id>',methods=['DELETE'])(delete_objeto)

#verifica si se ejecuta o no este archivo
if __name__=='__main__':
    app.run(debug=True)