#from mysql.connector import MySQLConnection
import mysql.connector
from datos.conexionsql import conexion_BD

class dDetalle:
    def __init__(self):
        self.conn = conexion_BD()

    def obtenerDetalle(self):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("select * from detalle")
            filas = cursor.fetchall()
            return filas
        except Exception as e:
            print("Error al cargar BD WillJos",e)
            return[]
        finally:
            if cursor:
                cursor.close()
        
    def insertarDetalle(self, id_detalle, cantidad, precio_unidad, sub_total, id_proveedor, id_producto):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("insert into detalle(id_detalle, cantidad, precio_unidad, sub_total, id_proveedor, id_producto) values(%s,%s,%s,%s,%s,%s)",(id_detalle, cantidad, precio_unidad, sub_total, id_proveedor, id_producto))            
            self.conn.conexion.commit()
            return True
        except Exception as e:
            print(f"Error al cargar BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()


    def buscarDetalle(self, id_detalle):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("select * from detalle where id_detalle like %s", (f'%{id_detalle}%',))
            encontrado = cursor.fetchall()
            return encontrado
        except Exception as e:
            print("Error al buscar BD WillJos",e)
            return[]
        finally:
            if cursor:
                cursor.close()


    def eliminarDetalle(self, id_detalle):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute('delete from detalle where id_detalle = %s', (id_detalle,))            
            self.conn.conexion.commit()
            return "Exito al eliminar el detalle"
        except Exception as e:
            print(f"Error al eliminar en BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()


    def modificarDetalle(self,  id_detalle, cantidad, precio_unidad, sub_total, id_proveedor, id_producto):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("update detalle set  cantidad = %s, precio_unidad = %s, sub_total = %s, id_proveedor = %s, id_producto = %s where id_detalle = %s",(cantidad, precio_unidad, sub_total, id_proveedor, id_producto, id_detalle))            
            self.conn.conexion.commit()
            return "Exito al modificar el detalle"
        except Exception as e:
            print(f"Error al modificar BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()



# if __name__ =="__main__":
#     objDetalle = dDetalle()

#     #objDetalle.insertarDetalle(5, 7, 180, 1260,3,8)
#     print(objDetalle.eliminarDetalle(1))


