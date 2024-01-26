# Demanar a l'usuari que introdueixi entre 1 i 3 paraules y que muestre el caracter incial y final 
paraules = input("Introduce de 1 a 3 palabras separadas por espacios: ")

paraulaSeparadas = paraules.split()


if 1 <= len(paraulaSeparadas) <= 3:
    for paraula in paraulaSeparadas:
      
        print("palabras:", paraula)
        
       
        numeroCaracteres = len(paraula)
        print("Numero de caràcters:", numeroCaracteres)
       
        primerChar = paraula[0]
        ultimChar = paraula[-1]
        print("Primer caràcter: ", primerChar)
        print("Último caràcter: ", ultimChar)
        
        print("__________________________________")

else:
    print("Introduce de 1 a 3 palabras separadas por espacios:")
