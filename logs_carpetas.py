import os
import time
import logging
import getpass
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler,FileDeletedEvent, DirDeletedEvent
from rutas import rutas  #función que consulta la DB
from model_SMPT import enviar_correo  # función para enviar correos


base_dir = Path().resolve()
usuario = getpass.getuser()

class EventoCarpeta(FileSystemEventHandler):
    def on_modified(self, event):
        logging.info(f"Modificado: {event.src_path} for user {usuario}")

    def on_created(self, event):
        logging.info(f"Creado: {event.src_path} for user {usuario}")
        
        
        
    def on_deleted(self, event):
        logging.info(f"Eliminado: {event.src_path} for user {usuario}")
        nombre_file = os.path.basename(event.src_path)
        enviar_correo(event.src_path, nombre_file, usuario) 

def iniciar_monitoreo():
    db_path = base_dir / "log_varias_carpetas.log"
    logging.basicConfig(
        filename=db_path,
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
    )

    event_handler = EventoCarpeta()
    observer = Observer()
    observer.start()

    carpetas_monitoreadas = set()

    try:
        while True:
            carpetas_a_monitorear = [ruta[0] for ruta in rutas()]

            for carpeta in carpetas_a_monitorear:
                if carpeta not in carpetas_monitoreadas:
                    if os.path.exists(carpeta):
                        observer.schedule(event_handler, path=carpeta, recursive=True)
                        carpetas_monitoreadas.add(carpeta)
                        logging.info(f"Nuevo monitoreo: {carpeta}")
                    else:
                        logging.warning(f"Ruta no existe: {carpeta}")
            
            time.sleep(10)  # Chequea cada 10 segundos
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    iniciar_monitoreo()
