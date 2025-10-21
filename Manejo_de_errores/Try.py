def dividir():
    while True:
        try:
            x=int(input("Ingrese un número: "))
            div=10/x
        except ValueError  as e:
            print("Error: Debe ingresar un número entero.")
            print(e)
            continue
        except ZeroDivisionError as e:
            print("Error: No se puede dividir por cero. Pero jamás en la vida.")
            print(e)
            continue
        except Exception as e:
            print("Error inesperado.")
            print(e)
            continue
        else:
            print(f"10 dividido por {x} es {div}")
            break
        finally:
            print("Ejecución delprogrma finalizada.")

dividir()
# Ejemplo de manejo de errores con try, except, else y finally