#1)_ crear una lista con los números del 1 al 100 que sean multiplos de 4. utilizar la función range.

multiplos_de_4=[]

for numero in range(1,101):
    if numero % 4 == 0:
        multiplos_de_4.append(numero)

print(multiplos_de_4)

print(".......................................")
print(".......................................")
#2)_crear un alista con 5 elementos (colocar los elementos que más te gusten) y mostrar el 
#penúltimo ¡puedes hacerlo como se muestra en los videos o bien investigar como funciona el
#indexado negativo en las listas!

lista_favoritos=["Álgebra","Matemáticas","Quimica","Fisica","Estadistíca"]
penultimo_elemento=lista_favoritos[3]
print(penultimo_elemento)

# El indexado negativo en las listas de python te permite acceder a los elementos desde el 
#final de la lista. EL último elemento tiene el índice -1, el penúltimo -2 y asi sucesivamente
#. Por ejemplo, en mi_lista=["a","b","c"], mi_lista[-1] devuelve "c".

print(".......................................")
print(".......................................")

#3)_crear una lista vacia, agregar 3 palabras con append e imprimir la lista resultante por pantalla

lista_vacia=[]
lista_vacia.append("Hola")
lista_vacia.append("Mundo")
lista_vacia.append("Python")
print(lista_vacia) 


print(".......................................")
print(".......................................")

#4)_Reemplzar el segundo y el último valor de la lista "animales" con las palabras "loro
# y "oso", respectivamente. Imprimir la lista resultante por pantalla.
animales=["perro","gato","conejo","pez"]

animales[1]="loro"
animales[3]="oso"

print(animales)


print(".......................................")
print(".......................................")

#5)_Analizar el siguiente programa y explicar con tus palabras que es lo que hace y por qué.
numeros=[8,15,3,22,7]
numeros.remove(max(numeros))# A simple vista y sin conocer que hace la función max(), diria que 
#lo que hace este código es remover o quitar el número mas grande que hay en la lista, ya que la función
#remove sirve para remover un elemento de la lista y la función.
print(numeros)


print(".......................................")
print(".......................................")

#6)_Crea una lista con números del 10 al 30 (Incluído), haciendo saltos de 5 en 5 y mostrar por 
# pantalla los 2 primeros.

numeros=list(range(10,31,5))

print(numeros[:2])


print(".......................................")
print(".......................................")

#7)_Reemplazar los valores centrales (índices 1 y 2) de la lista "autos" por dos nuevos valores
# (los que quieras). Imprimir la lista resultante por pantalla.
autos=["sedan","polo","suran","gol"]
autos[1]="camioneta"
autos[2]="4x4"
print(autos)


print("......................................")
print("......................................")

#8)_crea una lista vacia llamada "dobles" y agregar el doble de 5, 10 y 15 usando append 
# directamente. Imprimir la lista resultante por pantalla.

dobles=[]   
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)


print(".......................................")
print(".......................................")

#9)_Dada la lista "compras", cuyos elementos representan productos comprados por 
#diferentes clientes:
compras=[["pan","leche"],["arroz","fideos","salsa"],["agua"]]

# a)_Agregar "jugo" a la lista del tercer cliente usando append.

compras[2].append("jugo")

# b)_Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.

compras[1][1]="tallarines"

# c)_ Eliminar "pan" de la lista del primer cliente usando remove.
compras[0].remove("pan")

# d)_Imprimir la lista resultante por pantalla.
print(compras)


print("...................................")
print("...................................")

# 10)_ Elaborar una lista anidada llamada "lista_anidada" que contenga los siguientes elementos

#posoción lista_anidada[0]:15
#posición lista_anidada[1]:true
#posición lista_anidada[2][0]:25.5
#posición lista_anidada[2][1]:57.9
#posición lista_anidada[2][2]:30.6
#posición lista_anidada[3]: False

Lista_anidada=[['15'],["True"],['20.5','57.9','30.6'],["False"]]
print(lista_anidada)
