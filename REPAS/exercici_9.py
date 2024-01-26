# Demanar a l’usuari que posi dues paraules. Al executar el programa, mostrarà per pantalla les dues paraules amb els dos primers caràcters de cada paraula intercanviats. Exemple: Quatre Camins passaria a Caatre Qumins.

palabras = input("Introduce 2 palabras separadas por espacios: ")

palabritas = palabras.split()
a= palabritas[0]
b= palabritas[1]
print(b[:1]+a[1:], a[:1]+b[1:])
