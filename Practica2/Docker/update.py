#importar las conecciones y la tabla
from connection import *

def update():
    #query update para actualizar los datos de una fila de la columna
    updt= "UPDATE public.users SET user_name='Derek' , user_surname= 'Arandano', user_age= 25, user_email= 'derek@gmail.com', user_telf='698743125' WHERE user_id= 1"

    connection.execute(updt)# ejecucion de la update
    conn.commit()
    print(" \n Actualización exitosa \n ")


