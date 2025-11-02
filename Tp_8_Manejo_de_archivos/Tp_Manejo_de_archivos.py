# # 1. Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos.
# # Cada línea debe tener: nombre,precio,cantidad
# with open ("productos.txt","w") as archivo:
#     archivo.write("nombre,precio,cantidad\n")
#     archivo.write("mesa,$150.000,7\n")
#     archivo.write("silla,$35.000,15\n")
#     archivo.write("mesa de luz,$65.000,8\n")
# print("Archivo 'productos.txt' creado exitosamente")
# dejo comentado el punto 1 porque me borraba el avance del archivo cada vez que ejecutaba de nuevo la terminal

print("--------------------------------------------")

# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea,
#  la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

with open("productos.txt","r") as archivo:
    encabezado=archivo.readline()
    for linea in archivo:
        linea=linea.strip()
        partes=linea.split(",")
        #Asignamos a cada parte una variable para mas claridad
        nombre=partes[0]
        precio=partes[1]
        cantidad=partes[2]
        print(f"Producto:{nombre} | Precio: {precio} | Cantidad: {cantidad}")

print("--------------------------------------------")

# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar los productos,
#le pida al usuario que ingrese un nuevo producto (nombre, precio, cantidad) y lo agregue al archivo
#   sin borrar el contenido existente.
print("\n--- Agregar nuevo producto ---")
nombre_nuevo=input("Ingrese el nombre del producto: ")
precio_nuevo=input("Ingrese el precio del producto: ")
cantidad_nueva=input("Ingrese la cantidad: ")

#Abrimos el archivo en modo 'a' (append) para añadir al final
with open ("productos.txt","a") as archivo:
    #formateamos el string con el salto de linea al final
    linea_nueva=f"{nombre_nuevo},{precio_nuevo},{cantidad_nueva}\n"
    archivo.write(linea_nueva)

print(f"Producto '{nombre_nuevo}' agregado exitosamente")

print("-------------------------------------------------")

# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en una lista llamada productos,
#  donde cada elemento sea un diccionario con claves: nombre, precio, cantidad.
productos=[]
try:
    with open ("productos.txt","r") as archivo:
        encabezado= archivo.readline()
        for linea in archivo
            linea=linea.strip()
                if linea:
                    partes=linea.split(",")
                    producto_dic= {
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad,
                    }
                    productos.append(producto_dic)
    print("Lista cargada en la memoria")
    print("Contenido de la lista (para verificar) ")
    print(productos)
    print("----------------------------------------------")
    except FileNotFoundError:
        print("Error: El archivo productos.txt no se encontro.")
    except Exception as e:
        print(f"Ocurrio el error: {e}")
            
