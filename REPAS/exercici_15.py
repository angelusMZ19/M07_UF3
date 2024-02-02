# El mateix que l’anterior exercici, però sense demanar un màxim de números. L’usuari indicarà quan ha acabat posant un 0.

numeros = []
while True:
    
        entrada = input("Introduce un numero y (0 para salir): ")
        num = int(entrada)
        if num == 0:
            break
        numeros.append(num)
    
print("Numero introducidos:", numeros)
