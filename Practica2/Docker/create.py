#importar las conecciones y la tabla
from connection import *

def crea():
    insert= "INSERT INTO public.users(user_name, user_surname, user_age, user_email, user_telf)VALUES (%s,%s, %s,%s,%s)"

    usuario=[
        ("Angelo", "Montenegro", 20, "angelo@gmail.com", "659275193"),
        ("Jaime", "Castro", 40, "jaime@gmail.com", "954872593"),
        ("Javier", "Zavala", 37, "javier@gmail.com", "123456789"),
        ("Pedro", "Carrion", 26, "pedro@gmail.com", "987456321")
    ]
    for i in usuario:
        connection.execute(insert,i)
        conn.commit()

print("exitoso")
crea()