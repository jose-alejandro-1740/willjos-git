#from mysql.connector import MySQLConnection
import mysql.connector
from datos.conexionsql import conexion_BD

# conewxion a tb Producto
class dProducto:
    def __init__(self):
        self.conn = conexion_BD()

    def obtenerProducto(self):
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("select * from producto")
            filas = cursor.fetchall()
            return filas
        except Exception as e:
            print("Error al cargar BD WillJos",e)
            return[]
        finally:
            if cursor:
                cursor.close()
        
    def insertarProducto(self, id_producto, nombre, descripcion, ancho, alto, precio):
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("insert into producto(id_producto, nombre, descripcion, ancho, alto, precio) values(%s,%s,%s,%s,%s,%s)",(id_producto, nombre, descripcion, ancho, alto, precio))            
            self.conn.conexion.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Error al cargar BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()


    def buscarProducto(self, nombreProducto):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("select * from producto where nombre like %s", (f'%{nombreProducto}%',))
            encontrado = cursor.fetchall()
            return encontrado
        except Exception as e:
            print("Error al buscar BD WillJos",e)
            return[]
        finally:
            if cursor:
                cursor.close()


    def eliminarProducto(self, id_producto):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute('delete from producto where id_producto = %s', (id_producto,))            
            self.conn.conexion.commit()
            return "Exito al eliminar el producto"
        except Exception as e:
            print(f"Error al eliminar en BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()


    def modificarProducto(self, id_producto, nombre, descripcion, ancho, alto, precio):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("update  producto set  nombre = %s, descripcion = %s, ancho = %s, alto = %s, precio = %s where id_producto = %s",(nombre, descripcion, ancho, alto, precio, id_producto))            
            self.conn.conexion.commit()
            return "Exito al modificar el producto "
        except Exception as e:
            print(f"Error al modificar BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()



# if __name__ =="__main__":
#     objProducto = dProducto()

#     #objProducto.insertarProducto(5,"aluminio","Natural s 20","6.00 mt","0.20 cm",220.00)
#     print(objProducto.eliminarProducto())


