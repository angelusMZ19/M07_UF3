# Importar las conexiones y la tabla
from connection import *

#metodo para elimanr
def delete(user_id):
    #query para eleiminar un usuario por id
    delete = "DELETE FROM public.users WHERE user_id = %s"
    connection.execute(delete, (user_id,)) #ejecucion la orden con el id del ususario
    conn.commit()
    print(" \n Eliminación exitosa \n")


