from pydantic import BaseModel, Field, ValidationError
import sys
import os
from datetime import date
from typing import Optional

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Importamos la clase específica que necesitamos de la capa de datos
from datos.dTrabajador import dTrabajador

class TrabajadorModel(BaseModel):
    id_trabajador: int
    nombre: str = Field(..., min_length=1, error_messages={"min_length": "El nombre no puede estar vacío."})
    ap_paterno: str = Field(..., min_length=1, error_messages={"min_length": "El apellido paterno no puede estar vacío."})
    ap_materno: str = Field(..., min_length=1, error_messages={"min_length": "El apellido materno no puede estar vacío."})
    direccion: str = Field(..., min_length=1, error_messages={"min_length": "La dirección no puede estar vacía."})
    telefono: str = Field(..., min_length=1, error_messages={"min_length": "El teléfono no puede estar vacío."})
    cargo: str = Field(..., min_length=1, error_messages={"min_length": "El cargo no puede estar vacío."})
    sueldo: float = Field(..., gt=0, error_messages={"gt": "El sueldo debe ser un número positivo."})
    f_ingreso: date
    f_egreso: Optional[date] = None

class nTrabajador():
    def __init__(self):
        # creamos obj de clase negosioCliente
        self.obj_trabajador = dTrabajador()

    def obtener_trabajador(self):
        # Llamamos al método de nuestro objeto de la capa de datos
        return self.obj_trabajador.obtenerTrabajador()
    
    def insertar_trabajador(self, id_trabajador, nombre, ap_paterno, ap_materno, direccion, telefono, cargo, sueldo, f_ingreso, f_egreso):
        
        try:
            # Si f_egreso es "None" o está vacío, lo convertimos a None para la validación
            f_egreso_valid = f_egreso if f_egreso and f_egreso.strip().lower() != 'none' else None
            
            TrabajadorModel(
                id_trabajador=id_trabajador,
                nombre=nombre,
                ap_paterno=ap_paterno,
                ap_materno=ap_materno,
                direccion=direccion,
                telefono=telefono,
                cargo=cargo,
                sueldo=sueldo,
                f_ingreso=f_ingreso,
                f_egreso=f_egreso_valid
            )
            resultado = self.obj_trabajador.insertarTrabajador(id_trabajador, nombre, ap_paterno, ap_materno, direccion, telefono, cargo, sueldo, f_ingreso, f_egreso)
            if resultado:
                return "Exito: Trabajador insertado correctamente."
            else:
                return "Error: No se pudo insertar el trabajador."
        except ValidationError as e:
            return f"Error de validación: {e}"

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
        
        try:
            # Si f_egreso es "None" o está vacío, lo convertimos a None para la validación
            f_egreso_valid = f_egreso if f_egreso and f_egreso.strip().lower() != 'none' else None
            
            TrabajadorModel(
                id_trabajador=id_trabajador,
                nombre=nombre,
                ap_paterno=ap_paterno,
                ap_materno=ap_materno,
                direccion=direccion,
                telefono=telefono,
                cargo=cargo,
                sueldo=sueldo,
                f_ingreso=f_ingreso,
                f_egreso=f_egreso_valid
            )
            resultado = self.obj_trabajador.modificarTrabajador(id_trabajador, nombre, ap_paterno, ap_materno, direccion, telefono, cargo, sueldo, f_ingreso, f_egreso)
            if resultado:
                return "Exito: Trabajador modificado correctamente."
            return "Error: No se pudo modificar los datos del trabajador."
        except ValidationError as e:
            return f"Error de validación: {e}"
        
""" 
if __name__ =="__main__":
    objTrabajador = nTrabajador()
    print(objTrabajador.modificar_trabajador(5, "Jose ","quino","quino", "mirador", "22222222", "ayudante", "1800", "2025-1-5", "None"))
    print("Imprimir Aqui los datos") 
"""