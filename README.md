# 📂 File Watcher Desktop App

Aplicación de escritorio desarrollada en **Python** para el monitoreo de **carpetas compartidas**. Registra eventos en tiempo real en un archivo `.log` y envía **correos electrónicos de alerta** cuando se detecta la **eliminación de archivos o carpetas**.

La ruta de la carpeta seleccionada se guarda en una base de datos **SQLite**, lo que permite su reutilización por un servicio independiente que se ejecuta en segundo plano.

---

## 🎯 Objetivo

Esta aplicación fue creada con fines de **monitoreo de carpetas compartidas en entornos de red**, permitiendo auditar cambios críticos, especialmente eliminaciones, y notificar en tiempo real al administrador correspondiente.

---

## 🚀 Funcionalidades principales

- 🖥️ Interfaz de escritorio para seleccionar la ruta a monitorear
- 🗃️ Persistencia de rutas seleccionadas en una base de datos **SQLite**
- 📄 Registro de eventos (creación, modificación, eliminación) en un archivo `.log`
- 📧 Envío de **correos automáticos** al detectar **eliminación de archivos o carpetas**
- 🔐 Variables sensibles (correos y contraseña de aplicación) gestionadas por `.env`
- 📦 Empaquetado como ejecutable `.exe` con **PyInstaller**

---

## 🧱 Tecnologías utilizadas

- **Python 3**
- **SQLite** (almacenamiento local)
- **Tkinter** (GUI)
- **Watchdog** (monitoreo de sistema de archivos)
- **smtplib / email** (envío de correos)
- **dotenv** (gestión de variables de entorno)
- **PyInstaller** (empaquetado como `.exe`)

---

## ⚙️ Variables de entorno

La aplicación utiliza un archivo `.env` con las siguientes variables:


```env
USER=correo_destino@example.com
USER_ORIGEN=correo_origen@gmail.com
PASS=contraseña_de_aplicacion_google
```
## 🛠️ Cómo generar los ejecutables (.exe)

### 1. Instala las dependencias del proyecto:

pip install -r requirements.txt

### 2. Instala PyInstaller:

pip install pyinstaller

### 3. Ejecuta los siguientes comandos para generar los ejecutables:
Ejecutable de la interfaz gráfica (GUI)
pyinstaller --onefile --add-data "rutas.db;." gui.py

Ejecutable del monitor de carpetas
pyinstaller --onefile --add-data "rutas.db;." logs_carpetas.py


> 🛑 **Nota:**  
> En Windows usa `;` como separador en `--add-data`.  
> En Linux/macOS usa `:` en lugar de `;`.

### 4. Resultado

Los archivos `.exe` se generarán en la carpeta `dist/`.

