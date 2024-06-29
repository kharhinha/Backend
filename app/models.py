from app.database import get_db

class Libro:

    def __init__(self, id_objeto=None, titulo=None, age=None, ejemplares=None, prestados=None, restantes=None, autor=None, editorial=None):
        self.id_objeto = id_objeto
        self.titulo = titulo
        self.age = age
        self.ejemplares = ejemplares
        self.prestados = prestados
        self.restantes = restantes
        self.autor = autor
        self.editorial = editorial

    #convercion de diccionario a formato Json
    def serialize(self):
        return {
            'id_objeto': self.id_objeto,
            'titulo': self.titulo,
            'age': self.age,
            'ejemplares': self.ejemplares,
            'prestados': self.prestados,
            'restantes': self.restantes,
            'autor': self.autor,
            'editorial': self.editorial,
        }

    @staticmethod#ambito global listar todos los datos
    def gett_all():
        db = get_db()
        cursor =db.cursor()
        cursor.execute("SELECT * FROM libro")#modificar objeto
        rows = cursor.fetchall()
        objetos = [Libro(id_objeto=row[0], titulo=row[1], age=row[2],ejemplares=row[3], prestados=row[4],restantes=row[5],autor=row[6],editorial=row[7]) for row in rows]
        cursor.close()
        return objetos

    #para traer el objeto
    @staticmethod
    def get_by_id(objeto_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM libro WHERE id_objeto = %s", (objeto_id,))#modificar objeto
        row = cursor.fetchone()
        cursor.close()
        if row:
           return Libro(id_objeto=row[0],titulo=row[1], age=row[2],ejemplares=row[3], 
         prestados=row[4],restantes=row[5],autor=row[6],editorial=row[7])
        return None 

    #guardar y actualizar objeto
    def save_objeto(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_objeto:
            cursor.execute("""
                UPDATE libro SET titulo=%s, age=%s, ejemplares=%s, prestados=%s, restantes=%s, autor=%s, editorial=%s
                WHERE id_objeto = %s
            """, (self.titulo, self.age ,self.ejemplares, self.prestados, self.restantes, self.autor, self.editorial, self.id_objeto))
        else:
            cursor.execute(""" INSERT INTO libro (titulo, age, ejemplares, prestados, restantes, autor, editorial) VALUES (%s, %s,%s, %s,%s, %s,%s)
               
            """, (self.titulo, self.age ,self.ejemplares, self.prestados, self.restantes, self.autor, self.editorial))
            self.id_objeto = cursor.lastrowid
        db.commit()
        cursor.close()

    #para eliminar el objeto
    def delete(self):
        db = get_db()
        cursor =db.cursor()
        cursor.execute("DELETE FROM libro WHERE id_objeto = %s", (self.id_objeto,))#modificar objeto
        db.commit()
        cursor.close()
    
  




