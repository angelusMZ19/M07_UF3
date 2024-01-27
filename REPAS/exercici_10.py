#Crear un arxiu on caldrà endevinar el número escollit pel programa entre 1 i 100. Cada vegada que l’usuari hi posi un número, caldrà indicar si és més petit o més gran fins que encerti i el missatge haurà d’indicar que ha encertat. Indicar també el número d’intents.
import random


numero_secret = random.randint(1, 100)
intents = 0

print("Adivina el numero entre el 1 y el 100")

while True:
    posibilidad = int(input("Introduce un numero "))
    intents += 1

    if posibilidad == numero_secret:
        print("Felicidades has adivinado :v ")
        print("Numero de intentos", intents)
        break
    elif posibilidad < numero_secret:
        print("El numero es mas GRANDE que" , posibilidad ,  " vuelve a intentarlo")
    else:
        print("El numero es mas PEQUEÑO que" , posibilidad ,  " vuelve a intentarlo")
