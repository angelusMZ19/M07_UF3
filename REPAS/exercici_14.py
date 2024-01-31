#Demanar a l’usuari que introdueixi 10 números separats per un espai. Al acabar, el programa els introduirà en una tupla i els ordenarà (major o menor, com volgueu), mostrant per pantalla el contingut de la tupla.
#sorted se usa para ordenar y el reverse=True es para hacerlo de forma inversa es decir de major a menor
entrada=input("introduce 10 valores separados por espacios")

numeros = [int(num) for num in entrada.split()]
tupla = tuple(numeros)
ordenado = tuple(sorted(tupla, reverse=True))

print("Tupla ordenada de major a menor:", ordenado)
