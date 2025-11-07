#from mysql.connector import MySQLConnection
import mysql.connector
from datos.conexionsql import conexion_BD

class dVenta:
    def __init__(self):
        self.conn = conexion_BD()

    def obtenerVenta(self):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("select * from venta")
            filas = cursor.fetchall()
            return filas
        except Exception as e:
            print("Error al cargar BD WillJos",e)
            return[]
        finally:
            if cursor:
                cursor.close()
        
    def insertarVenta(self, id_venta, fecha, total, forma_pago, id_cliente):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("insert into venta(id_venta, fecha, total, forma_pago, id_cliente) values(%s,%s,%s,%s,%s)",(id_venta, fecha, total, forma_pago, id_cliente))            
            self.conn.conexion.commit()
            return True
        except Exception as e:
            print(f"Error al cargar BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()


    def buscarVenta(self, id_venta):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("select * from venta where id_venta like %s", (f'%{id_venta}%',))
            encontrado = cursor.fetchall()
            return encontrado
        except Exception as e:
            print("Error al buscar BD WillJos",e)
            return[]
        finally:
            if cursor:
                cursor.close()


    def eliminarVenta(self, id_venta):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute('delete from venta where id_venta = %s', (id_venta,))            
            self.conn.conexion.commit()
            return "Exito al eliminar el venta"
        except Exception as e:
            print(f"Error al eliminar en BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()


    def modificarVenta(self, id_venta, fecha, total, forma_pago, id_cliente):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("update venta set fecha = %s,total = %s, forma_pago = %s, id_cliente = %s where id_venta = %s",(fecha, total, forma_pago, id_cliente, id_venta))            
            self.conn.conexion.commit()
            return "Exito al modificar venta"
        except Exception as e:
            print(f"Error al modificar BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()


""" 
if __name__ =="__main__":
    objVenta = dVenta()
   
    print(objVenta.eliminarVenta())

"""
    # objVenta.insertarVenta(2, "2025-10-6", 1000, "efectivo", 1)
    # objVenta.insertarVenta(3, "2025-9-6", 2000, "efectivo", 101)
    # objVenta.insertarVenta(4, "2025-8-6", 3000, "efectivo", 102)
    # objVenta.insertarVenta(5, "2025-7-6", 3000, "efectivo", 103)
    # objVenta.insertarVenta(6, "2025-7-6", 4000, "efectivo", 104)
    # objVenta.insertarVenta(7, "2025-5-6", 5000, "efectivo", 105)
    # objVenta.insertarVenta(8, "2025-4-6", 7000, "efectivo", 107)
    # objVenta.insertarVenta(9, "2025-3-6", 8000, "efectivo", 108)
    # objVenta.insertarVenta(10, "2025-2-6", 9000, "efectivo", 109)
 


