#Importamos sqlite3 para poder trabajar con bases de Datos de manera mas efectiva.
import sqlite3
import FuncionesMenu as FMenus
import os

def AñadirCanciones(lector,database):#Funcion para añadir canciones a la tabla canciones
    while True:
        try:
            a = input("Digite el codigo de la nueva cancion: ")
            b = input("Digite el nombre de la nueva cancion: ")
            c = input("Digite el genero de la nueva cancion: ")
            d = input("Digite el album de la nueva cancion: ")
            e = input("Digite el interprete de la nueva cancion: ")

            nueva_cancion = (a,b,c,d,e) #se crea esta tupla con todos las caracteristicas de la cancion ingresada
            lector.execute("INSERT INTO CANCIONES(CODIGO, NOMBRE, GENERO, ALBUM, INTERPRETE) VALUES(?,?,?,?,?)",nueva_cancion)
            database.commit()
            break
        except: #se activa cuando ingresa datos erroneos o intenta ingresar una cancion que ya existe.
            print("Ocurrido un error, por favor digite denuevo.")
    os.system('cls')

def BorrarCanciones(lector,database):# funcion que borra la cancion de la base de datos y de la lista de canciones del cliente
    y = input("Digite el codigo de la cancion que desea eliminar: ")
    while True:
        try:
            lector.execute("DELETE FROM CANCIONES WHERE CODIGO = ?",(y,))

            break
        except:
            print("Codigo no existente.")
    database.commit()
    os.system('cls')


def ModificarCanciones(lector,database):# funcion que permite elegir que atributo de una cancion existente desea cambiar
    cod = input("Digite el codigo de la cancion que desee modificar: ")
    lector.execute("SELECT * FROM CANCIONES WHERE CODIGO = ?",(cod,))
    y = lector.fetchall()
    x = 0
    w = 5
    k = 0
    for i in range(len(y)): #separa por | las canciones mostradas
        for j in y[i]:
            if (k == w):
                k = 0
                print("")
            print("|",end=" ")
            print(j,end=" ")
            print("|",end=" ")
            k = k + 1
    print("")
    FMenus.MenuCanciones()
    while True:
        try:
            a = input("¿Que desea modificar de la cancion?")
            break
        except:
            print("Opcion no valida, digite denuevo.")
    if (a == '1'):
        b = input("Digite el nuevo nombre: ")
        lector.execute("UPDATE CANCIONES SET NOMBRE = ? WHERE CODIGO = ? ",(b,cod,))
    if (a == '2'):
        b = input("Digite el nuevo genero: ")
        lector.execute("UPDATE CANCIONES SET GENERO = ? WHERE CODIGO = ? ",(b,cod,))
        
    if (a == '3'):
        b = input("Digite el nuevo album: ")
        lector.execute("UPDATE CANCIONES SET ALBUM = ? WHERE CODIGO = ? ",(b,cod,))
    
    if (a == '4'):
        b = input("Digite el nuevo interprete: ")
        lector.execute("UPDATE CANCIONES SET INTERPRETE = ? WHERE CODIGO = ? ",(b,cod,))
    if (a == '5'):
        pass
    database.commit()
    os.system('cls')

def ConsultarCanciones(lector,database):# puede buscar las canciones por uno de sus atributos
    print('''
    1.) Consulta de todo el modulo.
    2.) Consulta especifica por uno de los campos.
    ''')
    print("")
    m=int(input("Elija el tipo de consulta que desea realizar:"))
    if(m == 1):
        Mostrar(lector,"CANCIONES")
    if(m == 2):
        
        print("")
        print('''
        1.) codigo
        2.) nombre
        3.) genero
        4.) album
        5.) interprete
        ''')
        print("")
        d = []
        a = int(input("Digite la opcion de busqueda: "))
        if(a == 1):
            c = input("Digite el codigo de la cancion: ")
            lector.execute("SELECT * FROM CANCIONES WHERE CODIGO = ?",(c,))
            d = lector.fetchall()
            FMenus.ImprimirTabla("CANCIONES")

        if (a == 2):
            c = input("Digite el nombre de la cancion: ")
            lector.execute("SELECT * FROM CANCIONES WHERE NOMBRE = ?",(c,))
            d = lector.fetchall()
            FMenus.ImprimirTabla("CANCIONES")

        if (a == 3):
            c = input("Digite el genero de la cancion: ")
            lector.execute("SELECT * FROM CANCIONES WHERE GENERO = ?",(c,))
            d = lector.fetchall()
            FMenus.ImprimirTabla("CANCIONES")

        if (a == 4):
            c = input("Digite el album de la cancion: ")
            lector.execute("SELECT * FROM CANCIONES WHERE ALBUM = ?",(c,))
            d = lector.fetchall()
            FMenus.ImprimirTabla("CANCIONES")

        if (a == 5):
            c = input("Digite el interprete de la cancion: ")
            lector.execute("SELECT * FROM CANCIONES WHERE INTERPRETE = ?",(c,))
            d = lector.fetchall()
            FMenus.ImprimirTabla("CANCIONES")

        b = 7
        k = 0
        for i in range(len(d)):
            for j in d[i]:
                if (k == b):
                    k = 0
                    print("")
                print("|",end=" ")
                print(j,end=" ")
                print("|",end=" ")
                k = k + 1
        wait = input()
        os.system('cls')

    
