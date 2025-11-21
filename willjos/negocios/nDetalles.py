from pydantic import BaseModel, Field, ValidationError, validator
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Importamos la clase específica que necesitamos de la capa de datos
from datos.dDetalle import dDetalle

# Modelo Pydantic para la validación de datos de Detalles
class DetalleModel(BaseModel):
    id_detalle: int = Field(..., ge=1)
    cantidad: int = Field(..., gt=0)
    precio_unidad: float = Field(..., gt=0)
    sub_total: float = Field(..., gt=0)
    id_proveedor: int = Field(..., ge=1)
    id_producto: int = Field(..., ge=1)



class nDetalles():
    def __init__(self):
        # creamos obj de clase negosioCliente
        self.obj_detalle = dDetalle()

    def obtener_detalles(self):
        # Llamamos al método de nuestro objeto de la capa de datos
        return self.obj_detalle.obtenerDetalle()
    
    def insertar_detalles(self, id_detalle, cantidad, precio_unidad, sub_total, id_proveedor, id_producto):
        try:
            # Validamos los datos con el modelo Pydantic
            datos = DetalleModel(
                id_detalle=id_detalle,
                cantidad=cantidad,
                precio_unidad=precio_unidad,
                sub_total=sub_total,
                id_proveedor=id_proveedor,
                id_producto=id_producto
            )
            # Pasamos los datos validados a la capa de datos
            resultado = self.obj_detalle.insertarDetalle(
                datos.id_detalle, datos.cantidad, datos.precio_unidad, 
                datos.sub_total, datos.id_proveedor, datos.id_producto
            )
            return "Exito: Detalle insertado correctamente." if resultado else "Error: No se pudo insertar el detalle."
        except ValidationError as e:
            return f"Error de validación: {e}"



    def buscar_detalles(self, id_detalle):
        if not str(id_detalle).strip().isdigit():
            return "Error: El ID del detalle debe ser un número."

        resultado = self.obj_detalle.buscarDetalle(int(id_detalle))

        # Devolvemos un mensaje de éxito o error
        return resultado if resultado else "Error: No se pudo encontrar el detalle."


    def eliminar_detalles(self, id_detalle):
        if not isinstance(id_detalle, int):
            return "Error: El ID debe ser un número."

        resultado = self.obj_detalle.eliminarDetalle(id_detalle)

        # Devolvemos un mensaje de éxito o error
        return "Exito: Detalle eliminado correctamente." if resultado else "Error: No se pudo eliminar el detalle."


    def modificar_detalles(self, id_detalle, cantidad, precio_unidad, sub_total, id_proveedor, id_producto):
        try:
            datos = DetalleModel(
                id_detalle=id_detalle,
                cantidad=cantidad,
                precio_unidad=precio_unidad,
                sub_total=sub_total,
                id_proveedor=id_proveedor,
                id_producto=id_producto
            )
            resultado = self.obj_detalle.modificarDetalle(
                datos.id_detalle, datos.cantidad, datos.precio_unidad, 
                datos.sub_total, datos.id_proveedor, datos.id_producto
            )
            return "Exito: Detalle modificado correctamente." if resultado else "Error: No se pudo modificar el detalle."
        except ValidationError as e:
            return f"Error de validación: {e}"



""" 
if __name__ =="__main__":
    objDetalles = nDetalles()
    print(objDetalles.modificar_detalles(1,10,70,700,3, 1))
    print("Imprimir Aqui los datos")
"""