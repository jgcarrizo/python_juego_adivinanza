import random

def juego_adivinanza():
    # Generar un número del 1 al 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("Bienvenido al juego de adivinanza de números")
    print("Debes adivinar un número del 1 al 100")

    while not adivinado:
        # Solicitamos un número
        adivinanza = input("Introduce un número del 1 al 100: ")

        # Verificar que la entrada sea un número
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)  # Convertir de texto a entero
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El número secreto es mayor que {adivinanza}.")
            elif adivinanza > numero_secreto:
                print(f"El número secreto es menor que {adivinanza}.")
            else:
                print(f"¡Felicidades! Has ganado. El número {adivinanza} es el secreto y lo has adivinado en {intentos} intentos.")
                adivinado = True

        else:
            print("Por favor, introduce un número válido entre el 1 y el 100.")

juego_adivinanza()