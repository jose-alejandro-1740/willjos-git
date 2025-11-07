#from mysql.connector import MySQLConnection
import mysql.connector
from datos.conexionsql import conexion_BD

class dProyecto:
    def __init__(self):
        self.conn = conexion_BD()

    def obtenerProyecto(self):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("select * from proyecto")
            filas = cursor.fetchall()
            return filas
        except Exception as e:
            print("Error al cargar BD WillJos",e)
            return[]
        finally:
            if cursor:
                cursor.close()
        
    def insertarProyecto(self, id_proyecto, nombre, direccion, f_proyecto, descuento, total, id_cliente):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("insert into proyecto(id_proyecto, nombre, direccion, f_proyecto, descuento, total, id_cliente) values(%s,%s,%s,%s,%s,%s,%s)",(id_proyecto, nombre, direccion, f_proyecto, descuento, total, id_cliente))            
            self.conn.conexion.commit()
            return True
        except Exception as e:
            print(f"Error al cargar BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()


    def buscarProyecto(self, nombre_proyecto):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("select * from proyecto where nombre like %s", (f'%{nombre_proyecto}%',))
            encontrado = cursor.fetchall()
            return encontrado
        except Exception as e:
            print("Error al buscar BD WillJos",e)
            return[]
        finally:
            if cursor:
                cursor.close()


    def eliminarProyecto(self, id_proyecto):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute('delete from proyecto where id_proyecto = %s', (id_proyecto,))            
            self.conn.conexion.commit()
            return "Exito al eliminar el proyecto"
        except Exception as e:
            print(f"Error al eliminar en BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()


    def modificarProyecto(self, id_proyecto, nombre, direccion, f_proyecto, descuento, total, id_cliente):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("update proyecto set nombre = %s, direccion = %s, f_proyecto = %s, descuento = %s, total = %s, id_cliente = %s where id_proyecto = %s",(nombre, direccion, f_proyecto, descuento, total, id_cliente,id_proyecto))            
            self.conn.conexion.commit()
            return "Exito al modificar el proyecto"
        except Exception as e:
            print(f"Error al modificar BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()


""" 
if __name__ =="__main__":
    objProyecto = dProyecto()

    print(objProyecto.eliminarProyecto())
"""
""" 
    objProyecto.insertarProyecto(2,"senkata 2", "sencata las bajo", "2024-10-01", 1000, 11000, 1)
    objProyecto.insertarProyecto(3,"senkata 1", "sencata las medio", "2024-9-01", 1000, 11000, 102)
    objProyecto.insertarProyecto(4,"senkata 13", "sencata las alto", "2024-1-01", 1000, 11000, 103)
    objProyecto.insertarProyecto(5,"senkata 1", "sencata las intermedio", "2024-3-01", 1000, 11000, 105)
    objProyecto.insertarProyecto(6,"senkata 2", "sencata las bajo", "2024-3-01", 1000, 11000, 107)
    objProyecto.insertarProyecto(7,"senkata 5", "llojeta", "2024-10-01", 1000, 11000, 105)
    objProyecto.insertarProyecto(8,"senkata 6", "llojeta las nievas", "2024-5-01", 1000, 11000, 107)
    objProyecto.insertarProyecto(9,"senkata 7", "llojeta las bajo", "2024-7-01", 1000, 11000, 107)
"""

