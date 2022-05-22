import requests

from datetime import datetime

import os

from app.config import logging


def eliminar_archivo():
    # especifiar ruta de los archivo
    path = 'C:\\Users\\WalterPc\\Documents\\Alkemy' 

    # especificar extencion
    extension = ".csv" 
    
    #comprobando si la ruta existe o no
    if os.path.exists(path):

        #compruebe si la ruta es directorio o no        
        if os.path.isdir(path):
            
            # iterando a través de las subcarpetasS
            for root_folder, folders, files in os.walk(path):

                # comprobación de los archivos 
                for file in files:
                    
                    # ruta de archivo
                    file_path = os.path.join(root_folder, file)

                    # extrayendo la extensión del nombre de archivo
                    file_extension = os.path.splitext(file_path)[1]

                    # comprobando la extensión_de_archivo
                    if extension == file_extension:

                        # borrando el archivo
                        if not os.remove(file_path):

                            # mensaje de exito
                            logging.info(f"{file_path} Archivo eliminado")
                        else: 
                            # mensaje de falla
                             logging.info(f"Unable to delete the {file_path}")
        else:
             # la ruta no es directorio
            logging.info(f"{path} is not a directory")
    else: 
        # la ruta no existe
        logging.info(f"{path} doesn't exist")



url_1 = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv'
url_2 = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv'
url_3 = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'


fecha = str(datetime.now().strftime("%d_%m_%y"))

nombre_museo= 'museo_' + fecha + '.csv'
nombre_cine= 'cine_' + fecha + '.csv'
nombre_bibloteca = 'bibloteca_' + fecha + '.csv'



def solicitud_web_museo():

    res = requests.get(url_1)

    if res.status_code == 200:
        open (nombre_museo, 'wb').write(res.content) # Wb contenido binario 

    else:
      print("Descarga no realizada")


def solicitud_web_cine():

    res = requests.get(url_2)

    if res.status_code == 200:
        open (nombre_cine, 'wb').write(res.content) # Wb contenido binario 
    else:
      print("Descarga no realizada")


def solicitud_web_bibloteca():

    res = requests.get(url_3)

    if res.status_code == 200:
        open (nombre_bibloteca, 'wb').write(res.content) # Wb contenido binario 
    else:
      print("Descarga no realizada")


    
    