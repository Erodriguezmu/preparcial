import sqlite3
import FuncionesSQL as funciones
import FuncionesGraficas as graficos
import os

database = sqlite3.connect("labasededatospooparcial.db.db")

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

try:
    lector.execute('''CREATE TABLE MATERIASDOC (CODIGO VARCHAR(9), NOMBRE VARCHAR(30), NOMDOC VARCHAR(56), 
    APDOC VARCHAR(24), ID VARCHAR(10), HORARIOINIT INTEGER(4), HORARIOEND INTEGER(4), DIAS VARCHAR(10), CUPOS INTEGER(3), GRUPO INTEGER(2)) ''')
except:
    pass

