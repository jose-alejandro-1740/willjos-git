from pydantic import BaseModel, Field, ValidationError, validator
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Importamos la clase específica que necesitamos de la capa de datos
from datos.dDetalleVenta import dDetalleVenta

# Modelo Pydantic para la validación de datos de DetalleVenta
class DetalleVentaModel(BaseModel):
    id_detventa: int = Field(..., ge=1)
    cantidad: int = Field(..., gt=0)
    precio_unidad: float = Field(..., gt=0)
    sub_total: float = Field(..., gt=0)
    id_venta: int = Field(..., ge=1)
    id_producto: int = Field(..., ge=1)


class nDetalleVenta():
    def __init__(self):
        # creamos obj de clase negosioCliente
        self.obj_detalleVentanta = dDetalleVenta()

    def obtener_detalleVenta(self):
        # Llamamos al método de nuestro objeto de la capa de datos
        return self.obj_detalleVentanta.obtenerDetalleVenta()
    
    def insertar_detalleVenta(self, id_detventa, cantidad, precio_unidad, sub_total, id_venta, id_producto):
        try:
            datos = DetalleVentaModel(
                id_detventa=id_detventa,
                cantidad=cantidad,
                precio_unidad=precio_unidad,
                sub_total=sub_total,
                id_venta=id_venta,
                id_producto=id_producto
            )
            resultado = self.obj_detalleVentanta.insertarDetalleVenta(
                datos.id_detventa, datos.cantidad, datos.precio_unidad, 
                datos.sub_total, datos.id_venta, datos.id_producto
            )
            return "Exito: Detalle de venta insertado correctamente." if resultado else "Error: No se pudo insertar el detalle de venta."
        except ValidationError as e:
            return f"Error de validación: {e}"


    def buscar_detalleVenta(self, id_detventa):
        if not str(id_detventa).strip().isdigit():
            return "Error: El ID del detalle de venta debe ser un número."

        resultado = self.obj_detalleVentanta.buscarDetalleVenta(int(id_detventa))

        # Devolvemos un mensaje de éxito o error
        return resultado if resultado else "Error: No se pudo encontrar el detalle de venta."


    def eliminar_detalleVenta(self, id_detventa):
        if not isinstance(id_detventa, int):
            return "Error: El ID debe ser un número."

        resultado = self.obj_detalleVentanta.eliminarDetalleVenta(id_detventa)

        # Devolvemos un mensaje de éxito o error
        return "Exito: Detalle de la venta eliminado correctamente." if resultado else "Error: No se pudo eliminar el detalle de la venta."


    def modificar_detalleVenta(self, id_detventa, cantidad, precio_unidad, sub_total, id_venta, id_producto):
        try:
            datos = DetalleVentaModel(
                id_detventa=id_detventa,
                cantidad=cantidad,
                precio_unidad=precio_unidad,
                sub_total=sub_total,
                id_venta=id_venta,
                id_producto=id_producto
            )
            resultado = self.obj_detalleVentanta.modificarDetalleVenta(
                datos.id_detventa, datos.cantidad, datos.precio_unidad, 
                datos.sub_total, datos.id_venta, datos.id_producto
            )
            return "Exito: Detalle de venta modificado correctamente." if resultado else "Error: No se pudo modificar el detalle de venta."
        except ValidationError as e:
            return f"Error de validación: {e}"

""" 
if __name__ =="__main__":
    objDetalleVenta = nDetalleVenta()
    print(objDetalleVenta.eliminar_detalleVenta(1))
    print("Imprimir Aqui los datos")
"""