########################################################################

def AñadirClientes(lector,database): #añade clientes, es necesario poner los 8 datos
    while True:
        try:
            a = input("Digite la cedula del nuevo/a cliente: ")
            b = input("Digite el nombre del nuevo/a cliente: ")
            c = input("Digite el apellido del nuevo/a cliente: ")
            d = input("Digite el pais del nuevo/a cliente: ")
            e = input("Digite la ciudad del nuevo/a cliente: ")
            f = input("Digite el numero celular del nuevo/a cliente: ")
            g = int(input("Digite la fecha de pago (ddmmaa): "))
            h = input("Digite el numero de tarjeta de credito del nuevo/a cliente: ")
            i = "pagado" #cuando se añade un nuevo cliente se presume que por lo menos ha pagado el primer mes
            j = input ("Digite el codigo del plan al que se suscribe este nuevo/a cliente: ")

            nuevo_cliente = (a,b,c,d,e,f,g,h,i,j) #se crea esta tupla con todos las caracteristicas del cliente ingresado
            lector.execute("INSERT INTO CLIENTES(CEDULA, NOMBRE, APELLIDO, PAIS, CIUDAD,  CELULAR,  FECHA,  NTARJETA, ESTADO,IDPLAN) VALUES(?,?,?,?,?,?,?,?,?,?)",nuevo_cliente)
            database.commit()
            break
        except:
            print("Ocurrido un error, por favor digite denuevo.")
    os.system('cls')

def BorrarClientes(lector,database): # borra un cliente luego de ingresar su cedula.
    y = input("Digite la cedula del cliente que desea eliminar: ")
    while True:
        try:
            lector.execute("DELETE FROM CLIENTES WHERE CEDULA = ?",(y,))
            break
        except:
            print("Cedula no existente.")
    database.commit()
    os.system('cls')


def ModificarClientes(lector,database): #ingresa la cedula y luego pregunta que atributo del cliente desea modificar.
    ide = input("Digite el # de identificacion del cliente que desee modificar: ")
    lector.execute("SELECT * FROM CLIENTES WHERE CEDULA = ?",(ide,))
    y = lector.fetchall()
    x = 0
    w = 9
    k = 0
    for i in range(len(y)):
        for j in y[i]:
            if (k == w):
                k = 0
                print("")
            print("|",end=" ")
            print(j,end=" ")
            print("|",end=" ")
            k = k + 1
    print("")
    FMenus.MenuClientes()
    while True:
        try:
            a = input("¿Que desea modificar del cliente?")
            break
        except:
            print("Opcion no valida, digite denuevo.")
    if (a == '1'):
        b = input("Digite el nuevo nombre: ")
        lector.execute("UPDATE CLIENTES SET NOMBRE = ? WHERE CEDULA = ? ",(b,ide,))
    if (a == '2'):
        b = input("Digite el nuevo apellido: ")
        lector.execute("UPDATE CLIENTES SET APELLIDO = ? WHERE CEDULA = ? ",(b,ide,))        
    if (a == '3'):
        b = input("Digite el nuevo pais: ")
        lector.execute("UPDATE CLIENTES SET PAIS = ? WHERE CEDULA = ? ",(b,ide,))    
    if (a == '4'):
        b = input("Digite el nuevo ciudad: ")
        lector.execute("UPDATE CLIENTES SET CIUDAD = ? WHERE CEDULA = ? ",(b,ide,))
    if (a == '5'):
        b = input("Digite el nuevo numero celular: ")
        lector.execute("UPDATE CLIENTES SET  CELULAR = ? WHERE CEDULA = ? ",(b,ide,))
    if (a == '6'):
        b = int(input("Digite la nuevo fecha de pago (ddmmaa):  "))
        lector.execute("UPDATE CLIENTES SET FECHA = ? WHERE CEDULA = ? ",(b,ide,))
    if (a == '7'):
        b = input("Digite el nuevo tarjeta de credito: ")
        lector.execute("UPDATE CLIENTES SET NTARJETA = ? WHERE CEDULA = ? ",(b,ide,))
    if (a == '8'):
        b = input("digite el estado de pago del cliente [pagado/no pagado]: ")
        lector.execute("UPDATE CLIENTES SET ESTADO = ? WHERE CEDULA = ? ",(b,ide,))

    if (a == '9'):
        pass
    database.commit()
    os.system('cls')

