#import para poder usar los archivos individuales, y conectarlo por medio del main 
import psycopg2
#from creat_table import sql
from connection import *

def menu():
        print("Menu:(Selecciona una opcion)")
        print("(C) para crear un usuario")
        print("(R) para obtener un usuario")
        print("(U) para actualizar un usuario")
        print("(D) para eliminar un usuario")
        print("(S) para eliminar un usuario")
    
def run():
    entrada=input("Ingrese una opcion del menu")
    entrada=entrada.upper()
    if entrada == 'C':
        pass
    elif entrada=='R':
        pass
    elif entrada=='U':
        pass
    elif entrada=='D':
        pass
    elif entrada=='S':
        exit
        
try:
   
            

    connection


except(Exception, psycopg2.Error)as Error:
    print("Error", Error)
finally:
    connection.close()

