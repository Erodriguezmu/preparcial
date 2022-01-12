def Menu(): #este es el menu principal donde se elige la tabla que va a ser usada.
    print("Bienvenido, seleccione la operacion que desea realizar")
    print("1.) Canciones")
    print("2.) Clientes")
    print("3.) Planes")
    print("4.) Lista")
    print("5.) Salir")
    while True:
        try:
            opcion = int(input("Digite la opción: "))
            break
        except:
            print("Numero no valido, escoga denuevo.")
    return opcion

def MenuOpciones(): #las 3 primeras tablas usan esta opcion por lo que es llamada luego del menu.
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

def MenuLista(): # solo la opcion lista usa esta tabla ya que no se requiere modificar los campos de la lista.
    print("Seleccione la operacion que desea realizar")
    print("1.) Añadir")
    print("2.) Eliminar")
    print("3.) Consultar")
    print("4.) Reproducir Cancion")
    print("5.) Salir")
    while True:
        try:
            opcion = int(input("Digite la opción: "))
            break
        except:
            print("Numero no valido, escoga denuevo.")
    return opcion
    
    
def MenuCanciones(): #este menu es llamado cuando se requiere que se vean los atributos de CANCIONES para elegir alguno de ellos
    print("1.) Nombre")
    print("2.) Genero")
    print("3.) Album")
    print("4.) Interprete")
    print("5.) Cancelar")

def MenuClientes(): #este menu es llamado cuando se requiere que se vean los atributos de CLIENTES para elegir alguno de ellos
    print("1.) Nombre")
    print("2.) Apellido")
    print("3.) Pais")
    print("4.) Ciudad")
    print("5.) Celular")
    print("6.) Fecha")
    print("7.) NTARJETA")
    print("8.) ESTADO")
    print("9.) Salir")

def MenuPlanes(): #este menu es llamado cuando se requiere que se vean los atributos de PLANES para elegir alguno de ellos
    print("1.) Nombre")
    print("2.) Valor")
    print("3.) Cantidad Canciones")
    print("4.) Salir")

def ImprimirTabla(tabla): # Esta funcion se usa para mostrar los atributos de las tablas antes de mostrar los campos
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
    if (tabla == "LISTA"):
        print("IDCLIENTE"," ","IDCANCION")
        print("")
        print("")

def Salir(): #funcion para salir, si la persona desea salir convierte condition en false y lo envia a menu para que termine la ejecucion
    condition = True
    salida = input("Esta seguro que desea salir Y|N: ")
    if (salida == "Y"):
        condition = False
    else:
        pass
    return condition
