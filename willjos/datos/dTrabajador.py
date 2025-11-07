import mysql.connector
from datos.conexionsql import conexion_BD

class dTrabajador:
    def __init__(self):
        self.conn = conexion_BD()

    def obtenerTrabajador(self):
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("select * from trabajador")
            filas = cursor.fetchall()
            cursor.close()
            return filas
        except Exception as e:
            print("Error al cargar BD WillJos",e)
            return[]
        finally:
            if cursor:
                cursor.close()

    def insertarTrabajador(self, id_trabajador, nombre, ap_paterno, ap_materno, direccion, telefono, cargo, sueldo, f_ingreso, f_egreso):
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("insert into trabajador(id_trabajador, nombre, ap_paterno, ap_materno, direccion, telefono, cargo, sueldo, f_ingreso, f_egreso) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(id_trabajador, nombre, ap_paterno, ap_materno, direccion, telefono, cargo, sueldo, f_ingreso, f_egreso))            
            self.conn.conexion.commit()
            cursor.close()
            return True
        except mysql.connector.Error as e:
            print(f"Error al cargar BD WillJos : {e}")
            return False
        

    def buscarTrabajador(self, nombre_trabajador):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("select * from trabajador where nombre like %s", (f'%{nombre_trabajador}%',))
            encontrado = cursor.fetchall()
            return encontrado
        except Exception as e:
            print("Error al buscar BD WillJos",e)
            return[]
        finally:
            if cursor:
                cursor.close()


    def eliminarTrabajador(self, id_trabajador):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute('delete from trabajador where id_trabajador = %s', (id_trabajador,))            
            self.conn.conexion.commit()
            return "Exito al eliminar el trabajador"
        except Exception as e:
            print(f"Error al eliminar en BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()


    def modificarTrabajador(self, id_trabajador, nombre, ap_paterno, ap_materno, direccion, telefono, cargo, sueldo, f_ingreso, f_egreso):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("update trabajador set nombre = %s, ap_paterno = %s, ap_materno = %s, direccion = %s, telefono = %s, cargo = %s, sueldo = %s, f_ingreso = %s, f_egreso = %s where id_trabajador = %s",(nombre, ap_paterno, ap_materno, direccion, telefono, cargo, sueldo, f_ingreso, f_egreso, id_trabajador))            
            self.conn.conexion.commit()
            return "Exito al modificar el trabajador"
        except Exception as e:
            print(f"Error al modificar BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()



""" 
if __name__ =="__main__":
    objTrabajador = dTrabajador()

    #objTrabajador.insertarTrabajador(7,"Alejandro","quiriarte","quiroga","miraflores","22233344", "contramaestro", 3000.00, "2025-01-01","Null")
    print(objTrabajador.eliminarTrabajador(9))

"""