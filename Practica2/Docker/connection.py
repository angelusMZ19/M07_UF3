import psycopg2
#datos de la base de dato para la coneccion 
conn= psycopg2.connect(
    database="dbangelo",
    user="angelo",
    password="angelo",
    host="localhost",
    port='5432'
)
connection= conn.cursor()

print(connection)