def ConsultarClientes(lector,database): #consultar clientes dependiendo de la opcion de busqueda.
    print('''
    1.) Consulta de todo el modulo.
    2.) Consulta especifica por uno de los campos.
    ''')
    print("")
    m=int(input("Elija el tipo de consulta que desea realizar:"))
    if(m == 1):
        Mostrar(lector,"CLIENTES")
    if(m == 2):
        print("")
        print('''
        1.) cedula
        2.) nombre
        3.) apellido
        4.) pais
        5.) ciudad
        6.) # celular
        7.) fecha pago (ddmmaa)
        8.) Tarjeta credito
        9.) estado cuenta
        ''')
        print("")
        d = []
        a = int(input("Digite la opcion de busqueda: "))
        if(a == 1):
            c = input("Digite la cedula del/a cliente: ")
            lector.execute("SELECT * FROM CLIENTES WHERE CEDULA = ?",(c,))
            d = lector.fetchall()
            FMenus.ImprimirTabla("CLIENTES")

        if (a == 2):
            c = input("Digite el nombre del/a cliente: ")
            lector.execute("SELECT * FROM CLIENTES WHERE NOMBRE = ?",(c,))
            d = lector.fetchall()
            FMenus.ImprimirTabla("CLIENTES")

        if (a == 3):
            c = input("Digite el apellido del/a cliente: ")
            lector.execute("SELECT * FROM CLIENTES WHERE APELLIDO = ?",(c,))
            d = lector.fetchall()
            FMenus.ImprimirTabla("CLIENTES")

        if (a == 4):
            c = int(input("Digite el pais del/a cliente: "))
            lector.execute("SELECT * FROM CLIENTES WHERE PAIS = ?",(c,))
            d = lector.fetchall()
            FMenus.ImprimirTabla("CLIENTES")

        if (a == 5):
            c = int(input("Digite la ciudad del/a cliente: "))
            lector.execute("SELECT * FROM CLIENTES WHERE CIUDAD = ?",(c,))
            d = lector.fetchall()
            FMenus.ImprimirTabla("CLIENTES")

        if(a == 6):
            c = int(input("Digite el numero celular del/a cliente: "))
            lector.execute("SELECT * FROM CLIENTES WHERE CELULAR = ?",(c,))
            d = lector.fetchall()
            FMenus.ImprimirTabla("CLIENTES")

        if(a == 7):
            c = int(input("Digite la fecha del/a cliente(ddmmaa): "))
            lector.execute("SELECT * FROM CLIENTES WHERE FECHA = ?",(c,))
            d = lector.fetchall()
            FMenus.ImprimirTabla("CLIENTES")

        if(a == 8):
            c = input("Digite el numero de tarjeta del/a cliente: ")
            lector.execute("SELECT * FROM CLIENTES WHERE TARJETA = ?",(c,))
            d = lector.fetchall()
            FMenus.ImprimirTabla("CLIENTES")

        if(a == 9):
            c = input("Digite el estado de la cuenta del/a cliente [pagado/no pagado]: ")
            lector.execute("SELECT * FROM CLIENTES WHERE ESTADO = ?",(c,))
            d = lector.fetchall()
            FMenus.ImprimirTabla("CLIENTES")

        b = 7
        k = 0
        for i in range(len(d)):
            for j in d[i]:
                if (k == b):
                    k = 0
                    print("")
                print("|",end=" ")
                print(j,end=" ")
                print("|",end=" ")
                k = k + 1
    wait = input()
    os.system('cls')

