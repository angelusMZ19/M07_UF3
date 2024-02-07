import psycopg2

conn= psycopg2.connect(
    database="dbangelo",
    user="angelo",
    password="angelo",
    host="db",
    port='5432'
)
connection= conn.cursor()

print(connection)
