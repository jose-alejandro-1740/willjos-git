from pydantic import BaseModel, Field, ValidationError
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Importamos la clase específica que necesitamos de la capa de datos
from datos.dProveedor import dProveedor

class nProveedor():
    def __init__(self):
        # creamos obj de clase negosioCliente
        self.obj_proveedor = dProveedor()

    def obtener_proveedor(self):
        # Llamamos al método de nuestro objeto de la capa de datos
        return self.obj_proveedor.obtenerProveedor()
    
    def insertar_proveedor(self, id_proveedor, nombre, ap_paterno, ap_materno, direccion, telefono, e_mail, contacto):
        
        # Pasamos los datos a la capa de datos para la inserción
        resultado = self.obj_proveedor.insertarProveedor(id_proveedor, nombre, ap_paterno, ap_materno, direccion, telefono, e_mail, contacto) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            return "Exito: Proveedor insertado correctamente."
        else:
            return "Error: No se pudo insertar el proveedor."

    def buscar_proveedor(self, nombre):
        
        # Pasamos los datos a la capa de datos para la inserción
        resultado = self.obj_proveedor.buscarProveedor(nombre) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            print("Exito: Cliente encontrado correctamente.")
            return resultado
        else:
            return "Error: No se pudo encontrar el cliente."


    def eliminar_proveedor(self, id_proveedor):
        
        # Pasamos los datos a la capa de datos para la eliminacion
        resultado = self.obj_proveedor.eliminarProveedor(id_proveedor) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            return "Exito: Proveedor eliminado correctamente."
        else:
            return "Error: No se pudo eliminar el proveedor."


    def modificar_proveedor(self, id_proveedor, nombre, ap_paterno, ap_materno, direccion, telefono, e_mail, contacto):
        
        # Pasamos los datos a la capa de datos para la modificar

        # Devolvemos un mensaje de éxito o error
        if not nombre or not ap_paterno or not ap_materno or not direccion or not telefono or not e_mail or not contacto:
            return "Error: No se pudo modificar el proveedpr."
        else:
            resultado = self.obj_proveedor.modificarProveedor(id_proveedor, nombre, ap_paterno, ap_materno, direccion, telefono, e_mail, contacto) # La capa de datos aún usa camelCase
            return resultado
        


""" 
if __name__ =="__main__":
    objProveedor = nProveedor()
    print(objProveedor.modificar_proveedor(5,"Juan Marcelo","Hilaquita",'Gutierrez', "Av.Mario Mercado ",22244477,"juan@gmail.com","None"))
    print("Imprimir Aqui los datos") 
"""