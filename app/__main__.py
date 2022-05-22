from app import eliminar_archivo, solicitud_web_museo, solicitud_web_cine, solicitud_web_bibloteca

from app import logging, salidas, cantidades, cantidad1

from app import Salida, Cine, cantidad, Base, engine, session

from app import salida_cine, provincia_categoria_cine, fuente_cine, categoria_cine, cantida, nuevo_archivo, concat, renombrar

from app import fuente_museo, categoria_provincia_museo, categoria_museo, salida_museo

from app import categoria_bibloteca, provincia_categoria_bibloteca, fuente_bibloteca, salida_bibloteca

if __name__ == '__main__':

    logging.info('eliminando archivos CSV')
    eliminar_archivo() 
    logging.info('Descargando archivos')
    solicitud_web_museo()
    solicitud_web_cine()
    solicitud_web_bibloteca()
    logging.info('archivos descargados')
    logging.info('Creando tablas')
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    logging.info('Creacion finalizada')
    logging.info('Actualizando Base de datos')
    salida_cine()
    salidas()
    categoria_cine()
    cantidades()
    fuente_cine()
    cantidades()
    provincia_categoria_cine()
    cantidades()
    cantida()
    nuevo_archivo()
    concat()
    renombrar()
    cantidad1()
    salida_museo()
    salidas()
    categoria_museo()
    cantidades()
    fuente_museo()
    cantidades()
    categoria_provincia_museo()
    cantidades()
    salida_bibloteca()
    salidas()
    categoria_bibloteca()
    cantidades()
    fuente_bibloteca()
    cantidades()
    provincia_categoria_bibloteca()
    cantidades()
    logging.info('Base de datos Actualizada')