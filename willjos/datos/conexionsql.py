import mysql.connector
from mysql.connector import connect, Error

class conexion_BD:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
            user="root",
            password="",
            host="127.0.0.1",
            database="willjose",
            port="3306"
            )   # ES Atributos de la Clase
            if self.conexion.is_connected():
                print(" Conexion exitosa a BD sejo  te mereces repasar mas. ")

        except Error as error:
            print(' Error en la conexion con BD, chacra , vuelve a intentar : {}'.format(error))
            self.conexion = None    # ES Atributos de la Clase

#conexion_BD1 = conexion_BD()
#print(conexion_BD1)