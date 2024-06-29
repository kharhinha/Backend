from flask import jsonify, request
from app.models import Libro

#en general se devuelve datos Json o xml
def index():
    return '<h1> Hola mundo </h1>'

def get_all():
    objeto = Libro.gett_all()
    list_objeto = [obj.serialize() for obj in objeto]
    return jsonify(list_objeto)

def get_objeto(objeto_id):
    obj = Libro.get_by_id(objeto_id)
    if not obj:
        return jsonify({'message':'Error al traer la información'}),404
    return jsonify(obj.serialize())

def create_objeto():
    #datos recibidos en formato json
    data = request.json
    nuevo_objeto = Libro( 
        titulo = data['titulo'],
        age=data['age'],
        ejemplares = data['ejemplares'],
        prestados=data['prestados'],
        restantes = data['restantes'],
        autor=data['autor'],
        editorial=data['editorial']
    )
    nuevo_objeto.save_objeto()
    return jsonify({'message':'Libro ingresado correctamente'}),201

def update_objeto(objeto_id):
   obj = Libro.get_by_id(objeto_id)
   #datos recibidos en formato json
   if not obj:
    return jsonify({'message':'Modificación no realizada'}),404
   data = request.json
   obj.titulo = data['titulo']
   obj.age =  data['age']
   obj.ejemplares = data['ejemplares']
   obj.prestados= data['prestados']
   obj.restantes = data['restantes']
   obj.autor= data['autor']
   obj.editorial =data['editorial']
   obj.save_objeto()
   return jsonify({'message':'Se modificaron los datos','data':data,'id':objeto_id})

def delete_objeto(objeto_id):
    obj = Libro.get_by_id(objeto_id)
    if not obj:
        return jsonify({'message':'No se elimino el libro'}),404
    obj.delete()
    return jsonify({'message':'Libro eliminado'})