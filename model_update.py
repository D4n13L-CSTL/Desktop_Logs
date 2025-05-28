from gestion_paths import Update

valor_update = r"C:/Users/Windows 11/Documents/Updated_PDF"
nueva_ruta = r"C:/Users/Windows 11/Documents/PDF"

update = Update()
update.update_ruta(valor_update, nueva_ruta)

print("Ruta actualizada correctamente.")