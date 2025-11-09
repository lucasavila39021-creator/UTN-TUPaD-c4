# # --------------------------------------------------
# # Ejercicio 1: Factorial 
# # --------------------------------------------------

# def factorial_recursivo(n):
#     #Calcula el factorial de n de forma recursiva.
#     # Caso base
#     if n == 0:
#         return 1
#     # Caso recursivo
#     else:
#         return n * factorial_recursivo(n - 1)

# print("--- Ejercicio 1: Factoriales ---")
# try:
#     num_usuario = int(input("Ingrese un número entero para calcular factoriales (1 a N): "))
    
#     if num_usuario < 1:
#         print("Por favor, ingrese un número mayor a 0.")
#     else:
#         # Bucle para mostrar el factorial de cada número 
#         for i in range(1, num_usuario + 1):
#             resultado_fact = factorial_recursivo(i)
#             print(f"El factorial de {i} es: {resultado_fact}")
            
# except ValueError:
#     print("Entrada no válida. Debe ingresar un número entero.")


# # --------------------------------------------------
# # Ejercicio 2: Fibonacci 
# # --------------------------------------------------

# def fibonacci_recursivo(posicion):
#     #Calcula el número de Fibonacci en una posición dada.
#     # Casos base (posición 0 y 1)
#     if posicion == 0:
#         return 0
#     elif posicion == 1:
#         return 1
#     # Caso recursivo
#     else:
#         return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2)

# print("\n--- Ejercicio 2: Serie de Fibonacci ---")
# try:
#     pos_usuario = int(input("Ingrese hasta qué posición desea ver la serie de Fibonacci: "))
    
#     if pos_usuario < 0:
#         print("Por favor, ingrese una posición positiva (0 o mayor).")
#     else:
#         print(f"Serie de Fibonacci hasta la posición {pos_usuario}:")
#         # Bucle para mostrar la serie completa 
#         for i in range(pos_usuario + 1):
#             resultado_fib = fibonacci_recursivo(i)
#             print(f"Posición {i}: {resultado_fib}")

# except ValueError:
#     print("Entrada no válida. Debe ingresar un número entero.")


# # --------------------------------------------------
# # Ejercicio 3: Potencia 
# # --------------------------------------------------

# def potencia_recursiva(base, exponente):
#     #Calcula la potencia usando la fórmula n^m = n * n^(m-1).
#     # Caso base (exponente 0)
#     if exponente == 0:
#         return 1
#     # Caso recursivo
#     else:
#         # Aplicamos la fórmula dada 
#         return base * potencia_recursiva(base, exponente - 1)

# print("\n--- Ejercicio 3: Potencia Recursiva ---")
# try:
#     base_user = int(input("Ingrese el número base: "))
#     exp_user = int(input("Ingrese el exponente: "))
    
#     if exp_user < 0:
#         print("Este ejemplo funciona con exponentes positivos.")
#     else:
#         # Algoritmo general para probar la función 
#         resultado_pot = potencia_recursiva(base_user, exp_user)
#         print(f"{base_user} elevado a {exp_user} es: {resultado_pot}")

# except ValueError:
#     print("Entrada no válida. Debe ingresar números enteros.")


# # --------------------------------------------------
# # Ejercicio 4: Decimal a Binario
# # --------------------------------------------------

# def decimal_a_binario(n):
#     # Convierte un número decimal a una cadena binaria.
#     # Caso base: cuando el cociente es 0 o 1 
#     if n < 2:
#         return str(n)
#     # Caso recursivo
#     else:
#         # El proceso es: [Recursión con cociente] + [Resto actual]
#         # Esto arma la cadena de abajo hacia arriba
#         cociente = n // 2
#         resto = n % 2
#         return decimal_a_binario(cociente) + str(resto)

# print("\n--- Ejercicio 4: Decimal a Binario ---")
# try:
#     num_dec = int(input("Ingrese un número entero positivo para convertir a binario: "))
    
#     if num_dec < 0:
#         print("Por favor, ingrese un número positivo.")
#     else:
#         resultado_bin = decimal_a_binario(num_dec)
#         print(f"El número {num_dec} en binario es: {resultado_bin}")

# except ValueError:
#     print("Entrada no válida. Debe ingresar un número entero.")


# # --------------------------------------------------
# # Ejercicio 5: Palíndromo 
# # --------------------------------------------------

# def es_palindromo(palabra):
#     # Verifica recursivamente si una palabra es palíndromo.
#     # Casos base:
#     # 1. Si la palabra tiene 0 o 1 letra, es palíndromo.
#     if len(palabra) <= 1:
#         return True
    
#     # Caso recursivo:
#     # Compara la primera y la última letra
#     if palabra[0] != palabra[-1]:
#         return False
#     else:
#         # Llama a la función con la subcadena (sin la primera y sin la última)
#         return es_palindromo(palabra[1:-1])

