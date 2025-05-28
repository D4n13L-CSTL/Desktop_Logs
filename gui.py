from tkinter import *
from tkinter import filedialog
from model_insert import insertar
from gestion_paths import Consultar
from tkinter import messagebox
import os
import sys
alto = 550
ancho = 550 

def seleccionar_carpeta():
    ruta = filedialog.askdirectory()
    if ruta:
        etiqueta_ruta.config(text=ruta)
        nombre = ruta.split('/')
        insertar(ruta, nombre[len(nombre) - 1])
        messagebox.showinfo('INFO', f'Ruta {ruta} agregada, correctamente')
        rutas_label()
    
    return ruta

consu = Consultar()
def rutas_label():
    
    for i in enumerate(consu.consultar_ruta(),start=4):
        Label(frame1, text=f'Nombre: {i[1][1]} | Ruta: {i[1][0]}').grid(row=i[0], column=0)
    
    
root = Tk()
root
alto_pantalla  = root.winfo_screenheight()
ancho_pantalla = root.winfo_screenwidth()

pos_x = (ancho_pantalla // 2) - (ancho // 2)
pos_y = (alto_pantalla // 2) - (alto // 2)
root.geometry(f"{ancho}x{alto}+{pos_x}+{pos_y}")
root.title('GESTOR DE RUTAS')

frame1 = Frame(root)
frame1.place(x=50, y=50)
Label(frame1, text='RUTAS Y CARPETAS DE LOGS').grid(row=0, column=0)
Button(frame1, text='Seleccionar Carpeta', width=25, command=seleccionar_carpeta).grid(row=1, column=0)
etiqueta_ruta = Label(frame1, text="SELECCIONAR CARPETA")
etiqueta_ruta.grid(row=2,column=0)

Label(frame1, text="-----------------------------------------------------------\n Carpetas Seleccionadas:").grid(row=3, column=0)
rutas_label()


root.mainloop()
