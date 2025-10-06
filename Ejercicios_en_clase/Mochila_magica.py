# Mochila mágica con manejo de excepciones
tamaño_mochila = 0
while tamaño_mochila <= 0:
    try:
        tamaño_mochila = int(input("Ingresa cuántos espacios tendrá la mochila: "))
        if tamaño_mochila <= 0:
            print("Error: El número debe ser positivo y mayor que cero.")
    except ValueError:
        print("Error: Debes ingresar un número válido.")
mochila = [None] * tamaño_mochila
def mostrar_mochila():
    print("Contenido de la mochila:")
    for i in range(len(mochila)):
        if mochila[i] is None:
            print(f"Espacio {i+1}: --- vacío ---")
        else:
            print(f"Espacio {i}: {mochila[i]}")
print("--- Menú de la Mochila ---")
while True:
    print("1. Guardar objeto")
    print("2. Ver mochila")
    print("3. Salir")
    print("4. Eliminar objeto (Desafío Extra)")
    opcion = input("Elige una opción: ")
    if opcion == '1':
        try:
            posicion = int(input(f"Ingresa la posición (1-{tamaño_mochila}): "))
            if posicion < 0 or posicion >= tamaño_mochila:
                raise IndexError
            objeto = input("Ingresa el objeto mágico: ").strip()
            if objeto == "":
                print("Error: No puedes dejar el nombre del objeto vacío.")
            else:
                mochila[posicion] = objeto
                print(f"{objeto} guardado en el espacio {posicion}.")
        except ValueError:
            print("Error: Debes ingresar un número válido para la posición.")
        except IndexError:
            print("Error: La posición ingresada no existe en la mochila.")
    elif opcion == '2':
        mostrar_mochila()
    elif opcion == '3':
        print("¡Gracias por usar la mochila mágica! ¡Hasta luego!")
        break
    elif opcion == '4':
            #desafio extra
            #4. Eliminar objeto → El usuario elige una posición y el objeto de ese espacio se elimina (queda vacío otra vez).
            #• Si la posición no existe → IndexError.
            #• Si el espacio ya estaba vacío, mostrar un mensaje que lo indique.
        try:
            posicion = int(input(f"Ingresa la posición (0-{tamaño_mochila - 1}) para eliminar: "))
            if posicion < 0 or posicion >= tamaño_mochila:
                raise IndexError
            if mochila[posicion] is None:
                print(f"El espacio {posicion} ya está vacío.")
            else:
                objeto_eliminado = mochila[posicion]
                mochila[posicion] = None
                print(f"{objeto_eliminado} eliminado del espacio {posicion}.")
        except ValueError:
            print("Error: Debes ingresar un número válido para la posición.")
        except IndexError:
            print("Error: La posición ingresada no existe en la mochila.")
    else:
        print("Opción no válida. Por favor, elige 1, 2 o 3.")
