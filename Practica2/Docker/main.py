#import para poder usar los archivos individuales, y conectarlo por medio del main 
import psycopg2
from creat_table import sql
from connection import *

try:
    connection

except(Exception, psycopg2.Error)as Error:
    print("Error", Error)
finally:
    connection.close()

