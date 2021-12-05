import sqlite3
import FuncionesSQL as funciones
import FuncionesMenu as FMenus
import os

database = sqlite3.connect("labasededatospooparcial.db")

lector = database.cursor()

try:
    lector.execute("CREATE TABLE CANCIONES (CODIGO INTEGER(10) PRIMARY KEY,NOMBRE VARCHAR(30),GENERO VARCHAR(20),ALBUM VARCHAR(30), INTERPRETE VARCHAR(25))")
except:
    pass

try:
    lector.execute("CREATE TABLE CLIENTES (CEDULA INTEGER(10) PRIMARY KEY,NOMBRE VARCHAR(25),APELLIDO VARCHAR(25), PAIS VARCHAR(20), CIUDAD VARCHAR(20),CELULAR INTEGER(10),FECHA INTEGER(7),NTARJETA INTEGER(10),ESTADO INTEGER (8))")
except:
    pass

try:
    lector.execute("CREATE TABLE PLANES (CODIGO INTEGER(9) PRIMARY KEY, NOMBRE VARCHAR(30), VALOR INTEGER(6), CANTIDAD INTEGER(6))")
except:
    pass
condition = True
os.system('cls')
while condition ==  True:

    opcion =FMenus.Menu()

    if (opcion == 1):

        opcion1 = FMenus.MenuOpciones()

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
                print("Opcion no valida.")

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
                print("Opcion no valida.")

    if (opcion == 3):

        opcion1 = FMenus.MenuOpciones()

        if (opcion1 == 1):
                funciones.AñadirPlanes(lector,database)
        elif (opcion1 == 2):
                funciones.BorrarPlanes(lector,database)
        elif (opcion1 == 3):
                funciones.ModificarPlanes(lector,database)
        elif (opcion1 == 4):
                funciones.BuscarPlanes(lector,database)
        elif (opcion1 == 5):
                pass
        else:
                print("Opcion no valida.")

    elif (opcion == 6):
        condition =(FMenus.Salir)

    else:
        print("")

    

database.commit()
database.close()
