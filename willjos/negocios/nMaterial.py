from pydantic import BaseModel, Field, ValidationError
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Importamos la clase específica que necesitamos de la capa de datos
from datos.dMaterial import dMaterial

class MaterialModel(BaseModel):
    id_material: int
    nombre: str = Field(min_length=1)
    descripcion: str = Field(min_length=1)
    tipo: str = Field(min_length=1)
    precio: float
    stock: int
    unidad: str = Field(min_length=1)
    id_proveedor: int

class nMaterial():
    def __init__(self):
        # creamos obj de clase negosioCliente
        self.obj_material = dMaterial()

    def obtener_material(self):
        # Llamamos al método de nuestro objeto de la capa de datos
        return self.obj_material.obtenerMaterial()
    
    def insertar_material(self, id_material, nombre, descripcion, tipo, precio, stock, unidad, id_proveedor):
        try:
            MaterialModel(id_material=id_material, nombre=nombre, descripcion=descripcion, tipo=tipo, precio=precio, stock=stock, unidad=unidad, id_proveedor=id_proveedor)
            resultado = self.obj_material.insertarMaterial(id_material, nombre, descripcion, tipo, precio, stock, unidad, id_proveedor)
            if resultado:
                return "Exito: Material insertado correctamente."
            else:
                return "Error: No se pudo insertar el material."
        except ValidationError as e:
            return f"Error de validación: {e}"


    def buscar_material(self, nombre_material):
        
        # Pasamos los datos a la capa de datos para la inserción
        resultado = self.obj_material.buscarMaterial(nombre_material) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            print("Exito: Material encontrado correctamente.")
            return resultado
        else:
            return "Error: No se pudo encontrar el material."


    def eliminar_material(self, id_material):
        
        # Pasamos los datos a la capa de datos para la eliminacion
        resultado = self.obj_material.eliminarMaterial(id_material) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            return "Exito: Material eliminado correctamente."
        else:
            return "Error: No se pudo eliminar el material."


    def modificar_material(self, id_material, nombre, descripcion, tipo, precio, stock, unidad, id_proveedor):
        try:
            MaterialModel(id_material=id_material, nombre=nombre, descripcion=descripcion, tipo=tipo, precio=precio, stock=stock, unidad=unidad, id_proveedor=id_proveedor)
            resultado = self.obj_material.modificarMaterial(id_material, nombre, descripcion, tipo, precio, stock, unidad, id_proveedor)
            if resultado:
                return "Exito: Material modificado correctamente."
            else:
                return "Error: No se pudo modificar el material."
        except ValidationError as e:
            return f"Error de validación: {e}"
        


""" 
if __name__ =="__main__":
    objMaterial = nMaterial()
    # print(objMaterial.(""))
    print("Imprimir Aqui los datos")
 """