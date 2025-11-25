from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import date
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Importamos la clase específica que necesitamos de la capa de datos
from datos.dVenta import dVenta

class VentaModel(BaseModel):
    id_venta: int
    fecha: date
    total: float
    forma_pago: str
    id_cliente: int


class nVenta():
    def __init__(self):
        # creamos obj de clase negosioCliente
        self.obj_venta = dVenta()

    def obtener_venta(self):
        # Llamamos al método de nuestro objeto de la capa de datos
        return self.obj_venta.obtenerVenta()
    
    def insertar_venta(self, id_venta, fecha, total, forma_pago, id_cliente):
        try:
            VentaModel(id_venta=id_venta, fecha=fecha, total=total, forma_pago=forma_pago, id_cliente=id_cliente)
            resultado = self.obj_venta.insertarVenta(id_venta, fecha, total, forma_pago, id_cliente)
            if resultado:
                return "Exito: Venta insertada correctamente."
            else:
                return "Error: No se pudo insertar la venta."
        except ValidationError as e:
            return f"Error de validación: {e}"


    def buscar_venta(self, id_venta):
        
        # Pasamos los datos a la capa de datos para la inserción
        resultado = self.obj_venta.buscarVenta(id_venta) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            print("Exito: Venta encontrada correctamente.")
            return resultado
        else:
            return "Error: No se pudo encontrar la venta."


    def eliminar_venta(self, id_venta):
        
        # Pasamos los datos a la capa de datos para la eliminacion
        resultado = self.obj_venta.eliminarVenta(id_venta) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            return "Exito: Venta eliminada correctamente."
        else:
            return "Error: No se pudo eliminar la venta."


    def modificar_venta(self, id_venta, fecha, total, forma_pago, id_cliente):
        try:
            VentaModel(id_venta=id_venta, fecha=fecha, total=total, forma_pago=forma_pago, id_cliente=id_cliente)
            resultado = self.obj_venta.modificarVenta(id_venta, fecha, total, forma_pago, id_cliente)
            if resultado:
                return "Exito: Venta modificada correctamente."
            else:
                return "Error: No se pudo modificar la venta."
        except ValidationError as e:
            return f"Error de validación: {e}"
        
""" 
if __name__ =="__main__":
    objVentan =nVenta()
    print(objVentan.modificar_venta(11, "2025-12-02", 7000, "efectivo", 121))
    print("Imprimir Aqui los datos")
"""