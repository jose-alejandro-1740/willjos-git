from pydantic import BaseModel, Field, ValidationError
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Importamos la clase específica que necesitamos de la capa de datos
from datos.dDetalleVenta import dDetalleVenta

class nDetalleVenta():
    def __init__(self):
        # creamos obj de clase negosioCliente
        self.obj_detalleVentanta = dDetalleVenta()

    def obtener_detalleVenta(self):
        # Llamamos al método de nuestro objeto de la capa de datos
        return self.obj_detalleVentanta.obtenerDetalleVenta()
    
    def insertar_detalleVenta(self, id_detventa, cantidad, precio_unidad, sub_total, id_venta, id_producto):
        
        # Pasamos los datos a la capa de datos para la inserción
        resultado = self.obj_detalleVentanta.insertarDetalleVenta(id_detventa, cantidad, precio_unidad, sub_total, id_venta, id_producto) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            return "Exito: Detalle de venta insertado correctamente."
        else:
            return "Error: No se pudo insertar el detalle de venta."


    def buscar_detalleVenta(self, id_detventa):
        
        # Pasamos los datos a la capa de datos para la inserción
        resultado = self.obj_detalleVentanta.buscarDetalleVenta(id_detventa) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            print("Exito: Detalle de venta encontrado correctamente.")
            return resultado
        else:
            return "Error: No se pudo encontrar el detalle de venta."


    def eliminar_detalleVenta(self, id_detventa):
        
        # Pasamos los datos a la capa de datos para la eliminacion
        resultado = self.obj_detalleVentanta.eliminarDetalleVenta(id_detventa) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            return "Exito: Detalle de la venta eliminado correctamente."
        else:
            return "Error: No se pudo eliminar el detalle de la venta."


    def modificar_detalleVenta(self, id_detventa, cantidad, precio_unidad, sub_total, id_venta, id_producto):
        
        # Pasamos los datos a la capa de datos para la modificar

        # Devolvemos un mensaje de éxito o error
        if not cantidad or not precio_unidad or not sub_total or not id_venta or not id_producto:
            return "Error: No se pudo modificar el cliente."
        else:
            resultado = self.obj_detalleVentanta.modificarDetalleVenta(id_detventa, cantidad, precio_unidad, sub_total, id_venta, id_producto) # La capa de datos aún usa camelCase
            return resultado
        


if __name__ =="__main__":
    objDetalleVenta = nDetalleVenta()
    print(objDetalleVenta.eliminar_detalleVenta(1))
    print("Imprimir Aqui los datos")
