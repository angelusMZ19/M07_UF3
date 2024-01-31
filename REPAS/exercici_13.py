#Demanar a l’usuari un número de l’1 al 10 i mostrar per pantalla la seva taula de multiplicar fins el 10. Exemple: l’usuari marca 3, es mostra per pantalla: 3,6,9,12,15,18,21,24,27 i 30

num = int(input("introduce un numero del 1 al 10 de la tabla que se desee obtener: "))
tupla=(1,2,3,4,5,6,7,8,9,10)
n=1
total=1
 
if 1 <= num <= 10:
    while n <=10:
        total= num*n
        n=n+1
        print(total,end=", ")
if num == 0:
    print("ERROR: tienes que ingresar un numero entre el 1 y el 10")
        