#####################################################################################
def AñadirPlanes(lector,database): #funcion para añadir planes disponibles para clientes.
    while True:
        try:
            a = input("Digite el codigo del nuevo plan: ")
            b = input("Digite el nombre del nuevo plan: ")
            c = int(input("Digite el valor del nuevo plan: "))
            d = int(input("Digite el la cantidad de canciones disponibles en del nuevo plan: "))

            nuevo_plan = (a,b,c,d) #se crea esta tupla con todos las caracteristicas del plan
            lector.execute("INSERT INTO PLANES(CODIGO, NOMBRE, VALOR, CANTIDAD) VALUES(?,?,?,?)",nuevo_plan)
            database.commit()
            break
        except:
            print("Ocurrido un error, por favor digite denuevo.")
    os.system('cls')

def BorrarPlanes(lector,database):
    y = input("Digite el codigo del plan que desea eliminar: ")
    while True:
        try:
            lector.execute("DELETE FROM PLANES WHERE CODIGO = ?",(y,))
            break
        except:
            print("Codigo no existente.")
    database.commit()
    os.system('cls')

def ModificarPlanes(lector,database):
    cod = input("Digite el codigo del plan que desee modificar: ")
    lector.execute("SELECT * FROM PLANES WHERE CODIGO = ?",(cod,))
    y = lector.fetchall()
    x = 0
    w = 4
    k = 0
    for i in range(len(y)):
        for j in y[i]:
            if (k == w):
                k = 0
                print("")
            print("|",end=" ")
            print(j,end=" ")
            print("|",end=" ")
            k = k + 1
    print("")
    FMenus.MenuPlanes()
    while True:
        try:
            a = input("¿Que desea modificar del plan?")
            break
        except:
            print("Opcion no valida, digite denuevo.")
    if (a == '1'):
        b = input("Digite el nuevo nombre  del plan: ")
        lector.execute("UPDATE PLANES SET NOMBRE = ? WHERE CODIGO = ? ",(b,cod,))
    if (a == '2'):
        b = int(input("Digite el valor nuevo  del plan: "))
        lector.execute("UPDATE PLANES SET VALOR = ? WHERE CODIGO = ? ",(b,cod,))
        
    if (a == '3'):
        b = int(input("Digite ela nueva cantidad de canciones del plan: "))
        lector.execute("UPDATE PLANES SET CANTIDAD = ? WHERE CODIGO = ? ",(b,cod,))
    
    if (a == '4'):
        pass
    database.commit()
    os.system('cls')

def ConsultarPlanes(lector,database):
    print('''
    1.) Consulta de todo el modulo.
    2.) Consulta especifica por uno de los campos.
    ''')
    print("")
    m=int(input("Elija el tipo de consulta que desea realizar:"))
    if(m == 1):
        Mostrar(lector,"PLANES")
    if(m == 2):
        print("")
        print('''
        1.) Codigo
        2.) Nombre
        3.) Valor
        4.) Cantidad 
        ''')
        print("")
        d = []
        a = int(input("Digite la opcion de busqueda: "))
        if(a == 1):
            c = input("Digite el codigo del plan: ")
            lector.execute("SELECT * FROM PLANES WHERE CODIGO = ?",(c,))
            d = lector.fetchall()
            FMenus.ImprimirTabla("PLANES")

        if (a == 2):
            c = input("Digite el nombre del plan: ")
            lector.execute("SELECT * FROM PLANES WHERE NOMBRE = ?",(c,))
            d = lector.fetchall()
            FMenus.ImprimirTabla("PLANES")

        if (a == 3):
            c = int(input("Digite el valor del plan: "))
            lector.execute("SELECT * FROM PLANES WHERE VALOR = ?",(c,))
            d = lector.fetchall()
            FMenus.ImprimirTabla("PLANES")

        if (a == 4):
            c = int(input("Digite el cantidad del plan: "))
            lector.execute("SELECT * FROM PLANES WHERE CANTIDAD = ?",(c,))
            d = lector.fetchall()
            FMenus.ImprimirTabla("PLANES")

        b = 6
        k = 0
        for i in range(len(d)):
            for j in d[i]:
                if (k == b):
                    k = 0
                    print("")
                print("|",end=" ")
                print(j,end=" ")
                print("|",end=" ")
                k = k + 1
    wait = input()
    os.system('cls')
    
