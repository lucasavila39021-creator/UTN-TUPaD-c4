#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
mayor_edad=int(input("Dime tu edad: "))
if mayor_edad>=18:
    print("Es mayor de edad")
else:
    pass

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
#mensaje “Desaprobado”. 

nota=int(input("Ingrese su nota:"))
if nota>=6:
    print("Aprobado")
else:
    print("Desaprobado")


#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
#operador de módulo (%) en Python para evaluar si un número es par o impar.

numeros_pares=int(input("Por favor ingrese solo números pares:"))
if (numeros_pares%2==0):
    print("Ha ingresado un número par")
else:
    print("Por favor,ingrese un numero par")


#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
#siguientes categorías pertenece: 
#● Niño/a: menor de 12 años. 
#● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#● Adulto/a: mayor o igual que 30 años.

edad=int(input("Ingrese su edad: "))
if edad<12 and edad >0:
    print("Eres un niño")
elif edad>=12 and edad<18:
    print("Eres un adolecente")
elif edad>=18 and edad<30:
    print("Eres un joven adulto")
else:
    print("Eres un adulto")


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
#como una lista o un string.

contrasena=(input("Ingrese una contraseña, entre 8 y 14 caracteres"))
longitud= len(contrasena)
if longitud>=8 and longitud<=14:
    print("Ha ingresado una contraseña correcta")
else:
     print("La contraseña debe tener entre 8 y 14 caracteres")

#6)_

import random
from statistics import mode, median, mean

#Generar una lista de 50 números aleatorios entre 1 y 100

numeros_aleatorios=[random.randint(1,100) for i in range(50)]
print(f"Lista de números aleatorios:{numeros_aleatorios}\n")

#Calcular la media, moda y mediana

moda=mode(numeros_aleatorios)

mediana=median(numeros_aleatorios)
media=mean(numeros_aleatorios)

print(f"Moda:{moda}")
print(f"Mediana:{mediana}")
print(f"Media:{media}\n")

#Determinar el sesgo

if media>mediana:
    print("El sesgo es positivo o a la derecha(media>mediana).")
elif media<mediana:
    print("El sesgo es negativo o a la izquierda (media<mediana).")
else:
    print("No hay sesgo (media = mediana).")


#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
#dependiendo de la opción que desee: 
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre=input("Ingresa tu nombre:")
opcion=int(input("Ingrese una opción(1= mayúsculas, 2= minúsculas, 3= primera letra en mayúscula):"))
#usamos una estructura condicional para formatear el nombre según la opción
if opcion==1:
    nombre_formateado=nombre.upper()
    print(f"Su nombre en mayúsculas es:{nombre_formateado}")
elif opcion==2:
    nombre_formateado=nombre.lower()
    print(f"Su nombre en minúsculas es:{nombre_formateado}")
elif opcion==3:
    nombre_formateado=nombre.title()
    print(f"Su nombre con la primera letra en mayúscula es :{nombre_formateado}")
else:
    print("Opción no válida. Por favor, inrese 1, 2 o 3")


#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
#por pantalla: 
#● Menor que 3: "Muy leve" (imperceptible). 
#● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
#generalmente no causa daños). 
#● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
#débiles). 
#● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud_terremoto=float(input("Ingrese la magnitud del terremoto:"))
if magnitud_terremoto < 3 and magnitud_terremoto>0:
    print("El terremoto fue Muy leve(imperceptible)")
elif magnitud_terremoto>=3 and magnitud_terremoto<4:
    print("El terremoto fue Leve (Casi imperceptible)")
elif magnitud_terremoto>=4 and magnitud_terremoto<5:
    print("EL terremoto fue moderado (sentido por personas pero generalmente no causa daños).)")
elif magnitud_terremoto>=5 and magnitud_terremoto<6:
    print("El terremoto fue fuerte (Puede causar daños en estructuras débiles)")
elif magnitud_terremoto>=6 and magnitud_terremoto<7:
    print("El terremoto fue muy fuerte y puede causar daños significativos en estructuras")
elif magnitud_terremoto>=7:
    print("El terremoto fue extremo (no se recomienda permanecer dentro de ninguna estructura cuya intregridad fuera comprometida)")
else:
    pass

#10)_Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
#si el usuario se encuentra en otoño, invierno, primavera o verano. 


#Solicitar al usuario que ingrese datos:

Hemisferio=input("Ingresa tu hemisferio (N/S):")
mes=input("Ingresa el mes:")
dia=int(input("Ingresa el dia:"))

#Convertimos el mes a minúsculas para evitar errores

mes=mes.lower()

#Lógica del hemisferio Norte

if Hemisferio.lower()=="n":
    #Verano del 21 de Junio al 20 de Septiembre:
    if (mes=="junio" and dia>=21) or (mes=="julio" or mes=="agosto") or (mes=="septiembre" or dia<=20):
        print("La estación es Verano")
    #Otoño del 21 de Septiembre al 20 de Diciembre:
    elif (mes=="septiembre" and dia>=21) or (mes=="octubre" or mes=="noviembre") or (mes=="diciembre" or dia<=20):
        print("La estación es otoño")
    #Invierno del 21 de Diciembre al 20 de Marzo:
    elif (mes=="diciembre" and dia>=21) or (mes=="enero" or mes=="febrero") or (mes=="marzo" or dia<=20):
        print("La estación es Invierno")
    #Primavera del 21 de Marzo al 20 de Junio:
    elif (mes=="marzo" and dia>=21) or (mes=="abril" or mes=="mayo") or (mes=="junio" or dia<=20):
        print("La estación es Primavera")
    else:
        print("Fecha no válida para el hemisferio norte")
#Lógica para el hemisferio sur:
elif Hemisferio.lower()=="s":
    #Invierno del 21 de Junio al 20 de Septiembre:
    if (mes=="junio" and dia>=21) or (mes=="julio" or mes=="agosto") or (mes=="septiembre" or dia<=20):
        print("La estación es Invierno")
    #Primavera del 21 de Septiembre al 20 de Diciembre:
    elif (mes=="septiembre" and dia>=21) or (mes=="octubre" or mes=="noviembre") or (mes=="diciembre" or dia<=20):
        print("La estación es Primavera")
    #Verano del 21 de Diciembre al 20 de Marzo:
    elif (mes=="diciembre" and dia>=21) or (mes=="enero" or mes=="febrero") or (mes=="marzo" or dia<=20):
        print("La estación es Verano")
    #Otoño del 21 de Marzo al 20 de Junio:
    elif (mes=="marzo" and dia>=21) or (mes=="abril" or mes=="mayo") or (mes=="junio" or dia<=20):
        print("La estación es Otoño")
    else:
        print("Fecha no válida para el hemisferio sur")
#Si el hemisferio no es ni N ni S:
else:
    print("Hemisferio no válido. Por favor ingresa N o S")