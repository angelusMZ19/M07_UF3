# Importar las conexiones y la tabla
from connection import *
from creat_table import *
from create import *
from read import *
from update import *
from delete import *

try:
    
    while True:
        #Menú con las opciones a mostrar
        print("Menu: (Selecciona una opción)")
        print("(T) para crear tabla")
        print("(C) para crear un usuario")
        print("(R) para obtener un usuario")
        print("(U) para actualizar un usuario")
        print("(D) para eliminar un usuario")
        print("(-1) para salir")
        
        #Entrada del usuario para escoger opcion del menu
        entrada = input("Ingrese una opción del menú: ")
        entrada = entrada.upper()

        if entrada == 'T':
            # crea la tabla de datos en la BBDD
            create_table()
        elif entrada == 'C':
            #crea los datos de usuarios
            create()
        elif entrada == 'R': 
            # lee los usuario : ingres un id del 1 al 4 a seleccionar si quieres ver todos pon 0
            idUser = input(" \n Introduce Id: ")
            read(idUser)
        elif entrada == 'U':
            #modifica el usuario 
            update()
        elif entrada == 'D':
            #borra los datos de los usuarios por id
            userIdDelete = input("Ingresa el ID que se desea eliminar: ")
            delete(userIdDelete)
        elif entrada == '-1':
            break  # Salir del bucle
        else:
            print("Opción no válida. Intente nuevamente. \n")

except (Exception, psycopg2.Error) as Error:
    print(" \n Error a", Error)#muestra el error en caso de poder acceder al try
finally:
    conn.close()#cerrar connection
