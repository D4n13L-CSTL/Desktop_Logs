import pyodbc
import sqlite3
from pathlib import Path


base_dir  = Path().resolve()
db_path = base_dir  / "rutas.db"


def get_db():
    conexion = sqlite3.connect(str(db_path))
    return conexion



class Insertar:
    def insertar_ruta(self,ruta,nombre):
        conexion = get_db()
        cursor = conexion.cursor() 
        cursor.execute("INSERT INTO RUTAS (RUTA, NOMBRE) VALUES (?, ?)", (ruta,nombre))
        conexion.commit()
        conexion.close()
    
class Consultar:
    def consultar_ruta(self):
        conexion = get_db()
        cursor = conexion.cursor() 
        cursor.execute("SELECT RUTA,NOMBRE FROM RUTAS")
        rutas = cursor.fetchall()
        conexion.close()
        return rutas

class Update:
    def update_ruta(self,ruta,nueva_ruta):
        conexion = get_db()
        cursor = conexion.cursor() 
        cursor.execute("UPDATE RUTAS SET RUTA = ? WHERE RUTA = ?", (nueva_ruta,ruta))
        conexion.commit()
        conexion.close()
    

class Delete:
    def delete_ruta(self,ruta):
        conexion = get_db()
        cursor = conexion.cursor() 
        cursor.execute("DELETE FROM RUTAS WHERE RUTA = ?", (ruta,))
        conexion.commit()
        conexion.close()
    
consu = Consultar()

for i in enumerate(consu.consultar_ruta(), start=2):
    print(i[1][1])