#usado para importar la conexion que tengo establecida en otro archivo 
from connection import *

#para crear la tabla
def create_table():
    drop= "DROP TABLE IF EXISTS USERS"
    sql= '''CREATE TABLE USERS(
                    user_id SERIAL PRIMARY KEY,
                    user_name VARCHAR(255) NOT NULL,
                    user_surname VARCHAR(255) NOT NULL,
                    user_age BIGINT NOT NULL,
                    user_email VARCHAR(255) NOT NULL,
                    user_telf VARCHAR(255) NOT NULL
    )''' 
    print(drop)
    print(sql)
    connection.execute(drop)#ejecucion de el drop 
    connection.execute(sql)#ejecucion para crear tabla
    conn.commit()
    print(" \n creacion tabla exitoso \n")

