
import pandas as pd

from datetime import datetime

from app.museo import categoria_provincia_museo

fecha = str(datetime.now().strftime("%d_%m_%y"))
nombre= 'bibloteca_' + fecha + '.csv'

def categoria_bibloteca():

    data = pd.read_csv('C:\\Users\\WalterPc\\Documents\\Alkemy\\' + nombre) # archivo .csv a analizar. Index_col =0 eliminamos Unnamed: 0 del dataframe

    freq = data.groupby(['Categoría']).size()

    data=freq.to_csv('archivo.csv')

    data = pd.read_csv('archivo.csv', converters={'string':str})

    data1=data.rename(columns={'0':'Total'})

    data2=data1.to_csv('archivo.csv', index=0)

def provincia_categoria_bibloteca():

    data = pd.read_csv('C:\\Users\\WalterPc\\Documents\\Alkemy\\' + nombre) # archivo .csv a analizar. Index_col =0 eliminamos Unnamed: 0 del dataframe

    freq = data.groupby(['Provincia', 'Categoría']).size()

    data=freq.to_csv('archivo.csv')

    data = pd.read_csv('archivo.csv', converters={'string':str})

    data1=data.rename(columns={'0':'Total'})

    data2=data1.to_csv('archivo.csv', index=0)

def fuente_bibloteca():

  data = pd.read_csv('C:\\Users\\WalterPc\\Documents\\Alkemy\\' + nombre) # archivo .csv a analizar. Index_col =0 eliminamos Unnamed: 0 del dataframe

  freq = data.groupby(['Categoría','Fuente']).size()

  data=freq.to_csv('archivo.csv')

  data = pd.read_csv('archivo.csv', converters={'string':str})

  data1=data.rename(columns={'0':'Total'})

  data2=data1.to_csv('archivo.csv', index=0)

def salida_bibloteca():

    data = pd.read_csv('C:\\Users\\WalterPc\\Documents\\Alkemy\\' + nombre) # archivo .csv a analizar. Index_col =0 eliminamos Unnamed: 0 del dataframe

    df = data.fillna('SIN DATOS')

    freq = df.groupby(['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'Categoría', 'Provincia', 'Localidad', 'Nombre', 'Domicilio', 'CP', 'Teléfono', 'Mail', 'Web']).size()

    
    data=freq.to_csv('archivo.csv')

    data = pd.read_csv('archivo.csv', converters={'string':str})

    data2=data.drop(columns=['0'])
    data3=data2.to_csv('archivo.csv', index=0)

'''
if __name__ == "__main__":
 
  categoria()
  cantidades()
  fuente()
  cantidades()
  categoria_provincia()
  cantidades()
  biblo()
  salidas()
'''

