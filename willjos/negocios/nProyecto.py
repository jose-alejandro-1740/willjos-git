from pydantic import BaseModel, Field, ValidationError
import sys
import os
from datetime import date

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Importamos la clase específica que necesitamos de la capa de datos
from datos.dProyecto import dProyecto

class ProyectoModel(BaseModel):
    id_proyecto: int
    nombre: str = Field(..., min_length=1, error_messages={"min_length": "El nombre no puede estar vacío."})
    direccion: str = Field(..., min_length=1, error_messages={"min_length": "La dirección no puede estar vacía."})
    f_proyecto: date
    descuento: float = Field(..., ge=0, error_messages={"greater_than_equal": "El descuento no puede ser negativo."})
    total: float = Field(..., gt=0, error_messages={"greater_than": "El total debe ser un número positivo."})
    id_cliente: int

class nProyecto():
    def __init__(self):
        # creamos obj de clase negosioCliente
        self.obj_proyecto = dProyecto()

    def obtener_proyecto(self):
        # Llamamos al método de nuestro objeto de la capa de datos
        return self.obj_proyecto.obtenerProyecto()
    
    def insertar_proyecto(self, id_proyecto, nombre, direccion, f_proyecto, descuento, total, id_cliente):
        
        try:
            ProyectoModel(
                id_proyecto=id_proyecto,
                nombre=nombre,
                direccion=direccion,
                f_proyecto=f_proyecto,
                descuento=descuento,
                total=total,
                id_cliente=id_cliente
            )
            # Pasamos los datos a la capa de datos para la inserción
            resultado = self.obj_proyecto.insertarProyecto(id_proyecto, nombre, direccion, f_proyecto, descuento, total, id_cliente)
    
            # Devolvemos un mensaje de éxito o error
            if resultado:
                return "Exito: Proyecto insertado correctamente."
            else:
                return "Error: No se pudo insertar el proyecto."
        except ValidationError as e:
            return f"Error de validación: {e}"

    def buscar_proyecto(self, nombre_proyecto):
        
        # Pasamos los datos a la capa de datos para la inserción
        resultado = self.obj_proyecto.buscarProyecto(nombre_proyecto) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            print("Exito: Proyecto encontrado correctamente.")
            return resultado
        else:
            return "Error: No se pudo encontrar el proyecto."


    def eliminar_proyecto(self, id_proyecto):
        
        # Pasamos los datos a la capa de datos para la eliminacion
        resultado = self.obj_proyecto.eliminarProyecto(id_proyecto) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            return "Exito: Proyecto eliminado correctamente."
        else:
            return "Error: No se pudo eliminar el proyecto."


    def modificar_proyecto(self, id_proyecto, nombre, direccion, f_proyecto, descuento, total, id_cliente):
        
        try:
            ProyectoModel(
                id_proyecto=id_proyecto,
                nombre=nombre,
                direccion=direccion,
                f_proyecto=f_proyecto,
                descuento=descuento,
                total=total,
                id_cliente=id_cliente
            )
            # Pasamos los datos a la capa de datos para la modificación
            resultado = self.obj_proyecto.modificarProyecto(id_proyecto, nombre, direccion, f_proyecto, descuento, total, id_cliente)
            if resultado:
                return "Exito: Proyecto modificado correctamente."
            return "Error: No se pudo modificar el proyecto."
        except ValidationError as e:
            return f"Error de validación: {e}"
        

""" 
if __name__ =="__main__":
    objProyecto = nProyecto()
    print(objProyecto.insertar_proyecto(9,"senkata 7", "llojeta las bajo", "2024-07-01", 1000, 11000, 107))
    print("Imprimir Aqui los datos")
"""