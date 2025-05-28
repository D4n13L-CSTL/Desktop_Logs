import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
load_dotenv()


# Configuración del correo
email_origen = os.getenv('USER_ORIGEN')
email_destino = os.getenv('USER')
contraseña = os.getenv('PASS')

# Crear el mensaje
mensaje = EmailMessage()
mensaje['Subject'] = 'AVISO'
mensaje['From'] = email_origen
mensaje['To'] = email_destino


def enviar_correo(Archivo, nombre_file, usuario):
# Enviar el mensaje
    mensaje.set_content(f'Eliminación de {nombre_file} ha sido detectada. Ruta de Archivo: {Archivo} for user {usuario} ') 
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_origen, contraseña)
            smtp.send_message(mensaje)
        print("Correo enviado correctamente.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
