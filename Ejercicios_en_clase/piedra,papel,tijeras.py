import random

def jugar_con_contador():
    """Juega varias partidas de piedra, papel o tijera con un contador de victorias."""
    opciones = ["piedra", "papel", "tijera"]
    victorias_usuario = 0
    victorias_computadora = 0

    while True:
        # Pide la elección del usuario
        while True:
            try:
                eleccion_usuario = input("\nElige piedra, papel o tijera (o 'salir' para terminar): ").lower()
                if eleccion_usuario == "salir":
                    print("\n¡Gracias por jugar!")
                    print(f"Resultado final: Tú ganaste {victorias_usuario} partidas, la computadora ganó {victorias_computadora} partidas.")
                    return # Finaliza la función
                elif eleccion_usuario in opciones:
                    break
                else:
                    print("Opción no válida. Por favor, elige entre 'piedra', 'papel' o 'tijera'.")
            except ValueError:
                print("Entrada no válida. Por favor, intenta de nuevo.")
        
        # Elección de la computadora
        eleccion_computadora = random.choice(opciones)
        print(f"La computadora eligió: {eleccion_computadora}")

        # Determina el ganador y actualiza los contadores
        if eleccion_usuario == eleccion_computadora:
            print("¡Es un empate!")
        elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijera") or \
             (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
             (eleccion_usuario == "tijera" and eleccion_computadora == "papel"):
            print("¡Ganaste esta ronda!")
            victorias_usuario += 1
        else:
            print("¡Perdiste esta ronda!")
            victorias_computadora += 1
        
        # Muestra el estado actual del contador
        print(f"Puntuación actual: Tú: {victorias_usuario} | Computadora: {victorias_computadora}")

if __name__ == "__main__":
    jugar_con_contador()
