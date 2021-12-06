def Menu():
    print("Bienvenido, seleccione la operacion que desea realizar")
    print("1.) Canciones")
    print("2.) Clientes")
    print("3.) Planes")
    print("4.) Planes por cliente")
    print("5.) Salir")
    while True:
        try:
            opcion = int(input("Digite la opción: "))
            break
        except:
            print("Numero no valido, escoga denuevo.")
    return opcion

def MenuOpciones():
    print("Seleccione la operacion que desea realizar")
    print("1.) Añadir")
    print("2.) Eliminar")
    print("3.) Modificar")
    print("4.) Consultar")
    print("5.) Salir")

    while True:
        try:
            opcion = int(input("Digite la opción: "))
            break
        except:
            print("Numero no valido, escoga denuevo.")
    return opcion

def MenuLista():
    print("Seleccione la operacion que desea realizar")
    print("1.) Añadir")
    print("1.) Eliminar")
    print("2.) Modificar a mi lista")
    print("3.) consultar de mi lista")
    print("4.) Salir")
    while True:
        try:
            opcion = int(input("Digite la opción: "))
            break
        except:
            print("Numero no valido, escoga denuevo.")
    return opcion
    
    
def MenuCanciones():
    print("1.) Nombre")
    print("2.) Genero")
    print("3.) Album")
    print("4.) Interprete")
    print("5.) Cancelar")

def MenuClientes():
    print("1.) Nombre")
    print("2.) Apellido")
    print("3.) Pais")
    print("4.) Ciudad")
    print("5.) Celular")
    print("6.) Fecha")
    print("7.) NTARJETA")
    print("8.) ESTADO")
    print("9.) Salir")

def MenuPlanes():
    print("1.) Nombre")
    print("2.) Valor")
    print("3.) Cantidad Canciones")
    print("4.) Salir")

def ImprimirTabla(tabla):
    if (tabla == "CANCIONES"):
        print("CODIGO"," ","NOMBRE"," ","GENERO"," ","ALBUM"," ","INTERPRETE")
        print("")
        print("")
    if (tabla == "CLIENTES"):
        print("CEDULA"," ","NOMBRE"," ","APELLIDO"," ","PAIS","CIUDAD","CELULAR","FECHA","NTARJETA","ESTADO")
        print("")
        print("")
    if (tabla == "PLANES"):
        print("CODIGO"," ","NOMBRE"," ","VALOR"," ","CANTIDAD")
        print("")
        print("")
    
    

def Salir():
    condition = True
    salida = input("Esta seguro que desea salir Y|N: ")
    if (salida == "Y"):
        condition = False
    else:
        pass
    return condition
