from pydantic import BaseModel, Field, ValidationError
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Importamos la clase específica que necesitamos de la capa de datos
from datos.dDetalle import dDetalle

class nDetalles():
    def __init__(self):
        # creamos obj de clase negosioCliente
        self.obj_detalle = dDetalle()

    def obtener_detalles(self):
        # Llamamos al método de nuestro objeto de la capa de datos
        return self.obj_detalle.obtenerDetalle()
    
    def insertar_detalles(self, id_detalle, cantidad, precio_unidad, sub_total, id_proveedor, id_producto):
        
        # Pasamos los datos a la capa de datos para la inserción
        resultado = self.obj_detalle.insertarDetalle(id_detalle, cantidad, precio_unidad, sub_total, id_proveedor, id_producto) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            return "Exito: Detalle insertado correctamente."
        else:
            return "Error: No se pudo insertar el detalle."


    def buscar_detalles(self, id_detalle):
        
        # Pasamos los datos a la capa de datos para la inserción
        resultado = self.obj_detalle.buscarDetalle(id_detalle) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            print("Exito: detalle encontrado correctamente.")
            return resultado
        else:
            return "Error: No se pudo encontrar el detalle."


    def eliminar_detalles(self, id_detalle):
        
        # Pasamos los datos a la capa de datos para la eliminacion
        resultado = self.obj_detalle.eliminarDetalle(id_detalle) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            return "Exito: Detalle eliminado correctamente."
        else:
            return "Error: No se pudo eliminar el detalle."


    def modificar_detalles(self, id_detalle, cantidad, precio_unidad, sub_total, id_proveedor, id_producto):
        
        # Pasamos los datos a la capa de datos para la modificar

        # Devolvemos un mensaje de éxito o error
        if not cantidad or not precio_unidad or not sub_total or not id_proveedor or not id_producto:
            return "Error: No se pudo modificar el cliente."
        else:
            resultado = self.obj_detalle.modificarDetalle(id_detalle, cantidad, precio_unidad, sub_total, id_proveedor, id_producto) # La capa de datos aún usa camelCase
            return resultado
        


""" 
if __name__ =="__main__":
    objDetalles = nDetalles()
    print(objDetalles.modificar_detalles(1,10,70,700,3, 1))
    print("Imprimir Aqui los datos")
"""