from pydantic import BaseModel, Field, ValidationError, EmailStr
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Importamos la clase específica que necesitamos de la capa de datos
from datos.dProveedor import dProveedor

class ProveedorModel(BaseModel):
    id_proveedor: int
    nombre: str = Field(..., min_length=1, error_messages={"min_length": "El nombre no puede estar vacío."})
    ap_paterno: str = Field(..., min_length=1, error_messages={"min_length": "El apellido paterno no puede estar vacío."})
    ap_materno: str = Field(..., min_length=1, error_messages={"min_length": "El apellido materno no puede estar vacío."})
    direccion: str = Field(..., min_length=1, error_messages={"min_length": "La dirección no puede estar vacía."})
    telefono: str = Field(..., min_length=1, error_messages={"min_length": "El teléfono no puede estar vacío."})
    e_mail: EmailStr
    contacto: str = Field(..., min_length=1, error_messages={"min_length": "El contacto no puede estar vacío."})

class nProveedor():
    def __init__(self):
        # creamos obj de clase negosioCliente
        self.obj_proveedor = dProveedor()

    def obtener_proveedor(self):
        # Llamamos al método de nuestro objeto de la capa de datos
        return self.obj_proveedor.obtenerProveedor()
    
    def insertar_proveedor(self, id_proveedor, nombre, ap_paterno, ap_materno, direccion, telefono, e_mail, contacto):
        
        try:
            ProveedorModel(
                id_proveedor=id_proveedor,
                nombre=nombre,
                ap_paterno=ap_paterno,
                ap_materno=ap_materno,
                direccion=direccion,
                telefono=telefono,
                e_mail=e_mail,
                contacto=contacto
            )
            resultado = self.obj_proveedor.insertarProveedor(id_proveedor, nombre, ap_paterno, ap_materno, direccion, telefono, e_mail, contacto)
            if resultado:
                return "Exito: Proveedor insertado correctamente."
            else:
                return "Error: No se pudo insertar el proveedor."
        except ValidationError as e:
            return f"Error de validación: {e}"

    def buscar_proveedor(self, nombre):
        
        # Pasamos los datos a la capa de datos para la inserción
        resultado = self.obj_proveedor.buscarProveedor(nombre) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            print("Exito: Proveedor encontrado correctamente.")
            return resultado
        else:
            return "Error: No se pudo encontrar el proveedor."


    def eliminar_proveedor(self, id_proveedor):
        
        # Pasamos los datos a la capa de datos para la eliminacion
        resultado = self.obj_proveedor.eliminarProveedor(id_proveedor) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            return "Exito: Proveedor eliminado correctamente."
        else:
            return "Error: No se pudo eliminar el proveedor."


    def modificar_proveedor(self, id_proveedor, nombre, ap_paterno, ap_materno, direccion, telefono, e_mail, contacto):
        
        try:
            ProveedorModel(
                id_proveedor=id_proveedor,
                nombre=nombre,
                ap_paterno=ap_paterno,
                ap_materno=ap_materno,
                direccion=direccion,
                telefono=telefono,
                e_mail=e_mail,
                contacto=contacto
            )
            resultado = self.obj_proveedor.modificarProveedor(id_proveedor, nombre, ap_paterno, ap_materno, direccion, telefono, e_mail, contacto)
            if resultado:
                return "Exito: Proveedor modificado correctamente."
            else:
                return "Error: No se pudo modificar el proveedor."
        except ValidationError as e:
            return f"Error de validación: {e}"
        


""" 
if __name__ =="__main__":
    objProveedor = nProveedor()
    print(objProveedor.modificar_proveedor(5,"Juan Marcelo","Hilaquita",'Gutierrez', "Av.Mario Mercado ",22244477,"juan@gmail.com","None"))
    print("Imprimir Aqui los datos") 
"""