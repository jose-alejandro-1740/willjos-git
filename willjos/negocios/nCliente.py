from pydantic import BaseModel, Field, validator
from pydantic import  ValidationError
import sys
import os

# se crea un modelo pydantic 

class ClienteModel(BaseModel):
    id_cliente: int = Field(..., ge=1)
    nombre: str = Field(..., min_length=2)
    ap_paterno: str = Field(..., min_length=2)
    ap_materno: str = Field(..., min_length=2)
    direccion: str = Field(..., min_length=3)
    telefono: str = Field(..., min_length=6, max_length=15)

    @validator("nombre", "ap_paterno", "ap_materno")
    def solo_letras(cls, v):
        if not v.replace(" ", "").isalpha():
            raise ValueError("Debe contener solo letras")
        return v
    
    @validator("telefono")
    def solo_numeros(cls, v):
        if not v.isdigit():
            raise ValueError("El teléfono debe contener solo números")
        return v


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


        try:
            datos = ClienteModel(
                id_cliente=id_cliente,
                nombre=nombre,
                ap_paterno=ap_paterno,
                ap_materno=ap_materno,
                direccion=direccion,
                telefono=telefono
            )

            resultado = self.obj_cliente.insertarCliente(
                datos.id_cliente,
                datos.nombre,
                datos.ap_paterno,
                datos.ap_materno,
                datos.direccion,
                datos.telefono
            )

            return "Éxito: Cliente insertado correctamente." if resultado else "Error: No se pudo insertar el cliente."

        except ValidationError as e:
            return f"Error de validación: {e}"


    def buscar_cliente(self, nombre):

        if not nombre.strip():
            return "Error: Nombre vacío."

        # Pasamos los datos a la capa de datos para la inserción
        resultado = self.obj_cliente.buscarCliente(nombre) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        return resultado if resultado else "Error: No se pudo encontrar el cliente."


    def eliminar_cliente(self, id_cliente):

        if not isinstance(id_cliente, int):
            return "Error: El ID debe ser un número."

        # Pasamos los datos a la capa de datos para la eliminacion
        resultado = self.obj_cliente.eliminarCliente(id_cliente) # La capa de datos aún usa camelCase

        # Devolvemos un mensaje de éxito o error
        if resultado:
            return "Exito: Cliente eliminado correctamente."
        else:
            return "Error: No se pudo eliminar el cliente."


    def modificar_cliente(self, id_cliente, nombre, ap_paterno, ap_materno, direccion, telefono):

        try:
            datos = ClienteModel(
                id_cliente=id_cliente,
                nombre=nombre,
                ap_paterno=ap_paterno,
                ap_materno=ap_materno,
                direccion=direccion,
                telefono=telefono
            )

            resultado = self.obj_cliente.modificarCliente(
                datos.id_cliente,
                datos.nombre,
                datos.ap_paterno,
                datos.ap_materno,
                datos.direccion,
                datos.telefono
            )

            return "Éxito: Cliente modificado." if resultado else "Error: No se pudo modificar."

        except ValidationError as e:
            return f"Error de validación: {e}"


"""         
        # Pasamos los datos a la capa de datos para la modificar

        # Devolvemos un mensaje de éxito o error
        if not nombre or not ap_paterno or not ap_materno or not direccion or not telefono:
            return "Error: No se pudo modificar el cliente."
        else:
            resultado = self.obj_cliente.modificarCliente(id_cliente, nombre, ap_paterno, ap_materno, direccion, telefono) # La capa de datos aún usa camelCase
            return resultado
        
 """

""" 
if __name__ =="__main__":
    objCliente = nCliente()
    print(objCliente.modificar_cliente(114,"pepe","mariaca","quispe","Max Paredes # 1","87654321"))
    print("Imprimir Aqui los datos")
 """
