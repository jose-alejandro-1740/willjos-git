from pydantic import BaseModel, Field, ValidationError
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Importamos la clase específica que necesitamos de la capa de datos
from datos.dMaterial import dMaterial

class nMaterial():
    def __init__(self):
        # creamos obj de clase negosioCliente
        self.obj_material = dMaterial()

    def obtener_material(self):
        # Llamamos al método de nuestro objeto de la capa de datos
        return self.obj_material.obtenerMaterial()
    
    def insertar_material(self, id_material, nombre, descripcion, tipo, precio, stock, unidad, id_proveedor):
        
        # Pasamos los datos a la capa de datos para la inserción
        resultado = self.obj_material.insertarMaterial(id_material, nombre, descripcion, tipo, precio, stock, unidad, id_proveedor) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            return "Exito: Material insertado correctamente."
        else:
            return "Error: No se pudo insertar el material."


    def buscar_material(self, nombre_material):
        
        # Pasamos los datos a la capa de datos para la inserción
        resultado = self.obj_material.buscarMaterial(nombre_material) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            print("Exito: Material encontrado correctamente.")
            return resultado
        else:
            return "Error: No se pudo encontrar el material."


    def eliminar_material(self, id_material):
        
        # Pasamos los datos a la capa de datos para la eliminacion
        resultado = self.obj_material.eliminarMaterial(id_material) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            return "Exito: Material eliminado correctamente."
        else:
            return "Error: No se pudo eliminar el material."


    def modificar_material(self, id_material, nombre, descripcion, tipo, precio, stock, unidad, id_proveedor):
        
        # Pasamos los datos a la capa de datos para la modificar

        # Devolvemos un mensaje de éxito o error
        if not nombre or not descripcion or not tipo or not precio or not stock or not unidad or not id_proveedor:
            return "Error: No se pudo modificar el cliente."
        else:
            resultado = self.obj_material.modificarMaterial(id_material, nombre, descripcion, tipo, precio, stock, unidad, id_proveedor) # La capa de datos aún usa camelCase
            return resultado
        


""" 
if __name__ =="__main__":
    objMaterial = nMaterial()
    print(objMaterial.(""))
    print("Imprimir Aqui los datos")
 """