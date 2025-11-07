#from mysql.connector import MySQLConnection
import mysql.connector
from datos.conexionsql import conexion_BD

class dMaterial:
    def __init__(self):
        self.conn = conexion_BD()

    def obtenerMaterial(self):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("select * from material")
            filas = cursor.fetchall()
            return filas
        except Exception as e:
            print("Error al cargar BD WillJos",e)
            return[]
        finally:
            if cursor:
                cursor.close()
        
    def insertarMaterial(self, id_material, nombre, descripcion, tipo, precio, stock, unidad, id_proveedor):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("insert into material(id_material, nombre, descripcion, tipo, precio, stock, unidad, id_proveedor) values(%s,%s,%s,%s,%s,%s,%s,%s)",(id_material, nombre, descripcion, tipo, precio, stock, unidad, id_proveedor))            
            self.conn.conexion.commit()
            return True
        except Exception as e:
            print(f"Error al cargar BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()


    def buscarMaterial(self, nombre_material):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("select * from material where nombre like %s", (f'%{nombre_material}%',))
            encontrado = cursor.fetchall()
            return encontrado
        except Exception as e:
            print("Error al buscar BD WillJos",e)
            return[]
        finally:
            if cursor:
                cursor.close()


    def eliminarMaterial(self, id_material):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute('delete from material where id_material = %s', (id_material,))            
            self.conn.conexion.commit()
            return "Exito al eliminar el material"
        except Exception as e:
            print(f"Error al eliminar en BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()


    def modificarMaterial(self, id_material, nombre, descripcion, tipo, precio, stock, unidad, id_proveedor):
        cursor = None
        try: 
            cursor = self.conn.conexion.cursor() # crea el buscador Cursor
            cursor.execute("update material set nombre = %s, descripcion = %s, tipo = %s, precio = %s, stock = %s, unidad = %s, id_proveedor = %s where id_material = %s",(nombre, descripcion, tipo, precio, stock, unidad, id_proveedor,id_material))            
            self.conn.conexion.commit()
            return "Exito al modificar el material"
        except Exception as e:
            print(f"Error al modificar BD WillJos : {e}")
            return False
        finally:
            if cursor:
                cursor.close()


""" 
if __name__ =="__main__":
    objMaterial = dMaterial()
    print(objMaterial.eliminarMaterial(6))
"""
"""   
    objMaterial.insertarMaterial(9,"acrilico","interior de ventanas", "hojas  1.8x0.9 de 2mm", 30, "20u","paquetes de 12u", 3 )
    objMaterial.insertarMaterial(2,"cielo falso","para dentoro casa", "barras 6x0.30", 70, 10,"paquetes de 10u", 3 )
    objMaterial.insertarMaterial(3,"puertas mdf","solo interiores", "hojas de 1.8x0.9", 1000, "10u","unidad ", 3 )
    objMaterial.insertarMaterial(4,"cielo falso","para dentoro casa", "placas 60x60", 30, "20u","paquetes de 12u", 1 )
    objMaterial.insertarMaterial(5,"cielo falso","para dentoro casa", "placas 60x60", 30, "20u","paquetes de 12u", 2 )
    objMaterial.insertarMaterial(6,"cielo falso","para dentoro casa", "placas 60x60", 30, "20u","paquetes de 12u", 7 )
    objMaterial.insertarMaterial(7,"cielo falso","para dentoro casa", "placas 60x60", 30, "20u","paquetes de 12u", 5 )
    objMaterial.insertarMaterial(8,"cielo falso","para dentoro casa", "placas 60x60", 30, "20u","paquetes de 12u", 7 )
"""


