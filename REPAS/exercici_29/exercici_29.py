

def mostraSumaNum(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1

    numeros_enteros = list(range(int(num1) + 1, int(num2)))
    suma = sum(numeros_enteros)

    print("Números enteros entre " ,num1," y ",num2," son: ", numeros_enteros)
    print("La suma de estos números enteros es:",suma)
