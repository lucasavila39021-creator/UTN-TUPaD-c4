#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. 

print("Hola mundo")


#Punto2
#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
#realizar la impresión por pantalla. 
nombre=input("Por favor, escribe tu nombre:")

print("Mucho gusto",nombre,"!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
#la impresión por pantalla.

nombre=input("Ingresa tu nombre:")
apellido=input("Ingresa tu apellido:")
edad=input("Ingresa tu edad:")
edad=int(edad)
residencia=input("Ingresa tu domicilio:")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
#su perímetro.

import math


radio = float(input("Ingrese el radio del círculo: "))


area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio


print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
#cuántas horas equivale.

calculador_de_horas=float(input("Ingresa la cantidad de segundos que quieres convertir a horas: "))
pasaje=calculador_de_horas/3600
print(f"Los segundos ingresados equivalen a {pasaje} horas")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
#multiplicar de dicho número. 
numero=int(input("Introduce un número para ver su tabla de multiplicar:"))
print(f"---Tabla de multiplicar del {numero}---")
for i in range(1,11):
    resultado=numero*i
    print(f"{numero} x {i}= {resultado}")


#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 
num1=int(input("Introduce el primer número entero distinto de 0:"))
num2=int(input("Introduce el segundo número entero distinto de 0:"))
suma=num1+num2
resta=num1-num2
multiplicacion=num1*num2
division=num1/num2
print(f"El resultado de la suma es: {suma}")
print(f"Elresultado de la resta es: {resta}")
print(f"El resultado de la multiplicación es: {multiplicacion}")
print(f"El reultado de la división es: {division}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
#de masa corporal.
# Pedir al usuario que ingrese su peso en kilogramos
peso=float(input("Introduzca su peso en kilogramos:"))
altura=float(input("Introduzca su altura en metros:"))
indice_de_masa_corporal=(peso/altura**2)
if altura>0:
    print(f"Su índice de masa corporal es: {indice_de_masa_corporal}")
else:
    print("No ha ingresado un valor válido para la ultura")
        

 #9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
#pantalla su equivalente en grados Fahrenheit.
grados_celsius=float(input("Ingrese la temperatura en grados celsius y la convertiremos a grados Fahrenheit:"))
grados_fahrenheit=1.8*grados_celsius+32
print(f"La temperatura equivalente en grados Fahrenheit es:{grados_fahrenheit}")



#10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
#dichos números. 
num1=int(input("Ingresa el primer número: "))
num2=int(input("Ingresa el segundo número: "))
num3=int(input("Ingresa el tercer número: "))
promedio=(num1+num2+num3)/3
print(f"El promedio de los 3 números ingresados es:{promedio}")