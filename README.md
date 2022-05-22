En este proyecto encontraran datos desde
3 fuentes distintas para popular una base de datos SQL con información cultural
sobre bibliotecas, museos y salas de cines argentinos.


Requerimientos: Libreria python a utilizar leer requirements.txt, las mismas se haran con el comando pip install en el entorno virtual(se debera crear con anterioridad(ver Entorno virtual))

Entorno virtual: 

    Se debera crear un entorno virtual en el sistema operativo a utilizar.
    
     >>>Modo de creacion

        Windows:
        C:\>python -m venv c:\ruta\al\entorno\virtual
    
        En macOS y Linux:
        $ python -m venv ruta/al/entorno/virtual

     >>>Activar un entorno virtual
        
        En Windows:
        C:\>c:\ruta\al\entorno\virtual\scripts\activate.bat
        
        En macOS y Linux:
        $ source ruta/al/entorno/virtual/bin/activate
        Sea cual sea nuestro sistema operativo sabremos que el entorno virtual se ha activado porque su nombre aparece entre paréntesis delante del promt.

     >>>Desactivar un entorno virtual
        Este comando es idéntico para Windows, macOS y Linux:

        $ deactivate

     >>>Eliminar un entorno virtual
   
        En Windows:
        C:\>rmdir c:\ruta\al\entorno\virtual /s

        En macOS y Linux:
        $ rm -rf ruta/al/entorno/virtual

        Eliminar un entorno virtual es tan sencillo como eliminar la carpeta que lo contiene. Por ello, esta operación también se puede realizar desde el correspondiente administrador de archivos.

Coneccion a base de datos: Se debera generar un archivo .env para realizar la conección a la base de datos. Un archivo .env es un archivo de texto donde se definen una serie de variables de entorno a las cuales les asignamos un valor y que se agrega en el directorio raíz de un proyecto.