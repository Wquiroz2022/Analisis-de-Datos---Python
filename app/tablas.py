from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from sqlalchemy import Column, Integer, String, DateTime

from app.config import conection

engine = create_engine(conection())

Base = declarative_base()

class Salida(Base):
    __tablename__= "salidas"

    id=Column(Integer(), primary_key=True )
    Cod_Loc= Column (Integer(), nullable=True)
    IdProvincia= Column(Integer(), nullable=True)
    IdDepartamento= Column(Integer(), nullable=True)
    Categoría=Column (String (200), nullable=True)
    Provincia=Column (String (200), nullable=True)
    Localidad=Column (String (200), nullable=True)
    Nombre=Column (String (200), nullable=True)
    Domicilio=Column (String (200), nullable=True)
    CP=Column (String (200), nullable=True)
    Teléfono=Column (String (200), nullable=True)
    Mail=Column (String (200), nullable=False, unique=False)
    Web= Column (String (200), nullable=False, unique=False)
    created_at= Column(DateTime(), default=datetime.now)

def __str__(self):
    return self.cod_localidad

class Cine(Base):
    __tablename__='cines'

    id= Column(Integer(), primary_key=True )
    Provincia =Column (String (200), nullable=True)
    Pantallas=Column(Integer(), nullable=True)
    Butacas=Column(Integer(), nullable=True)
    Espacios_INCAA=Column(Integer(), nullable=True)
    created_at = Column(DateTime(), default=datetime.now)

def __str__(self):
    return self.provincia

class cantidad(Base):
    __tablename__='cantidades'
    
    id = Column(Integer(), primary_key=True )
    Provincia=Column (String (100), nullable=True)
    Categoría= Column (String (100), nullable=True)
    Fuente=Column (String (100), nullable=True)
    Total= Column (Integer(), nullable=True )
    created_at = Column(DateTime(), default=datetime.now)

def __str__(self):
    return self.provincia

Session = sessionmaker(engine)
session = Session()

