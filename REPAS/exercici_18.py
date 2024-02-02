#Demanar a l’usuari posar 2 paraules. Afegir aquestes a una tupla i mostrar per pantalla quantes vegades apareix cada lletra.


p1 = input("Introduzca la primera palabra: ")
p2 = input("Introduzca la segunda palabra: ")

palabrita = p1 + p2

contaLetra = {}

for letra in palabrita:
    letra = letra.lower()
    if letra not in contaLetra:
        contaLetra[letra] = 1
    else:
        contaLetra[letra] += 1


for letra, count in contaLetra.items():
    print(f"La letra '{letra}' aparece {count} veces en las palabras")