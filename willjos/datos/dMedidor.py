#from mysql.connector import MySQLConnection
import mysql.connector
from datos.conexionsql import conexion_BD

class dMedidor:
    def __init__(self):
        self.conn = conexion_BD()

    def obtenerMedidor(self):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("select * from medidor")
            filas = cursor.fetchall()
            return filas
        except Exception as e:
            print("Error al cargar BD WillJos",e)
            return[]
        finally:
            if cursor:
                cursor.close()
        
    def insertarMedidor(self, codMedidor, direccion):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("insert into medidor(codMedidor, direccion) values(%s,%s)",(codMedidor, direccion))            
            self.conn.conexion.commit()
            return True
        except Exception as e:
            print(f"Error al cargar BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()


    def buscarMedidor(self, direccion):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("select * from medidor where direccion like %s", (f'%{direccion}%',))
            encontrado = cursor.fetchall()
            return encontrado
        except Exception as e:
            print("Error al buscar BD WillJos",e)
            return[]
        finally:
            if cursor:
                cursor.close()


    def eliminarMedidor(self, codMedidor):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute('delete from medidor where codMedidor = %s', (codMedidor,))            
            self.conn.conexion.commit()
            return "Exito al eliminar el medidor"
        except Exception as e:
            print(f"Error al eliminar en BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()


    def modificarMedidor(self, codMedidor, direccion):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("update medidor set direccion = %s where codMedidor = %s",( direccion, codMedidor))            
            self.conn.conexion.commit()
            return "Exito al modificar el medidor"
        except Exception as e:
            print(f"Error al modificar BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()


""" 
if __name__ =="__main__":
    objMedidor = dMedidor()

    # objMedidor.insertarMedidor(4, "buenos aires")
    # objMedidor.insertarMedidor(2, "buenos aires")
    # objMedidor.insertarMedidor(3, "buenos aires")       
    print(objMedidor.eliminarMedidor())

 """