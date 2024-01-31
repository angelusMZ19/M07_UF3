#Crear una tupla amb els mesos de l’any. Demanar a l’usuari que posi un número entre 0 i 12 i mostrar per pantalla el mes corresponent al número indicat per l’usuari. El programa finalitza només quan l’usuari posa 0.
mesAnyo=("","enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre ")

while True:
    
    nMes = int(input("Introsuce un numero entre el 1 y el 12 (o 0 para salir): "))

    if nMes == 0:
        print("---------Adios----------")
        break
    if 1 <= nMes <= 12:
        
        print("El mes és:", mesAnyo[nMes])
    else:
        print("Error: Introsuce un numero entre el 1 y el 12 (o 0 para salir):")
