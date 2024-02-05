

def calcularIVA(cantidad, iva):
    if (iva==4 or iva==10 or iva==21):
        iva = iva
    else: 
        iva=21

    total = cantidad * (1 + iva / 100)
    print("Importe sin IVA:", cantidad, "euros")
    print("IVA: ", iva,"%")
    print("Total con IVA:",  str(round(total, 2)), "euros")