from gestion_paths import Insertar

def insertar(ruta,nombre):
    valor_insertar = ruta
    nombre_insertar = nombre
    insertar = Insertar()
    insertar.insertar_ruta(valor_insertar, nombre_insertar)


