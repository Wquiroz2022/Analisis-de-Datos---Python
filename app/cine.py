import pandas as pd

from datetime import datetime


fecha = str(datetime.now().strftime("%d_%m_%y"))
nombre= 'cine_' + fecha + '.csv'

def salida_cine():

    data = pd.read_csv('C:\\Users\\WalterPc\\Documents\\Alkemy\\' + nombre) # archivo .csv a analizar. Index_col =0 eliminamos Unnamed: 0 del dataframe

    freq = data.groupby(['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'Categoría', 'Provincia',
                        'Localidad', 'Nombre', 'Dirección', 'CP', 'Teléfono', 'Mail', 'Web']).size()

    data=freq.to_csv('archivo.csv')

    data = pd.read_csv('archivo.csv', converters={'string':str})

    data1=data.rename(columns={'Dirección':'Domicilio'})
    data2=data1.drop(columns=['0'])
    data3=data2.to_csv('archivo.csv', index=0)

def provincia_categoria_cine():

    data = pd.read_csv(nombre) # archivo .csv a analizar. Index_col =0 eliminamos Unnamed: 0 del dataframe

    freq = data.groupby(['Provincia', 'Categoría']).size()

    data=freq.to_csv('archivo.csv')

    data = pd.read_csv('archivo.csv', converters={'string':str})

    data1=data.rename(columns={'0':'Total'})

    data2=data1.to_csv('archivo.csv', index=0)

def fuente_cine():

    data = pd.read_csv(nombre) # archivo .csv a analizar. Index_col =0 eliminamos Unnamed: 0 del dataframe

    freq = data.groupby(['Categoría','Fuente']).size()

    data=freq.to_csv('archivo.csv')

    data = pd.read_csv('archivo.csv', converters={'string':str})

    data1=data.rename(columns={'0':'Total'})

    data2=data1.to_csv('archivo.csv', index=0)

def categoria_cine():

    data = pd.read_csv('C:\\Users\\WalterPc\\Documents\\Alkemy\\' + nombre) # archivo .csv a analizar. Index_col =0 eliminamos Unnamed: 0 del dataframe

    freq = data.groupby(['Categoría']).size()

    data=freq.to_csv('archivo.csv')

    data = pd.read_csv('archivo.csv', converters={'string':str})

    data1=data.rename(columns={'0':'Total'})

    data2=data1.to_csv('archivo.csv', index=0)

def cantida():

    fecha = str(datetime.now().strftime("%d_%m_%y"))
    nombre= 'cine_' + fecha + '.csv'

    data = pd.read_csv('C:\\Users\\WalterPc\\Documents\\Alkemy\\'+ nombre) # archivo .csv a analizar. Index_col =0 eliminamos Unnamed: 0 del dataframe

    data.replace(to_replace='SI', value= '1', inplace=True)

    data.replace(to_replace='si', value= '1', inplace=True)
    
    freq = data.groupby(['Provincia', 'Pantallas', 'Butacas', 'espacio_INCAA']).size()

    data=freq.to_csv('archivo.csv')

    data = pd.read_csv('archivo.csv', converters={'string':str})

    data2=data.rename(columns={'0':'Total'})

    data2.to_csv('archivo.csv', index=0)  

def nuevo_archivo():

    data4=pd.read_csv('archivo.csv')

    LL=data4.groupby("Provincia")["Butacas"].sum()
    LL.to_csv('Butacas.csv')

    LLL=data4.groupby("Provincia")["Pantallas"].sum()
    LLL.to_csv('Pantallas.csv')

    LLLL=data4.groupby("Provincia")["espacio_INCAA"].sum()
    LLLL.to_csv('Espacio_INCAA.csv')

def concat():

    nombre1= 'C:\\Users\\WalterPc\\Documents\\Alkemy\\Pantallas.csv'
    nombre2= 'C:\\Users\\WalterPc\\Documents\\Alkemy\\Butacas.csv'
    nombre3= 'C:\\Users\\WalterPc\\Documents\\Alkemy\\Espacio_INCAA.csv'


    dataFrame = pd.concat(
         map(pd.read_csv, [nombre1, nombre2, nombre3]), axis=1, ignore_index=True, )
         

    dataFrame.to_csv('cantidad.csv', index=0)

    dataFrame = pd.read_csv('cantidad.csv', index_col=0, converters={'string':str})

    data=dataFrame.drop(columns=['2', '4'])
    
    data.to_csv('cantidad.csv')

def renombrar():

    data2 =pd.read_csv('cantidad.csv', converters={'string':str})

    data3=data2.rename(columns={'0':'Provincia', '1':'Pantallas', '3':'Butacas', '5':'Espacios_INCAA'})

    data3.to_csv('cantidad.csv', index=0)
