# Igual que l’anterior però a la tupla afegir la frase sense els caràcters repetits i mostrar el contingut de la tupla. Exemple: Usuari indica la paula caracteristica. Es mostra per pantalla carteis.

frase = input("Introduce una frase: ")
sinSpace = frase.replace(" ", "")

anyReplicados = []
for char in sinSpace:
    if char not in anyReplicados:
        anyReplicados.append(char)

palabras = tuple(anyReplicados)
print("Contenido de la tupla: ", palabras)
