lista_de_compras = []

def menu():
    while True:
        seleccion = input("¿Que deseas hacer? A: Agregar articulo; B: Eliminar articulo, C: Mostrar lista; D: salir: ")
        seleccion = seleccion.upper()
        if seleccion == 'A':
            agregar()
        elif seleccion == 'B':
            eliminar()
        elif seleccion == 'C':
            mostrar()
        elif seleccion == 'D':
            ("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def agregar():
    lista_de_compras.append(input("Agregar elemento: "))
    while True: 
        continuar = input("Para agregar otro articulo pulsa Y, para volver N: ")
        continuar = continuar.upper()
        if continuar == "Y":
             lista_de_compras.append(input("Agregar elemento: "))
             mostrar()
        elif continuar == "N":
            return True
        else: 
            print("Ingresa una opcion valida")

def eliminar():
    while True:
        print("Esta es tu lista:")
        mostrar()

        eliminar_index = int(input("Ingresa el index del elemento que deseas eliminar: "))
        if eliminar_index <= len(lista_de_compras) + 1:
            eliminar_index = eliminar_index - 1
            lista_de_compras.pop(eliminar_index)
            mostrar()
        else:
            print("Ingrese un valor valido")

        continuar = input("Si deseas eliminar otro elemento pulsa Y, para volver N: ")
        continuar = continuar.upper()
        if continuar == "Y":
             eliminar_index
        elif continuar == "N":
            break     
        else: 
            print("Ingresa una opcion valida")
def mostrar():
        for i in lista_de_compras:
            print(i)

menu()