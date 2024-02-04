#Crear una funció que passats dos números per paràmetre (demanats a l’usuari) ens mostri per pantalla un número aleatori entre aquests dos números.


import random

def numBiRandom(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1 
    rand = random.uniform(num1, num2)
    return rand
