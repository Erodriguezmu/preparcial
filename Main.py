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

    opcion =FMenus.Menu() #llama a la primera funcion de menu que usaremos 

    if (opcion == 1):
        objCancion = funciones.Cancion(database)
        opcion1 = FMenus.MenuOpcionesCanciones() #el menu opciones tiene las mismas 4 opciones para cada una de las tablas (añadir,borrar,modificar,consultar)

        if (opcion1 == 1):
                objCancion.AñadirCanciones()
        elif (opcion1 == 2):
                objCancion.ModificarCanciones()
        elif (opcion1 == 3):
                objCancion.ConsultarCanciones()
        elif (opcion1 == 4):
                pass
        else:
                print("Opcion no valida.1")

    if (opcion == 2):
        objCliente = funciones.Cliente(database)
        opcion1 = FMenus.MenuOpciones()

        if (opcion1 == 1):
                objCliente.AñadirClientes()
        elif (opcion1 == 2):
                objCliente.BorrarClientes()
        elif (opcion1 == 3):
                objCliente.ModificarClientes()
        elif (opcion1 == 4):
                objCliente.ConsultarClientes()
        elif (opcion1 == 5):
                pass
        else:
                print("Opcion no valida.2")

    if (opcion == 3):
        objPlan = funciones.Plan(database)
        opcion1 = FMenus.MenuOpciones()

        if (opcion1 == 1):
                objPlan.AñadirPlanes()
        elif (opcion1 == 2):
                objPlan.BorrarPlanes()
        elif (opcion1 == 3):
                objPlan.ModificarPlanes()
        elif (opcion1 == 4):
                objPlan.ConsultarPlanes()
        elif (opcion1 == 5):
                pass
        else:
                print("Opcion no valida.3")

    if (opcion == 4):
        objLista = funciones.Lista(database)
        opcion1 = FMenus.MenuLista() #la lista tiene un menu diferente sin la opcion modificar puesto que solo admite añadir,borrar y consultar.

        if (opcion1 == 1):
                objLista.AñadirLista()
        elif (opcion1 == 2):
                objLista.BorrarCancionesLista()
        elif (opcion1 == 3):
                objLista.ConsultarLista()
        elif (opcion1 == 4):
                objLista.ReproducirCancion()

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
