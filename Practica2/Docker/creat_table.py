#usado para importar la conexion que tengo establecida en otro archivo 
from connection import connection, conn

#para crear la tabla
sql= '''CREATE TABLE USERS(
                user_id SERIAL PRIMARY KEY,
                user_name VARCHAR(255) NOT NULL,
                user_surname VARCHAR(255) NOT NULL,
                user_age BIGINT NOT NULL,
                user_email VARCHAR(255) NOT NULL,
                user_telf VARCHAR(255) NOT NULL
)''' 
print(sql)
connection.execute(sql)
print(connection)
conn.commit()