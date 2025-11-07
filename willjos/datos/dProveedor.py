import mysql.connector
from datos.conexionsql import conexion_BD

class dProveedor:
    def __init__(self):
        self.conn = conexion_BD()

    def obtenerProveedor(self):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("select * from proveedor")
            filas = cursor.fetchall()
            return filas
        except Exception as e:
            print("Error al cargar BD WillJos",e)
            return[]
        finally:
            if cursor:
                cursor.close()

    def insertarProveedor(self, id_proveedor, nombre, ap_paterno, ap_materno, direccion, telefono, e_mail, contacto):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("insert into proveedor(id_proveedor, nombre, ap_paterno, ap_materno, direccion, telefono, e_mail, contacto) values(%s,%s,%s,%s,%s,%s,%s,%s)",(id_proveedor, nombre, ap_paterno, ap_materno, direccion, telefono, e_mail, contacto))            
            self.conn.conexion.commit()
            return True
        except Exception as e:
            print(f"Error al cargar BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()        




    def buscarProveedor(self, nombre_proveedor):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("select * from proveedor where nombre like %s", (f'%{nombre_proveedor}%',))
            encontrado = cursor.fetchall()
            return encontrado
        except Exception as e:
            print("Error al buscar BD WillJos",e)
            return[]
        finally:
            if cursor:
                cursor.close()


    def eliminarProveedor(self, id_proveedor):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute('delete from proveedor where id_proveedor = %s', (id_proveedor,))            
            self.conn.conexion.commit()
            return "Exito al eliminar el proveedor"
        except Exception as e:
            print(f"Error al eliminar en BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()


    def modificarProveedor(self, id_proveedor, nombre, ap_paterno, ap_materno, direccion, telefono, e_mail, contacto):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("update proveedor set nombre = %s, ap_paterno = %s, ap_materno = %s, direccion = %s, telefono = %s, e_mail = %s, contacto = %s where id_proveedor = %s",(nombre, ap_paterno, ap_materno, direccion, telefono,e_mail, contacto, id_proveedor))            
            self.conn.conexion.commit()
            return "Exito al modificar el proveedor"
        except Exception as e:
            print(f"Error al modificar BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()




""" 
if __name__ =="__main__":
    objProveedor = dProveedor()

    #objProveedor.insertarProveedor(7,"Juan Marcelo","Hilaquita","Gutierrez","Av.Mario Mercado","22244477", "juan@gmail.com", "juan")
    print(objProveedor.eliminarProveedor(8))
"""