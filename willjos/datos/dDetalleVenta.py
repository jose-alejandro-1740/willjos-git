#from mysql.connector import MySQLConnection
import mysql.connector
from datos.conexionsql import conexion_BD

class dDetalleVenta:
    def __init__(self):
        self.conn = conexion_BD()

    def obtenerDetalleVenta(self):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("select * from detalle_venta")
            filas = cursor.fetchall()
            return filas
        except Exception as e:
            print("Error al cargar BD WillJos",e)
            return[]
        finally:
            if cursor:
                cursor.close()
        
    def insertarDetalleVenta(self, id_detventa, cantidad, precio_unidad, sub_total, id_venta, id_producto):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("insert into detalle_venta(id_detventa, cantidad, precio_unidad, sub_total, id_venta, id_producto) values(%s,%s,%s,%s,%s,%s)",(id_detventa, cantidad, precio_unidad, sub_total, id_venta, id_producto))            
            self.conn.conexion.commit()
            return True
        except Exception as e:
            print(f"Error al cargar BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()


    def buscarDetalleVenta(self, id_detventa):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("select * from detalle_venta where id_detventa like %s", (f'%{id_detventa}%',))
            encontrado = cursor.fetchall()
            return encontrado
        except Exception as e:
            print("Error al buscar BD WillJos",e)
            return[]
        finally:
            if cursor:
                cursor.close()


    def eliminarDetalleVenta(self, id_detventa):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute('delete from detalle_venta where id_detventa = %s', (id_detventa,))            
            self.conn.conexion.commit()
            return "Exito al eliminar detalle de venta"
        except Exception as e:
            print(f"Error al eliminar en BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()


    def modificarDetalleVenta(self, id_detventa, cantidad, precio_unidad, sub_total, id_venta, id_producto):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("update detalle_venta set cantidad = %s, precio_unidad = %s, sub_total = %s, id_venta = %s, id_producto = %s where id_detventa = %s",(cantidad, precio_unidad, sub_total, id_venta, id_producto, id_detventa))            
            self.conn.conexion.commit()
            return "Exito al modificar el detalle de venta"
        except Exception as e:
            print(f"Error al modificar BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()

""" 
if __name__ =="__main__":
    objDetalleVenta = dDetalleVenta()

    print(objDetalleVenta.insertarDetalleVenta(11,"10","30","8300",1,2))
 """
    # objDetalleVenta.insertarDetalleVenta(2,"10","30","1000",1,2)
    # objDetalleVenta.insertarDetalleVenta(3,"10","30","2000",2,3)
    # objDetalleVenta.insertarDetalleVenta(4,"10","30","3000",3,5)
    # objDetalleVenta.insertarDetalleVenta(5,"10","30","4000",4,5)
    # objDetalleVenta.insertarDetalleVenta(6,"10","30","5000",5,7)
    # objDetalleVenta.insertarDetalleVenta(7,"10","30","7000",7,8)
    # objDetalleVenta.insertarDetalleVenta(8,"10","30","7000",8,5)
    # objDetalleVenta.insertarDetalleVenta(9,"10","30","8000",9,7)
    # objDetalleVenta.insertarDetalleVenta(10,"10","30","8300",10,8)
    


