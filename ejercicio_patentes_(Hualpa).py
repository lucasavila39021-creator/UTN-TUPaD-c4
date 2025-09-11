import string

def generar_patente_aaa000(numero_patente):
    """
    Genera una patente con el formato 'AAA 000' basada en un número de patente.
    El rango de patentes va de 'AAA 000' a 'ZZZ 999'.
    """

    if not 0 <= numero_patente <= 17575999:
        return "El número de patente debe estar entre 0 y 17,575,999."

    # Calcula la parte numérica
    parte_numerica = str(numero_patente % 1000).zfill(3)

    # Calcula la parte alfabética
    valor_letras = numero_patente // 1000
    letras = ''
    alfabeto = string.ascii_uppercase

    for _ in range(3):
        indice = valor_letras % 26
        letras = alfabeto[indice] + letras
        valor_letras //= 26
    
    # Crea la patente final
    patente = f"{letras} {parte_numerica}"
    return patente

# Ejemplo de uso
try:
    numero_ingresado = int(input("Ingresa un número para generar la patente (0 a 17,575,999): "))
    patente_generada = generar_patente_aaa000(numero_ingresado)
    print(f"La patente generada es: {patente_generada}")
except ValueError:
    print("Por favor, ingresa un número entero válido.")

