#Demanar a l’usuari que introdueixi un valor en €, seguidament demanar que introdueixi el IVA a aplicar-hi (4%, 10% o 21%) i finalment mostrar, per pantalla, el resultat del valor indicat per l’usuari, el % d’IVA demanat per l’usuari i el valor final amb l’IVA afegit

valor=int(input("añade un valor en €"))#para convertir colocar el tipo antes del input
iva=int(input("añade el iva a aplicar %"))

print(valor)
print(iva)
precio_final = valor * (1 + iva / 100)
print(precio_final)

