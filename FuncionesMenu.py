def menu():
    print("Bienvenido, seleccione la operacion que desea realizar")
    print("1.) Canciones")
    print("2.) Clientes")
    print("3.) Planes")
    print("4.) Planes por cliente")
    print("5.) Listas")
    print("6.) Salir")
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
    print("2.) Modificar")
    print("3.) Eliminar")
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
    print("1.) Consultar")
    print("2.) Añadir a mi lista")
    print("3.) Eliminar de mi lista")
    print("4.) Salir")
    while True:
        try:
            opcion = int(input("Digite la opción: "))
            break
        except:
            print("Numero no valido, escoga denuevo.")
    return opcion
    

def MenuAñadir:
    
def MenuBorrar:

def MenuModificar:

def MenuConsultar:

def MenuCanciones:
    print("1.) Nombre")
    print("2.) Genero")
    print("3.) Album")
    print("4.) Interprete")
    print("5.) Cancelar")

    

def Salir():
    condition = True
    salida = input("Esta seguro que desea salir Y|N: ")
    if (salida == "Y"):
        condition = False
    else:
        pass
    return condition
                    print("Numero no valido, escoga denuevo.")
            return opcion1
