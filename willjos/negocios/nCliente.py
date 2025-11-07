from pydantic import BaseModel, Field, ValidationError
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Importamos la clase específica que necesitamos de la capa de datos
from datos.dCliente import dCliente

class nCliente():
    def __init__(self):
        # creamos obj de clase negosioCliente
        self.obj_cliente = dCliente()

    def obtener_cliente(self):
        # Llamamos al método de nuestro objeto de la capa de datos
        return self.obj_cliente.obtenerCliente()
    
    def insertar_cliente(self, id_cliente, nombre, ap_paterno, ap_materno, direccion, telefono):
        
        # Pasamos los datos a la capa de datos para la inserción
        resultado = self.obj_cliente.insertarCliente(id_cliente, nombre, ap_paterno, ap_materno, direccion, telefono) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            return "Exito: Cliente insertado correctamente."
        else:
            return "Error: No se pudo insertar el cliente."


    def buscar_cliente(self, nombre):
        
        # Pasamos los datos a la capa de datos para la inserción
        resultado = self.obj_cliente.buscarCliente(nombre) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            print("Exito: Cliente encontrado correctamente.")
            return resultado
        else:
            return "Error: No se pudo encontrar el cliente."


    def eliminar_cliente(self, id_cliente):
        
        # Pasamos los datos a la capa de datos para la eliminacion
        resultado = self.obj_cliente.eliminarCliente(id_cliente) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            return "Exito: Cliente eliminado correctamente."
        else:
            return "Error: No se pudo eliminar el cliente."


    def modificar_cliente(self, id_cliente, nombre, ap_paterno, ap_materno, direccion, telefono):
        
        # Pasamos los datos a la capa de datos para la modificar

        # Devolvemos un mensaje de éxito o error
        if not nombre or not ap_paterno or not ap_materno or not direccion or not telefono:
            return "Error: No se pudo modificar el cliente."
        else:
            resultado = self.obj_cliente.modificarCliente(id_cliente, nombre, ap_paterno, ap_materno, direccion, telefono) # La capa de datos aún usa camelCase
            return resultado
        


""" 
if __name__ =="__main__":
    objCliente = nCliente()
    print(objCliente.modificar_cliente(114,"pepe","mariaca","quispe","Max Paredes # 1","87654321"))
    print("Imprimir Aqui los datos")
 """