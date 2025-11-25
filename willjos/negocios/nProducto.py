from pydantic import BaseModel, Field, ValidationError
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Importamos la clase específica que necesitamos de la capa de datos
from datos.dProducto import dProducto

class ProductoModel(BaseModel):
    id_producto: int
    nombre: str = Field(..., min_length=1, error_messages={"min_length": "El nombre no puede estar vacío."})
    descripcion: str = Field(..., min_length=1, error_messages={"min_length": "La descripción no puede estar vacía."})
    ancho: float = Field(..., gt=0, error_messages={"greater_than": "El ancho debe ser un número positivo."})
    alto: float = Field(..., gt=0, error_messages={"greater_than": "El alto debe ser un número positivo."})
    precio: float = Field(..., gt=0, error_messages={"greater_than": "El precio debe ser un número positivo."})


class nProducto():
    def __init__(self):
        # creamos obj de clase negosioCliente
        self.obj_producto = dProducto()

    def obtener_producto(self):
        # Llamamos al método de nuestro objeto de la capa de datos
        return self.obj_producto.obtenerProducto()
    
    def insertar_producto(self, id_producto, nombre, descripcion, ancho, alto, precio):
        
        try:
            # Validamos los datos con Pydantic
            ProductoModel(id_producto=id_producto, nombre=nombre, descripcion=descripcion, ancho=ancho, alto=alto, precio=precio)
            
            # Pasamos los datos a la capa de datos para la inserción
            resultado = self.obj_producto.insertarProducto(id_producto, nombre, descripcion, ancho, alto, precio)
            if resultado:
                return "Exito: Producto insertado correctamente."
            return "Error: No se pudo insertar el producto."
        except ValidationError as e:
            return f"Error de validación: {e}"


    def buscar_producto(self, nombre):
        
        # Pasamos los datos a la capa de datos para la inserción
        resultado = self.obj_producto.buscarProducto(nombre) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            print("Exito: Producto encontrado correctamente.")
            return resultado
        else:
            return "Error: No se pudo encontrar el producto."


    def eliminar_producto(self, id_producto):
        
        # Pasamos los datos a la capa de datos para la eliminacion
        resultado = self.obj_producto.eliminarProducto(id_producto) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            return "Exito: producto eliminado correctamente."
        else:
            return "Error: No se pudo eliminar el producto."


    def modificar_producto(self, id_producto, nombre, descripcion, ancho, alto, precio):
        
        try:
            # Validamos los datos con Pydantic
            ProductoModel(id_producto=id_producto, nombre=nombre, descripcion=descripcion, ancho=ancho, alto=alto, precio=precio)
            
            # Pasamos los datos a la capa de datos para la modificación
            resultado = self.obj_producto.modificarProducto(id_producto, nombre, descripcion, ancho, alto, precio)
            if resultado:
                return "Exito: Producto modificado correctamente."
            return "Error: No se pudo modificar el producto."
        except ValidationError as e:
            return f"Error de validación: {e}"
        

# if __name__ =="__main__":
#     objProducto = nProducto()
#     print(objProducto.modificar_producto(8))
#     print("Imprimir Aqui los datos")
