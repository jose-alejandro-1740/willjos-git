from pydantic import BaseModel, Field, ValidationError
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Importamos la clase específica que necesitamos de la capa de datos
from datos.dMedidor import dMedidor

class nMedidor():
    def __init__(self):
        # creamos obj de clase negosioCliente
        self.obj_medidor = dMedidor()

    def obtener_medidor(self):
        # Llamamos al método de nuestro objeto de la capa de datos
        return self.obj_medidor.obtenerMedidor()
    
    def insertar_medidor(self, codMedidor, direccion):
        
        # Pasamos los datos a la capa de datos para la inserción
        resultado = self.obj_medidor.insertarMedidor(codMedidor, direccion) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            return "Exito: Cliente insertado correctamente."
        else:
            return "Error: No se pudo insertar el cliente."


    def buscar_medidor(self, direccion):
        
        # Pasamos los datos a la capa de datos para la inserción
        resultado = self.obj_medidor.buscarMedidor(direccion) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            print("Exito: Cliente encontrado correctamente.")
            return resultado
        else:
            return "Error: No se pudo encontrar el cliente."


    def eliminar_medidor(self, codMedidor):
        
        # Pasamos los datos a la capa de datos para la eliminacion
        resultado = self.obj_medidor.eliminarMedidor(codMedidor) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            return "Exito: Cliente eliminado correctamente."
        else:
            return "Error: No se pudo eliminar el cliente."


    def modificar_medidor(self, codMedidor, direccion):
        
        # Pasamos los datos a la capa de datos para la modificar

        # Devolvemos un mensaje de éxito o error
        if not direccion :
            return "Error: No se pudo modificar el cliente."
        else:
            resultado = self.obj_medidor.modificarMedidor(codMedidor, direccion) # La capa de datos aún usa camelCase
            return resultado
        

if __name__ =="__main__":
    objMedidor = nMedidor()
    print(objMedidor.obtener_medidor())
    print("Imprimir Aqui los datos")