#####################################################################

def AñadirLista(lector,database): #añade canciones a la tabla canciones cliente, con el id del cliente y el id de la cancion
    while True:
        try:
            a = input("Digite la cedula del cliente: ")
            b = input("Digite el codigo de la cancion que desea agregar: ")   
            nueva_CanCliente = (a,b) 
            lector.execute("INSERT INTO LISTA(IDCLIENTE, IDCANCION) VALUES(?,?)",nueva_CanCliente)
            database.commit()
            break
        except:
            print("Ocurrido un error, por favor digite denuevo.")
    os.system('cls')

    

def BorrarCancionesLista(lector,database): #borra canciones de la lista luego de insertar el id de la cancion
    y = input("Digite el codigo de la cancion que desea eliminar: ")
    while True:
        try:
            lector.execute("DELETE FROM LISTA WHERE IDCANCION = ?",(y,))
            break
        except:
            print("Codigo no existente1.")
    database.commit()
    os.system('cls')

#def BuscarCancionesCliente():
    
def Mostrar(lector,tabla): # esta funcion recibe una tabla y la muestra en el orden que seleccione
    print("")
    b = 0
    c = "0"
    if (tabla == "CANCIONES"):
        b = 5
        print("")
        print('''
        1.) codigo
        2.) nombre
        3.) genero
        4.) album
        5.) interprete
        ''')
        d = input("Digite el orden que deseaa: ")
        if (d == '1'):
            c = "CODIGO"
        if (d == '2'):
            c = "NOMBRE"
        if (d == '3'):
            c = "GENERO"
        if (d == '4'):
            c = "ALBUM"
        if (d == '5'):
            c = "INTERPRETE"
        FMenus.ImprimirTabla(tabla)
        lector.execute("SELECT * FROM CANCIONES ORDER BY %s"%(c))
        
    elif (tabla == "CLIENTES"):
        b = 10
        print('''
        1.) cedula
        2.) nombre
        3.) apellido
        4.) pais
        5.) ciudad
        6.) # celular
        7.) fecha pago (ddmmaa)
        8.) Tarjeta credito
        9.) estado cuenta
        10.) id del plan
        ''')
        print("")
        d = input("Digite el orden que desea:")
        if (d == '1'):
            c = "CEDULA"
        if (d == '2'):
            c = "NOMBRE"
        if (d == '3'):
            c = "APELLIDO"
        if (d == '4'):
            c = "PAIS"
        if (d == '5'):
            c = "CIUDAD"
        if (d == '6'):
            c = "CELULAR"
        if (d == '7'):
            c = "FECHA"
        if (d == '8'):
            c = "NTARJETA"
        if (d == '9'):
            c = "ESTADO"
        if (d == '10'):
            c = "IDPLAN"
        FMenus.ImprimirTabla(tabla)
        lector.execute("SELECT * FROM CLIENTES ORDER BY %s"%(c))
    elif (tabla == "PLANES"):
        b = 4
        print('''
        1.) Codigo
        2.) Nombre
        3.) Valor
        4.) Cantidad 
        ''')
        print("")
        d = input("Digite el orden que desea:")
        if (d == '1'):
            c = "CODIGO"
        if (d == '2'):
            c = "NOMBRE"
        if (d == '3'):
            c = "VALOR"
        if (d == '4'):
            c = "CANTIDAD"
        FMenus.ImprimirTabla(tabla)
        lector.execute("SELECT * FROM PLANES ORDER BY %s"%(c))
    elif (tabla == "LISTA"):
        b = 2
        print('''
        1.) idcliente
        2.) idcancion
        ''')
        print("")
        d = input("Digite el orden que desea:")
        if (d == '1'):
            c = "IDCLIENTE"
        if (d == '2'):
            c = "IDCANCION"
    
        FMenus.ImprimirTabla(tabla)
        lector.execute("SELECT * FROM LISTA ORDER BY %s"%(c))
    a = lector.fetchall()
    k = 0
    for i in range(len(a)):
        for j in a[i]:
            if (k == b):
                k = 0
                print("")
            print("|",end=" ")
            print(j,end=" ")
            print("|",end=" ")
            k = k + 1
    
    wait = input()
    os.system('cls')
    
