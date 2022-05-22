
import pandas as pd

from datetime import datetime

fecha = str(datetime.now().strftime("%d_%m_%y"))
nombre= 'museo_' + fecha + '.csv'


def fuente_museo():

    data = pd.read_csv('C:\\Users\\WalterPc\\Documents\\Alkemy\\' + nombre) # archivo .csv a analizar. Index_col =0 eliminamos Unnamed: 0 del dataframe

    freq = data.groupby(['categoria', 'fuente']).size()

    data=freq.to_csv('archivo.csv')

    data = pd.read_csv('archivo.csv', converters={'string':str})

    data1=data.rename(columns={'0':'Total','categoria':'Categoría', 'fuente':'Fuente'})

    data2=data1.to_csv('archivo.csv', index=0)

def categoria_provincia_museo():
    
    data = pd.read_csv('C:\\Users\\WalterPc\\Documents\\Alkemy\\' + nombre) # archivo .csv a analizar. Index_col =0 eliminamos Unnamed: 0 del dataframe

    freq = data.groupby(['provincia', 'categoria']).size()

    data=freq.to_csv('archivo.csv')

    data = pd.read_csv('archivo.csv', converters={'string':str})

    data1=data.rename(columns={'0':'Total', 'provincia': 'Provincia', 'categoria': 'Categoría','fuente':'Fuente' })

    data2=data1.to_csv('archivo.csv', index=0)

def categoria_museo():

    data = pd.read_csv('C:\\Users\\WalterPc\\Documents\\Alkemy\\' + nombre) # archivo .csv a analizar. Index_col =0 eliminamos Unnamed: 0 del dataframe

    freq = data.groupby(['categoria']).size()

    data=freq.to_csv('archivo.csv')

    data = pd.read_csv('archivo.csv', converters={'string':str})

    data1=data.rename(columns={'0':'Total','categoria':'Categoría'})

    data2=data1.to_csv('archivo.csv', index=0)

def salida_museo():

    data = pd.read_csv('C:\\Users\\WalterPc\\Documents\\Alkemy\\' + nombre) # archivo .csv a analizar. Index_col =0 eliminamos Unnamed: 0 del dataframe

    freq = data.groupby(['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'categoria', 'provincia',
                        'localidad', 'nombre', 'direccion', 'CP', 'telefono', 'Mail', 'Web']).size()

    data=freq.to_csv('archivo.csv')

    data = pd.read_csv('archivo.csv', converters={'string':str})

    data1=data.rename(columns={'localidad':'Localidad', 'categoria':'Categoría', 'provincia':'Provincia', 'nombre':'Nombre', 'direccion':'Domicilio', 'telefono':'Teléfono'})
    data2=data1.drop(columns=['0'])
    data3=data2.to_csv('archivo.csv', index=0)

