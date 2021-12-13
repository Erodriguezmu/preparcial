import sqlite3
import smtplib, ssl #libreria para el envio de correo electronico y ssl para conexion segura
import FuncionesSQL as funciones
import FuncionesMenu as FMenus
import os

database = sqlite3.connect("labasededatospooparcial.db")

lector = database.cursor()
# Creacion de las tablas necesarias
try:
    
    lector.execute("CREATE TABLE CANCIONES (CODIGO CHAR(6) PRIMARY KEY,NOMBRE VARCHAR(30) not null,GENERO VARCHAR(20)not null,ALBUM VARCHAR(30)not null, INTERPRETE VARCHAR(25)not null)")
except:
    pass

try:
    
    lector.execute("CREATE TABLE CLIENTES (CEDULA CHAR(10) PRIMARY KEY,NOMBRE VARCHAR(25)not null,APELLIDO VARCHAR(25)not null, PAIS VARCHAR(20), CIUDAD VARCHAR(20),CELULAR CHAR(10),FECHA INTEGER(7),NTARJETA CHAR(10)not null,ESTADO VARCHAR (8)not null,IDPLAN CHAR(4) not null,CONSTRAINT FK_PLAN FOREIGN KEY (IDPLAN)REFERENCES PLANES(CODIGO))")
except:
    pass

try:
    
    lector.execute("CREATE TABLE PLANES (CODIGO CHAR(4) PRIMARY KEY, NOMBRE VARCHAR(30)not null, VALOR INTEGER(6)not null, CANTIDAD INTEGER(6)not null)")
except:
    pass


try:
    #la tabla lista es una tabla que posee dos llaves foraneas como llave primaria compuesta.
    lector.execute("CREATE TABLE LISTA (IDCLIENTE CHAR(10), IDCANCION CHAR(6),CONSTRAINT ID PRIMARY KEY (IDCLIENTE,IDCANCION),CONSTRAINT FK_CLIENTE FOREIGN KEY (IDCLIENTE)REFERENCES CLIENTES(CEDULA),CONSTRAINT FK_CANCION FOREIGN KEY (IDCANCION)REFERENCES CANCIONES(CODIGO) ON DELETE CASCADE ON UPDATE CASCADE)")
except:
    pass


condition = True
os.system('cls')
while condition ==  True:
#
    opcion =FMenus.Menu() #llama a la primera funcion de menu que usaremos 

    if (opcion == 1):

        opcion1 = FMenus.MenuOpciones() #el menu opciones tiene las mismas 4 opciones para cada una de las tablas (añadir,borrar,modificar,consultar)

        if (opcion1 == 1):
                funciones.AñadirCanciones(lector,database)
        elif (opcion1 == 2):
                funciones.BorrarCanciones(lector,database)
        elif (opcion1 == 3):
                funciones.ModificarCanciones(lector,database)
        elif (opcion1 == 4):
                funciones.ConsultarCanciones(lector,database)
        elif (opcion1 == 5):
                pass
        else:
                print("Opcion no valida.1")

    if (opcion == 2):

        opcion1 = FMenus.MenuOpciones()

        if (opcion1 == 1):
                funciones.AñadirClientes(lector,database)
        elif (opcion1 == 2):
                funciones.BorrarClientes(lector,database)
        elif (opcion1 == 3):
                funciones.ModificarClientes(lector,database)
        elif (opcion1 == 4):
                funciones.ConsultarClientes(lector,database)
        elif (opcion1 == 5):
                pass
        else:
                print("Opcion no valida.2")

    if (opcion == 3):

        opcion1 = FMenus.MenuOpciones()

        if (opcion1 == 1):
                funciones.AñadirPlanes(lector,database)
        elif (opcion1 == 2):
                funciones.BorrarPlanes(lector,database)
        elif (opcion1 == 3):
                funciones.ModificarPlanes(lector,database)
        elif (opcion1 == 4):
                funciones.ConsultarPlanes(lector,database)
        elif (opcion1 == 5):
                pass
        else:
                print("Opcion no valida.3")

    if (opcion == 4):

        opcion1 = FMenus.MenuLista() #la lista tiene un menu diferente sin la opcion modificar puesto que solo admite añadir,borrar y consultar.

        if (opcion1 == 1):
                funciones.AñadirLista(lector,database)
        elif (opcion1 == 2):
                funciones.BorrarCancionesLista(lector,database)
        elif (opcion1 == 3):
                funciones.ConsultarLista(lector,database)
        elif (opcion1 == 4):
                funciones.ReproducirCancion(lector,database)

        elif (opcion1 == 5):
                pass
        else:
                print("Opcion no valida.4")

    elif (opcion == 5):
        condition =(FMenus.Salir)

    else:
        print("")

    

database.commit()
database.close()
