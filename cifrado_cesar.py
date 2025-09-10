def cifrado_cesar(texto, corrimiento):
    """Cifra un texto usando el cifrado César."""
    resultado = ""
    for caracter in texto:
        if 'a' <= caracter.lower() <= 'z':
            inicio = ord('a') if caracter.islower() else ord('A')
            caracter_cifrado = chr((ord(caracter) - inicio + corrimiento) % 26 + inicio)
            resultado += caracter_cifrado
        else:
            resultado += caracter
    return resultado

mensajes_cifrados = []
try:
    corrimiento_deseado = int(input("Ingrese el corrimiento deseado para el cifrado (un número entero): "))
    if corrimiento_deseado < 0:
        print("El corrimiento debe ser un número positivo.")
    else:
        for i in range(5):
            mensaje = input(f"Ingrese el mensaje {i+1}: ")
            mensaje_cifrado = cifrado_cesar(mensaje, corrimiento_deseado)
            mensajes_cifrados.append(mensaje_cifrado)

        print("\nMensajes Cifrados:")
        for i, mensaje_cifrado in enumerate(mensajes_cifrados):
            print(f"Mensaje {i+1} cifrado: {mensaje_cifrado}")
except ValueError:
    print("Entrada inválida. Por favor, ingrese un número entero para el corrimiento.")
