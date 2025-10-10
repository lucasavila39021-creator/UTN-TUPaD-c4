#1) Dado el diccionario precios_frutas 
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
#1450} 
#Añadir las siguientes frutas con sus respectivos precios: 
#● Naranja = 1200 
#● Manzana = 1500 
#● Pera = 2300 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)
print("--------------------------------------------------")

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
#● Banana = 1330 
#● Manzana = 1700 
#● Melón = 2800 
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)
print("--------------------------------------------------")

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
#precios.

lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

print("--------------------------------------------------")

#4) Escribí un programa que permita almacenar y consultar números telefónicos. 
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
#• Luego, pedí un nombre y mostrale el número asociado, si existe. 
agenda_telefonica = {}
for _ in range(5):
    nombre = input("Ingresa el nombre del contacto: ")
    if nombre in agenda_telefonica:
        print("Este contacto ya existe. Por favor, ingresa otro nombre.")
        continue
    elif nombre.strip() == "":
        print("El nombre no puede estar vacío. Por favor, ingresa un nombre válido.")
        continue
    elif len(nombre) > 15:
        print("El nombre es demasiado largo. Por favor, ingresa un nombre más corto.")
        continue
    elif not nombre.replace(" ", "").isalpha():
        print("El nombre solo debe contener letras y espacios. Por favor, ingresa un nombre válido.")
        continue
    numero = input("Ingresa el número telefónico: ")
    if not numero.isdigit() or len(numero) < 7 or len(numero) > 15:
        print("El número telefónico debe contener solo dígitos y tener entre 7 y 15 caracteres. Por favor, ingresa un número válido.")
        continue
    agenda_telefonica[nombre] = numero
print("Agenda telefónica cargada.")
nombre_consulta = input("Ingresa el nombre del contacto que deseas consultar: ")
if nombre_consulta in agenda_telefonica:
    print(f"El número de {nombre_consulta} es: {agenda_telefonica[nombre_consulta]}")
else:
    print(f"No se encontró el contacto con el nombre {nombre_consulta}.")
    
print("--------------------------------------------------")

#5) Solicita al usuario una frase e imprime: 
#• Las palabras únicas (usando un set). 
#• Un diccionario con la cantidad de veces que aparece cada palabra.
frase = input("Ingresa una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)
contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1
print("Contador de palabras:", contador_palabras)

print("--------------------------------------------------")

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
#Luego, mostrá el promedio de cada alumno.
alumnos = {}
for _ in range(3):
    nombre = input("Ingresa el nombre del alumno: ")
    notas = []
    for i in range(3):
        while True:
            try:
                nota = float(input(f"Ingresa la nota {i+1} de {nombre}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 0 y 10. Intenta nuevamente.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número.")
    alumnos[nombre] = tuple(notas)
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {promedio:.2f}")
    
print("--------------------------------------------------")

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
#y Parcial 2: 
#• Mostrá los que aprobaron ambos parciales. 
#• Mostrá los que aprobaron solo uno de los dos. 
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 
parcial_1 = {1, 2, 3, 4, 5}
parcial_2 = {4, 5, 6, 7, 8}
aprobados_ambos = parcial_1.intersection(parcial_2) 
print("Estudiantes que aprobaron ambos parciales:", aprobados_ambos)
aprobados_solo_uno = parcial_1.symmetric_difference(parcial_2)
print("Estudiantes que aprobaron solo uno de los dos parciales:", aprobados_solo_uno)
aprobados_al_menos_uno = parcial_1.union(parcial_2)
print("Estudiantes que aprobaron al menos un parcial:", aprobados_al_menos_uno)

print("--------------------------------------------------")
#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
#Permití al usuario: 
#• Consultar el stock de un producto ingresado. 
#• Agregar unidades al stock si el producto ya existe. 
#• Agregar un nuevo producto si no existe. 
inventario = {}
while True:
    print("1. Consultar stock")
    print("2. Agregar unidades al stock")
    print("3. Agregar nuevo producto")
    print("4. Salir")
    opcion = input("Elige una opción: ")
    if opcion == '1':
        producto = input("Ingresa el nombre del producto a consultar: ")
        if producto in inventario:
            print(f"El stock de {producto} es: {inventario[producto]}")
        else:
            print(f"El producto {producto} no existe en el inventario.")
    elif opcion == '2':
        producto = input("Ingresa el nombre del producto para agregar unidades: ")
        if producto in inventario:
            try:
                unidades = int(input("Ingresa la cantidad de unidades a agregar: "))
                if unidades > 0:
                    inventario[producto] += unidades
                    print(f"Se han agregado {unidades} unidades a {producto}. Nuevo stock: {inventario[producto]}")
                else:
                    print("La cantidad debe ser un número positivo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número.")
        else:
            print(f"El producto {producto} no existe en el inventario.")
    elif opcion == '3':
        producto = input("Ingresa el nombre del nuevo producto: ")
        if producto in inventario:
            print(f"El producto {producto} ya existe en el inventario.")
        else:
            try:
                unidades = int(input("Ingresa la cantidad inicial de unidades: "))
                if unidades >= 0:
                    inventario[producto] = unidades
                    print(f"Producto {producto} agregado con un stock de {unidades}.")
                else:
                    print("La cantidad debe ser un número no negativo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número.")
    elif opcion == '4':
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 4.")
        
        
print("--------------------------------------------------")

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
#Permití al usuario: 
#• Agregar un evento (si ya hay uno, avisar que se sobrescribirá).
#• Consultar un evento en un día y hora determinados (si no hay ninguno, avisar).
agenda = {}
while True:
    print("1. Agregar evento")
    print("2. Consultar evento")
    print("3. Salir")
    opcion = input("Elige una opción: ")
    if opcion == '1':
        try:
            dia = int(input("Ingresa el día (1-31): "))
            hora = int(input("Ingresa la hora (0-23): "))
            if not (1 <= dia <= 31) or not (0 <= hora <= 23):
                print("Día o hora inválidos. Por favor, ingresa valores correctos.")
                continue
            evento = input("Ingresa el nombre del evento: ").strip()
            if evento == "":
                print("El nombre del evento no puede estar vacío.")
                continue
            clave = (dia, hora)
            if clave in agenda:
                print(f"Advertencia: Ya existe un evento en {clave}. Se sobrescribirá.")
            agenda[clave] = evento
            print(f"Evento '{evento}' agregado en {clave}.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa números para día y hora.")
    elif opcion == '2':
        try:
            dia = int(input("Ingresa el día (1-31) para consultar: "))
            hora = int(input("Ingresa la hora (0-23) para consultar: "))
            if not (1 <= dia <= 31) or not (0 <= hora <= 23):
                print("Día o hora inválidos. Por favor, ingresa valores correctos.")
                continue
            clave = (dia, hora)
            if clave in agenda:
                print(f"El evento en {clave} es: {agenda[clave]}")
            else:
                print(f"No hay ningún evento programado en {clave}.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa números para día y hora.")
    elif opcion == '3':
        print("Saliendo de la agenda. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 3.")
        
        
print("--------------------------------------------------")

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
#diccionario donde: 
#• Las capitales sean las claves. 
#• Los países sean los valores. 
original = {'Argentina': 'Buenos Aires', 'Brasil': 'Brasilia', 'Chile': 'Santiago', 'Perú': 'Lima'}
invertido = {capital: pais for pais, capital in original.items()}
print(invertido)