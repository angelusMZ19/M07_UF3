# Demanar a l’usuari que posi 10 números separats per espais. Afegir aquests números a una llista. Calcular la suma de tots els números i la seva mitjana i afegir aquests 2 números a la llista. Mostrar per pantalla la llista.
# Exemple mostra per pantalla.
# Números de l’usuari:
# suma total:
# mitjana:

entrada = input("Introduce 10 numeros seprados por espacios ")
numbs = list(entrada.split(" "))
sumaTotal = 0
for num in numbs:
    sumaTotal += int(num)
media = sumaTotal / len(numbs)

print("\nNúmeros del usuario:", numbs)
print("Suma total:", sumaTotal)
print("Media:", media)
