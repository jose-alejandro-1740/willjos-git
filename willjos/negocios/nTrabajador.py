from pydantic import BaseModel, Field, ValidationError
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Importamos la clase específica que necesitamos de la capa de datos
from datos.dTrabajador import dTrabajador

class nTrabajador():
    def __init__(self):
        # creamos obj de clase negosioCliente
        self.obj_trabajador = dTrabajador()

    def obtener_trabajador(self):
        # Llamamos al método de nuestro objeto de la capa de datos
        return self.obj_trabajador.obtenerTrabajador()
    
    def insertar_trabajador(self, id_trabajador, nombre, ap_paterno, ap_materno, direccion, telefono, cargo, sueldo, f_ingreso, f_egreso):
        
        # Pasamos los datos a la capa de datos para la inserción
        resultado = self.objtrabajador.insertarTrabajador(id_trabajador, nombre, ap_paterno, ap_materno, direccion, telefono, cargo, sueldo, f_ingreso, f_egreso) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            return "Exito: Trabajador insertado correctamente."
        else:
            return "Error: No se pudo insertar el trabajador."


    def buscar_trabajador(self, nombre):
        
        # Pasamos los datos a la capa de datos para la inserción
        resultado = self.obj_trabajador.buscarTrabajador(nombre) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            print("Exito: Trabajador encontrado correctamente.")
            return resultado
        else:
            return "Error: No se pudo encontrar el trabajador."


    def eliminar_trabajador(self, id_trabajador):
        
        # Pasamos los datos a la capa de datos para la eliminacion
        resultado = self.obj_trabajador.eliminarTrabajador(id_trabajador) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            return "Exito: Trabajador eliminado correctamente."
        else:
            return "Error: No se pudo eliminar el trabajador."


    def modificar_trabajador(self,  id_trabajador, nombre, ap_paterno, ap_materno, direccion, telefono, cargo, sueldo, f_ingreso, f_egreso):
        
        # Pasamos los datos a la capa de datos para la modificar

        # Devolvemos un mensaje de éxito o error
        if not nombre or not ap_paterno or not ap_materno or not direccion or not telefono or not cargo or not sueldo or not f_ingreso or not f_egreso:
            return "Error: No se pudo modificar datos del trabajador."
        else:
            resultado = self.obj_trabajador.modificarTrabajador( id_trabajador, nombre, ap_paterno, ap_materno, direccion, telefono, cargo, sueldo, f_ingreso, f_egreso) # La capa de datos aún usa camelCase
            return resultado
        
""" 
if __name__ =="__main__":
    objTrabajador = nTrabajador()
    print(objTrabajador.modificar_trabajador(5, "Jose ","quino","quino", "mirador", "22222222", "ayudante", "1800", "2025-1-5", "None"))
    print("Imprimir Aqui los datos") 
"""