import random

print("Comienza el juego de adivinar el numero entre 0 y 100")

numeroSecreto = random.randrange(100)
userGuess = 101
numeroIntentos = 6

for i in range(numeroIntentos):

    while numeroSecreto != userGuess:

            userGuess = int(input("Jugador, ingrese su numero, dispone de " + str(numeroIntentos - i) +" intentos:"))
            if userGuess > numeroSecreto:
                print("El numero buscado es mas pequeño")
            elif userGuess < numeroSecreto:
                print("El numero buscado es mas grande")
            else:
                print("¡Usted ha acertado! Jugador gana")

