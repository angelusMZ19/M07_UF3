
numUser = int(input("Introdueix un número entre 10 i 100: "))

if 10 <= numUser <= 100:

    tuplaNum = tuple(range(1, numUser + 1))

    print("Tupla con numeros del 1 hasta el ", numUser, ":", tuplaNum)
else:
    print("Porfavor introsuce un numero valido dentro del rango que se ha especificado 1 al 100: ")
