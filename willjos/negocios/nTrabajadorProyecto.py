from pydantic import BaseModel, Field, ValidationError
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Importamos la clase específica que necesitamos de la capa de datos
from datos.dTrabajadorProyecto import dTrabajadorProyecto

class TrabajadorProyectoModel(BaseModel):
    id_trabajador: int
    id_proyecto: int
    rol: str = Field(..., min_length=1, error_messages={"min_length": "El rol no puede estar vacío."})

class nTrabajadorProyecto():
    def __init__(self):
        # creamos obj de clase negosioCliente
        self.obj_trabajadorProyecto = dTrabajadorProyecto()

    def obtener_trabajadorProyecto(self):
        # Llamamos al método de nuestro objeto de la capa de datos
        return self.obj_trabajadorProyecto.obtenerTrabajadorProyecto()
    
    def insertar_trabajadorProyecto(self, id_trabajador, id_proyecto, rol):
        
        try:
            TrabajadorProyectoModel(id_trabajador=id_trabajador, id_proyecto=id_proyecto, rol=rol)
            # Pasamos los datos a la capa de datos para la inserción
            resultado = self.obj_trabajadorProyecto.insertarTrabajadorProyecto(id_trabajador, id_proyecto, rol)
            if resultado:
                return "Exito: Trabajador en el proyecto insertado correctamente."
            else:
                return "Error: No se pudo insertar el trabajador en el proyecto."
        except ValidationError as e:
            return f"Error de validación: {e}"

    def buscar_trabajadorProyecto(self, id_proyecto):
        
        # Pasamos los datos a la capa de datos para la inserción
        resultado = self.obj_trabajadorProyecto.buscarTrabajadorProyecto(id_proyecto) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            print("Exito: Trabajador del proyecto  encontrado correctamente.")
            return resultado
        else:
            return "Error: No se pudo encontrar el trabajador del proyecto ."


    def eliminar_trabajadorProyecto(self, id_trabajador):
        
        # Pasamos los datos a la capa de datos para la eliminacion
        resultado = self.obj_trabajadorProyecto.eliminarTrabajadorProyecto(id_trabajador) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            return "Exito: Trabajador del proyecto  eliminado correctamente."
        else:
            return "Error: No se pudo eliminar el trabajador del proyecto ."


    def modificar_trabajadorProyecto(self, id_trabajador, id_proyecto, rol):
        
        try:
            TrabajadorProyectoModel(id_trabajador=id_trabajador, id_proyecto=id_proyecto, rol=rol)
            # Pasamos los datos a la capa de datos para la modificación
            resultado = self.obj_trabajadorProyecto.modificarTrabajadorProyecto(id_trabajador, id_proyecto, rol)
            if resultado:
                return "Exito: Rol del trabajador en el proyecto modificado correctamente."
            return "Error: No se pudo modificar el rol del trabajador en el proyecto."
        except ValidationError as e:
            return f"Error de validación: {e}"
        

""" 
if __name__ =="__main__":
    objTrabajadorProyecto = nTrabajadorProyecto()
    print(objTrabajadorProyecto.modificar_trabajadorProyecto(1,1,"Maestro"))
    print("Imprimir Aqui los datos")
 """