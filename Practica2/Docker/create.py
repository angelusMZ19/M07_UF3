#importar las conecciones y la tabla
from creat_table import *

print("AGREGAR NUEVO USUARIO")

id=input("Id: ")
name=input("Nombre: ")
surname=input("Apellido: ")
age =input("Edad: ")
email=input("Correo: ")
telefono=input("Telefono: ")

insert= "Insert into users(user_id, user_name, user_surname, user_age, user_email, user_telf)VALUES(id, name, surname, age, email, telefono)"

