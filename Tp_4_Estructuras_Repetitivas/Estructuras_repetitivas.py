#1)_ Crea un programa que imprima por pantalla todos los números de 0 hasta 100 (Incluyendo)
#ambos extremos, en orden creciente, mostrando un número por línea.

for i in range(1,101):
    print(i)

print(".............................................")
print(".............................................")

#2)_Desarrolla un programa que solicite al usuario un número entero y determine la cantidad 
#de dígitos que tiene.
num_str=input("Ingresa un número entero:")
cant_dig= len(num_str)
print(f"El número tiene {cant_dig} dígitos")
print(".............................................")
print(".............................................")

#3)_Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.


num1=int(input("Ingrese el primer número entero: "))
num2=int(input("Ingrese el segundo número entero: "))

    #asuguramos que el primer número sea el menor para nuestro rango
if num1>num2:
        num1,num2=num2,num1
    #inicializa la variable para la suma
suma_total=0
print(f"\nLos números entre {num1} y {num2} son:")
    #bucle para imprimir los números y sumarlos 
for numero in range(num1+1,num2):
        print(numero)
        suma_total+=numero #agrega el número actual a la suma
print(f"\nLa suma de estos números es: {suma_total}")

print(".............................................")
print(".............................................")

#4)_Elabora un programa que permita al usuario ingresar números enteros
#y los sume en secuencia. El programa debe detenerse y mostrar el acumulado 
#cuando el usuario ingrese un 0.

sum_total=0#iniciamos la variable que acumulará la suma de los números
while True:
       
    num_ingresado=int(input("Ingresa un número o 0 para detener y ver la suma:"))
    if num_ingresado==0:
         break #si el número es 0 salimos del bucle
    elif num_ingresado!=0:
          sum_total+=num_ingresado
    else:
          print("Por favor, ingrese un número entero: ")

           
            
print(f"La suma total de los números ingresados es:{sum_total}")

print(".............................................")
print(".............................................")

#5)_Crea un juego en el que usuario deba adivinar un número aleatorio entre 0 y 9
# Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar
#el número
import random
numero_secreto=random.randint(0,9)

#inicimamos el contador de intentos 
intentos=0
print("!Bienvenido al juego de adivinar el número¡")
print("¡Adivina el número secreto! Esta entre 0 y 9.")

# Bucle principal del juego
while True:
    # pide al usuario que ingrese su suposicón 
    suposición = int(input("¿Cuál crees que es el número?"))
    #incrementamos el contador de intentos 
    intentos +=1
    #comprobamos si la suposición es correcta
    if suposición==numero_secreto:
        print(f"¡Felicidades! adivinaste el número en el {intentos} intentos.")
        break
    elif suposición<numero_secreto:
         print("El número que buscas es mayor. Intenta de nuevo")
    else:
         print("El número quebuscas es menor. Intenta de nuevo")




print("................................................................")
print("................................................................")

#6)_Desaorrolla un programa que imprima todos los números pares comprendidos entre
#0 y 100, en orden decreciente.

for numero in range(100,-1,-2):
    print(numero)
           

print("................................................................")
print("................................................................")

#7)_Escribe un programa que calcule la suma de todos los números comprendidos entre 0 y un número
#entero positivo indicado por el usuario.

#inicimos un contador que almacenará nuestra suma
#resultado usando un bucle for
num=int(input("Ingresa un número entero positivo:"))
suma=0
#usamos un bucle for para iterar desde 0 hasta num (inclusive)
for i in range(num+1):
     suma+=i #agregamos el valor actual de i a la suma

print(f"La suma de todos los números entre 0 y {num} es: {suma}")



print("................................................................")
print("................................................................")

#8)_Escribe un programa que perimita al usuario ingresar 100 numeros enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuantos son positivos.
cantidad_numeros=10

#iniciamos los contadores
pares=0
impares=0
positivos=0
negativos=0

print(f"Por favor; ingresa {cantidad_numeros} de números enteros:")
#usamos un bucle for para pedir los números al usuario
for i in range(cantidad_numeros):
    num=int(input(f"Ingrese el número {i+1}: "))
    #verificamos los datos ingresados y actualizamos los contadores
    if num%2==0:
         pares+=1
    else:
         impares+=1
    if num>0:
         positivos+=1
    elif num<0:
         negativos+=1
         # mostramos los resultados


print(f"\nDe los {cantidad_numeros} números ingresados:")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")


print("................................................................")
print("................................................................")


 #9)_Crea un programa que permita al usuario ingresar 100 números enteros,
 # y luego calcule la media de esos valores
  
          
cantidad_numeros=10

#iniciamos la variable para la suma
sum_total=0
contador_numeros=1
print(f"Por favor; ingresa {cantidad_numeros} números enteros:")
#usamos un bucle while para ejecutarmientras el contador sea menor o igual a la cantidad de números
#ingresados
while contador_numeros<=cantidad_numeros:
     num=int(input(f"Ingrese el número {contador_numeros}: "))
     sum_total+=num #agregamos el número ingresado a la suma total
     contador_numeros+=1 #incrementamos el contador
#calculamos la media
media=sum_total/cantidad_numeros
print(f"\nLa media de los {cantidad_numeros} números ingresados es: {media}")



print("................................................................")
print("................................................................")


#10)_Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario.

numero_original=int(input("Ingresa un número entero para invertir: "))
#creamos una variable para almacenar el número invertido
numero_invertido=0
#guardamos el número original para mostrarlo al final
num=numero_original
#usamos un bucle while para procesar cada dígito
while numero_original>0:
    digito=numero_original%10 #obtenemos el último dígito
    numero_invertido=numero_invertido*10+digito #agregamos el dígito al número invertido
    numero_original//=10 #eliminamos el último dígito del número original
print(f"El número {num} invertido es: {numero_invertido}")




   

              
       
