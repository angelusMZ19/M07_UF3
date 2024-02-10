#importa las conecciones
from connection import *

def read(idUser):
    #select mostrar los datos psando el id del usuario
    if idUser != '0':
        select= "SELECT * FROM public.users WHERE user_id = %s"
        connection.execute(select, (idUser))
    else:
        #select para mostrar todos los datos de la tabla
        select= "SELECT * FROM public.users"
        connection.execute(select)

    users = connection.fetchall()#recupera datos de la tabla 
    #itera cada uno de los datos
    for user in users:
        print(user)