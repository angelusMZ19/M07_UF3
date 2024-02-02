# El mateix que l’anterior exercici, però sense demanar un màxim de números. L’usuari indicarà quan ha acabat posant un 0.
# numeros = []
# while True:
#     try:
#         entrada = input("Introduce un numero y (0 para salir): ")
#         num = int(entrada)
#         if num == 0:
#             break
#         numeros.append(num)
    
#     except ValueError:
#         print("ERROR: Entrada no vàlida. porfavor introduzca un NUMERO")
# print("Numero introducidos:", numeros)

numeros = []
while True:
    
        entrada = input("Introduce un numero y (0 para salir): ")
        num = int(entrada)
        if num == 0:
            break
        numeros.append(num)
    
print("Numero introducidos:", numeros)
