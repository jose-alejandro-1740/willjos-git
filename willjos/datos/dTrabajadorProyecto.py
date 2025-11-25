#from mysql.connector import MySQLConnection
import mysql.connector
from datos.conexionsql import conexion_BD

class dTrabajadorProyecto:
    def __init__(self):
        self.conn = conexion_BD()

    def obtenerTrabajadorProyecto(self):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("select * from trabajador_proyecto")
            filas = cursor.fetchall()
            return filas
        except Exception as e:
            print("Error al cargar BD WillJos",e)
            return[]
        finally:
            if cursor:
                cursor.close()
        
    def insertarTrabajadorProyecto(self, id_trabajador, id_proyecto, rol):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("insert into trabajador_proyecto(id_trabajador, id_proyecto, rol) values(%s,%s,%s)",(id_trabajador, id_proyecto, rol))            
            self.conn.conexion.commit()
            return True
        except Exception as e:
            print(f"Error al cargar BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()


    def buscarTrabajadorProyecto(self, id_proyecto):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("select * from trabajador_proyecto where id_proyecto like %s", (f'%{id_proyecto}%',))
            encontrado = cursor.fetchall()
            return encontrado
        except Exception as e:
            print("Error al buscar BD WillJos",e)
            return[]
        finally:
            if cursor:
                cursor.close()


    def eliminarTrabajadorProyecto(self, id_trabajador):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute('delete from trabajador_proyecto where id_trabajador = %s', (id_trabajador,))            
            self.conn.conexion.commit()
            return "Exito al eliminar datos de la tabla trabajador proyecto "
        except Exception as e:
            print(f"Error al eliminar en BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()


    def modificarTrabajadorProyecto(self, id_trabajador, id_proyecto, rol):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("UPDATE trabajador_proyecto SET rol = %s WHERE id_trabajador = %s AND id_proyecto = %s", (rol, id_trabajador, id_proyecto))
            self.conn.conexion.commit()
            return "Exito al modificar datos de la tabla trabajador proyecto"
        except Exception as e:
            print(f"Error al modificar BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()



# if __name__ =="__main__":
#     objTrabajadorProyecto = dTrabajadorProyecto()
#     print(objTrabajadorProyecto.eliminarTrabajadorProyecto(2))

"""     
    objTrabajadorProyecto.insertarTrabajadorProyecto(1,1,"Maestro de obra")
    objTrabajadorProyecto.insertarTrabajadorProyecto(2,1,"ayudante")
    objTrabajadorProyecto.insertarTrabajadorProyecto(3,1,"contramaestro")
    objTrabajadorProyecto.insertarTrabajadorProyecto(5,2,"Maestro de obra")
    objTrabajadorProyecto.insertarTrabajadorProyecto(2,1,"ayudante")
    objTrabajadorProyecto.insertarTrabajadorProyecto(6,2,"contramaestro")
    objTrabajadorProyecto.insertarTrabajadorProyecto(7,1,"contramaestro")
    objTrabajadorProyecto.insertarTrabajadorProyecto(2,2,"ayudante")

 """