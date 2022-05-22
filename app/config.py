import pandas as pd

import logging

from decouple import config

from sqlalchemy import create_engine

def salidas():

    RUTA_CSV = 'C:\\Users\\WalterPc\\Documents\\Alkemy\\'
    nombre = 'archivo.csv'
    archivo =  nombre


    engine = create_engine(conection())
    archivocsv=pd.read_csv(RUTA_CSV+archivo, sep=',')
    archivocsv.to_sql('salidas', engine, if_exists='append', dtype= None, index=False, method= None)

def cantidades():

    RUTA_CSV = 'C:\\Users\\WalterPc\\Documents\\Alkemy\\'
    nombre = 'archivo.csv'
    archivo =  nombre


    engine = create_engine(conection())
    archivocsv=pd.read_csv(RUTA_CSV+archivo, sep=',')
    archivocsv.to_sql('cantidades', engine, if_exists='append', dtype= None, index=False, method= None)

def cantidad1():

    RUTA_CSV = 'C:\\Users\\WalterPc\\Documents\\Alkemy\\'
    nombre = 'cantidad.csv'
    archivo =  nombre


    engine = create_engine(conection())
    archivocsv=pd.read_csv(RUTA_CSV+archivo, sep=',')
    archivocsv.to_sql('cines', engine, if_exists='append', dtype= None, index=False, method= None)

logging.basicConfig(
level=logging.INFO    
    )

def conection():

    user=config('USUARIO_PSQL')
    contraseña=config('CONTRASEÑA_PSQL')
    host=config('PSQL_HOST')
    db=config('BASEDEDATOS_PSQL')

    databaseconec= f'postgresql://{user}:{contraseña}@{host}/{db}'

    return databaseconec


