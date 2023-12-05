# Crear un directorio
import os
def crear_directorio(ruta):
    try:
        os.makedirs(ruta)
    except OSError as e:
        pass
    os.chdir(ruta)


crear_directorio('C:\\Users\\ASUS\\Documents\\empty') 