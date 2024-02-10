#importa las conecciones
from connection import *

def create():
    #consulta insert a la base de datos
    insert= "INSERT INTO public.users(user_name, user_surname, user_age, user_email, user_telf)VALUES (%s,%s, %s,%s,%s)"

    #insert de datos para la consulta anterior
    usuario=[
        ("Angelo", "Montenegro", 20, "angelo@gmail.com", "659275193"),
        ("Jaime", "Castro", 40, "jaime@gmail.com", "954872593"),
        ("Javier", "Zavala", 37, "javier@gmail.com", "123456789"),
        ("Pedro", "Carrion", 26, "pedro@gmail.com", "987456321")
    ]
    for i in usuario:
        #ejecucion y commit d cada ejecucion de los datos
        connection.execute(insert,i)
        conn.commit()
    print("\n Creacion Exitosa \n")
