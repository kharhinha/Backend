from flask import Flask
from app.views import *
from app.database import init_app #inicializa la conexion de la base de datos

#inicializacion del proyecto flask
app = Flask(__name__)

init_app(app)

#rutas de la api_rest
app.route('/', methods=['GET'])(index)
app.route('/api/lista/libro', methods=['GET'])(get_all)
app.route('/api/libro', methods=['POST'])(create_objeto)
app.route('/api/libro/<int:objeto_id>',methods=['GET'])(get_objeto)
app.route('/api/libro/<int:objeto_id>',methods=['PUT'])(update_objeto)
app.route('/api/libro/<int:objeto_id>',methods=['DELETE'])(delete_objeto)

#verifica si se ejecuta o no este archivo
if __name__=='__main__':
    app.run(debug=True)