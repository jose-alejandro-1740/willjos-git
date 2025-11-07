#from mysql.connector import MySQLConnection
import mysql.connector
from datos.conexionsql import conexion_BD

class dCliente:
    def __init__(self):
        self.conn = conexion_BD()

    def obtenerCliente(self):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("select * from cliente")
            filas = cursor.fetchall()
            return filas
        except Exception as e:
            print("Error al cargar BD WillJos",e)
            return[]
        finally:
            if cursor:
                cursor.close()
        
    def insertarCliente(self, id_cliente, nombre, ap_paterno, ap_materno, direccion, telefono):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("insert into cliente(id_cliente, nombre, ap_paterno, ap_materno, direccion, telefono) values(%s,%s,%s,%s,%s,%s)",(id_cliente, nombre, ap_paterno, ap_materno, direccion, telefono))            
            self.conn.conexion.commit()
            return True
        except Exception as e:
            print(f"Error al cargar BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()


    def buscarCliente(self, nombre_Cliente):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("select * from cliente where nombre like %s", (f'%{nombre_Cliente}%',))
            encontrado = cursor.fetchall()
            return encontrado
        except Exception as e:
            print("Error al buscar BD WillJos",e)
            return[]
        finally:
            if cursor:
                cursor.close()


    def eliminarCliente(self, id_cliente):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute('delete from cliente where id_cliente = %s', (id_cliente,))            
            self.conn.conexion.commit()
            return "Exito al eliminar el cliente"
        except Exception as e:
            print(f"Error al eliminar en BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()


    def modificarCliente(self, id_cliente, nombre, ap_paterno, ap_materno, direccion, telefono):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("update cliente set nombre = %s, ap_paterno = %s, ap_materno = %s, direccion = %s, telefono = %s where id_cliente = %s",(nombre, ap_paterno, ap_materno, direccion, telefono, id_cliente))            
            self.conn.conexion.commit()
            return "Exito al modificar el cliente"
        except Exception as e:
            print(f"Error al modificar BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()


""" 
if __name__ =="__main__":
    objCliente = dCliente()

     #objCliente.buscarCliente("jose")
    print(objCliente.obtenerCliente())

"""