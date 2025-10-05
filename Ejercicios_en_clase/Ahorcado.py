# Juego del Ahorcado en Python
##Ejercicio en clase – Funciones
#Crea un juego interactivo del ahorcado en Python. El juego debe seleccionar una palabra al
#azar de una lista de palabras predefinidas y permitir que el jugador adivine la palabra letra por
#letra. El jugador tiene un número limitado de intentos antes de perder el juego.
#Requisitos:
# Define una lista de palabras que el programa pueda elegir al azar para que el jugador
#adivine. Puedes usar palabras relacionadas con la programación, tecnología o
#cualquier tema que te guste.
# El programa debe seleccionar una palabra al azar de la lista para cada partida.
# El juego debe mostrar el estado actual de la palabra oculta con guiones bajos (_) que
#representan las letras no adivinadas y las letras adivinadas deben mostrarse en su
#lugar correspondiente.
# El jugador debe poder ingresar una letra adivinada en cada turno.
# El programa debe verificar si la letra adivinada está en la palabra secreta y actualizar el
#tablero en consecuencia.
# El jugador tiene un número limitado de intentos (por ejemplo, 6) antes de perder el
#juego.
# Muestra mensajes informativos al jugador, como "Adivinaste una letra correctamente"
#o "Letra incorrecta, te quedan X intentos".
# El juego debe terminar cuando el jugador adivina todas las letras o se quedan sin
#intentos.
# Proporciona un mensaje de victoria si el jugador adivina la palabra y un mensaje de
#derrota si se quedan sin intentos.
#consideraciones adicionales:
# Puedes utilizar funciones para organizar tu código de manera efectiva.
# Agrega comentarios para explicar el funcionamiento de tu código
##como agregado puedes ir mostrando una figura del ahorcado con cada error que va cometiendo el usuario.
import random

def mostrar_ahorcado(intentos):
    estados = [
        """
           +---+
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    print(estados[intentos])


# --- Juego principal ---
palabras = ["PYTHON", "AHORCADO", "PROGRAMAR", "JUEGO", "COMPUTADORA", "INTELIGENCIA"]
palabra = random.choice(palabras)
letras_adivinadas = ["_"] * len(palabra)
intentos_fallidos = 0
letras_usadas = []

print("¡Bienvenido al juego del Ahorcado!\n")

# Mostrar el muñeco al inicio (sin fallos)
mostrar_ahorcado(intentos_fallidos)
print("Palabra:", " ".join(letras_adivinadas), "\n")

# Bucle del juego
while intentos_fallidos < 6 and "_" in letras_adivinadas:
    print("Letras usadas:", ", ".join(letras_usadas))
    letra = input("Adivina una letra: ").upper()

    # Evitar repetir letras
    if letra in letras_usadas:
        print("Ya usaste esa letra. Intenta otra.\n")
        continue
    letras_usadas.append(letra)

    # Verificar si la letra está en la palabra
    if letra in palabra:
        for i, l in enumerate(palabra):
            if l == letra:
                letras_adivinadas[i] = letra
        print("\n¡Bien hecho! Adivinaste una letra.")
    else:
        intentos_fallidos += 1
        print(f"\n Fallaste. Te quedan {6 - intentos_fallidos} intentos.")

    # Mostrar el muñeco y el progreso después de cada intento
    mostrar_ahorcado(intentos_fallidos)
    print("Palabra:", " ".join(letras_adivinadas), "\n")

# Fin del juego
if "_" not in letras_adivinadas:
    print("\n ¡Felicidades! Adivinaste la palabra:", palabra)
else:
    print("\n Has perdido. La palabra era:", palabra)
    mostrar_ahorcado(6)





