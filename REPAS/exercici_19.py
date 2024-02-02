#Cal buscar la informació que es demana de la següent list:
# areas_pis = [“Menjador”, 10.15, “Rebedor”, 9.56, “Habitació1”, 12.34, “Terrassa”, 15.55, “Lavabo”, 7.98, “Cuina”, 12, “Habitació2”, 12.23]
# (Cal utilitzar els “:” per a que siguin vàlids els prints següents)
# Imprimir el segon element
# Imprimir l’últim element
# Imprimir l’àrea de la terrassa
# Imprimir del primer element al tercer element
# Imprimir del tercer element a l’últim
# Imprimir el total de l'àrea de les dues habitacions
# Modificar l’àrea del lavabo i imprimir la nova list area
# Afegir l'àrea de “pati interior” i 2.78 a les últimes posicions. Imprimir la nova list area.
# Imprimir el total de l’àrea del pis.


area_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

print("Imprimir el segon element: \n", area_pis[1])
print()

print("Imprimir l’últim element: \n", area_pis[-1])
print()

print("Imprimir l’àrea de la terrassa: \n", area_pis[area_pis.index("Terrassa") + 1])
print()

print("Imprimir del primer al tercer element: \n", area_pis[0:3])
print()

print("Imprimir del tercer al últim element: \n",  area_pis[2:])
print()

h1=area_pis[area_pis.index("Habitació1")+1]
h2=area_pis[area_pis.index("Habitació2")+1]
totalH=h1+h2
print("Imprimir total area de las dos habitaciones: \n", totalH)
print()

area_pis[area_pis.index("Lavabo") + 1] = 5.2
print("Nova Modificacio al’àrea del lavabo i imprimir la nova list area: \n", area_pis)
print()

area_pis.extend(["Pati interior", 2.78])
print("Afegir l'àrea de “pati interior” i 2.78 a les últimes posicions: \n",area_pis)
print()

a1=area_pis[area_pis.index("Menjador")+1]
a2=area_pis[area_pis.index("Rebedor")+1]
a3=area_pis[area_pis.index("Habitació1")+1]
a4=area_pis[area_pis.index("Terrassa")+1]
a5=area_pis[area_pis.index("Lavabo")+1]
a6=area_pis[area_pis.index("Cuina")+1]
a7=area_pis[area_pis.index("Habitació2")+1]
a8=area_pis[area_pis.index("Pati interior")+1]
totalA= a1+a2+a3+a4+a5+a6+a7+a8
print("Imprimir el total de l’àrea del pis: ", totalA)
print()

