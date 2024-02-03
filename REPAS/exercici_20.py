#Crear un diccionari on la clau (key) sigui un nom i el valor (value) l’edat. S’haura de demanar a l’usuari que posi contactes (noms i edats). Si algun nom es repeteix no s’fageirà al diccionari (indicant-ho a l’usuari). Es deixarà d’inserir contactes quan l’usuari indiqui que no vol afegir-ne més.

myAgend={}
while True:
    nom=input("Ingrese un nombre (stop para finalizar o -1)")

    if nom=="stop" or nom=="-1":
        break
    if nom in myAgend:
        print("Nombre ya registrado, porfavor, Ingrese un nuevo registro")
    else: 
        edad=(input("Ingrese edad del agendado: "))
        if edad.isdigit():
            myAgend[nom]=edad
        else:
            print("Por favor ingrese una edad valida")

for nom , edad in myAgend.items():
    print(nom , " : " , edad , " años")