# print("\n--- Ejercicio 5: Palíndromo ---")
# # Pedimos la palabra y la preparamos (aunque la consigna dice que viene sin espacios/tildes)
# texto_user = input("Ingrese una palabra (sin espacios ni tildes): ").lower().strip()

# if texto_user:
#     if es_palindromo(texto_user):
#         print(f"'{texto_user}' SÍ es un palíndromo.")
#     else:
#         print(f"'{texto_user}' NO es un palíndromo.")
# else:
#     print("No ingresó texto.")


# # --------------------------------------------------
# # Ejercicio 6: Suma de Dígitos 
# # --------------------------------------------------

# def suma_digitos(n):
#     # Suma los dígitos de un número entero positivo recursivamente.
#     # Restricción: No usar strings, solo % y // 
    
#     # Caso base: si es un número de un solo dígito
#     if n < 10:
#         return n
#     # Caso recursivo
#     else:
#         # Suma el último dígito (n % 10) 
#         # con la suma de los dígitos restantes (n // 10)
#         ultimo_digito = n % 10
#         resto_del_numero = n // 10
#         return ultimo_digito + suma_digitos(resto_del_numero)

# print("\n--- Ejercicio 6: Suma de Dígitos ---")
# try:
#     num_suma = int(input("Ingrese un número entero positivo para sumar sus dígitos: "))
    
#     if num_suma < 0:
#         print("Por favor, ingrese un número positivo.")
#     else:
#         resultado_suma = suma_digitos(num_suma)
#         print(f"La suma de los dígitos de {num_suma} es: {resultado_suma}")

# except ValueError:
#     print("Entrada no válida. Debe ingresar un número entero.")


# # --------------------------------------------------
# # Ejercicio 7: Pirámide de Bloques 
# # --------------------------------------------------

# def contar_bloques(n):
#     # Cuenta el total de bloques en una pirámide (n + (n-1) + ... + 1)
#     # Caso base: el último nivel tiene 1 bloque 
#     if n == 1:
#         return 1
#     # Caso recursivo
#     else:
#         # Suma los bloques del nivel actual (n) 
#         # con el total de bloques de los niveles superiores (n-1)
#         return n + contar_bloques(n - 1)

# print("\n--- Ejercicio 7: Pirámide de Bloques ---")
# try:
#     base_piramide = int(input("Ingrese el número de bloques en la base de la pirámide: "))
    
#     if base_piramide < 1:
#         print("La base debe tener al menos 1 bloque.")
#     else:
#         total = contar_bloques(base_piramide)
#         print(f"Una pirámide con {base_piramide} bloques en la base tiene un total de {total} bloques.")

# except ValueError:
#     print("Entrada no válida. Debe ingresar un número entero.")


# # --------------------------------------------------
# # Ejercicio 8: Contar Dígito 
# # --------------------------------------------------

# def contar_digito(numero, digito):
#     """Cuenta cuántas veces aparece un dígito en un número."""
#     # Caso base: si el número es 0, no quedan dígitos por revisar.
#     if numero == 0:
#         # Excepción: si buscamos el 0 en el número 0
#         if digito == 0:
#             return 1 # (Aunque el input suele ser positivo, cubrimos 0)
#         return 0
    
#     # Caso especial para el 0 (ej: 1020)
#     if numero == 0 and digito == 0:
#         return 1

#     # Caso base si el número es positivo y se reduce a 0
#     if numero < 1:
#         return 0

#     # Caso recursivo
#     ultimo = numero % 10
#     resto = numero // 10
    
#     # Comparamos el último dígito
#     if ultimo == digito:
#         # Encontramos 1, más los que haya en el resto
#         return 1 + contar_digito(resto, digito)
#     else:
#         # No encontramos, buscamos en el resto
#         return contar_digito(resto, digito)

# print("\n--- Ejercicio 8: Contar un Dígito ---")
# try:
#     num_grande = int(input("Ingrese el número entero positivo (donde buscar): "))
#     dig_buscado = int(input("Ingrese el dígito (0-9) que desea contar: "))
    
#     if not (0 <= dig_buscado <= 9):
#         print("El dígito a buscar debe estar entre 0 y 9.")
#     elif num_grande < 0:
#          print("El número debe ser positivo.")
#     else:
#         # Caso especial: contar_digito(0, 0)
#         if num_grande == 0 and dig_buscado == 0:
#              veces = 1
#         else:
#              veces = contar_digito(num_grande, dig_buscado)
             
#         print(f"El dígito {dig_buscado} aparece {veces} veces en el número {num_grande}.")

# except ValueError:
#     print("Entrada no válida. Debe ingresar números enteros.")