from pydantic import BaseModel, Field, ValidationError
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Importamos la clase específica que necesitamos de la capa de datos
from datos.dProducto import dProducto

class nProducto():
    def __init__(self):
        # creamos obj de clase negosioCliente
        self.obj_producto = dProducto()

    def obtener_producto(self):
        # Llamamos al método de nuestro objeto de la capa de datos
        return self.obj_producto.obtenerProducto()
    
    def insertar_producto(self, id_producto, nombre, descripcion, ancho, alto, precio):
        
        # Pasamos los datos a la capa de datos para la inserción
        resultado = self.obj_producto.insertarProducto(id_producto, nombre, descripcion, ancho, alto, precio) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            return "Exito: Producto insertado correctamente."
        else:
            return "Error: No se pudo insertar el producto."



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
        
        # Pasamos los datos a la capa de datos para la modificar

        # Devolvemos un mensaje de éxito o error
        if not nombre or not descripcion or not ancho or not alto or not precio:
            return "Error: No se pudo modificar el cliente."
        else:
            resultado = self.obj_producto.modificarProducto(id_producto, nombre, descripcion, ancho, alto, precio) # La capa de datos aún usa camelCase
            return resultado
        

# if __name__ =="__main__":
#     objProducto = nProducto()
#     print(objProducto.modificar_producto(8))
#     print("Imprimir Aqui los datos")
