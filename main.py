"""
30-04-2024 , version 1.0
"""

#----------------librerias a importar--------------#
import os
import shutil
import glob
import PyPDF2

#----------------librerias a importar--------------#
def validar_archivo(ruta_carpeta):
    # Obtener la lista de archivos en la carpeta
    archivos = os.listdir(ruta_carpeta)

    # Iterar sobre los archivos en la carpeta
    for archivo in archivos:
        # Obtener la ruta completa del archivo
        ruta_completa = os.path.join(ruta_carpeta, archivo)

        # Verificar si el archivo es un PDF
        if archivo.lower().endswith('.pdf'):
            print(f"{archivo} es un archivo PDF.")
            
            # Ruta del archivo que quieres mover
            ruta_archivo = f"{ruta_carpeta}\{archivo}"
            print(ruta_archivo)

            # Ruta de la carpeta a la que quieres mover el archivo
            nueva_ruta = r"C:\Users\sebastian\OneDrive\Escritorio\Automatizacion-TIGO\PDF"

            # Mover el archivo a la nueva carpeta
            shutil.move(ruta_archivo, nueva_ruta)
            
            #------------Extraer elementos para -----------#
           
           
            
        # Verificar si el archivo es un archivo de Excel (XLSX)
        elif archivo.lower().endswith('.xlsx'):
            print(f"{archivo} es un archivo de Excel (XLSX).")
            
            # Ruta del archivo que quieres mover
            ruta_archivo = f"{ruta_carpeta}\{archivo}"
            # print(ruta_archivo)

            # Ruta de la carpeta a la que quieres mover el archivo
            nueva_ruta = r"C:\Users\sebastian\OneDrive\Escritorio\Automatizacion-TIGO\XLSX"

            # Mover el archivo a la nueva carpeta
            shutil.move(ruta_archivo, nueva_ruta)
            
            
            
        # Si el archivo no es ni PDF ni XLSX
        else:
            print(f"{archivo} no es ni un PDF ni un archivo de Excel.")

# Ruta de la carpeta donde están los archivos (cambia esto por la ruta real de la carpeta)
ruta_carpeta = r"C:\Users\sebastian\OneDrive\Escritorio\Automatizacion-TIGO\Descargas"

# Llamar a la función para validar los archivos en la carpeta
validar_archivo(ruta_carpeta)