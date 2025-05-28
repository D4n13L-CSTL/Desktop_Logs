import pyodbc
import sqlite3
from pathlib import Path



base_dir  = Path().resolve()
db_path = base_dir  / "rutas.db"


def get_db():
    conexion = sqlite3.connect(str(db_path))
    return conexion


def rutas():
    conexion = get_db()
    cursor = conexion.cursor() 
    cursor.execute("SELECT RUTA FROM RUTAS")
    rutas = cursor.fetchall()
    conexion.close()
    return rutas

