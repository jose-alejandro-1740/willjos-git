import sys
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from negocios.nTrabajador import nTrabajador

class Trabajador:
    def __init__(self, frm1, frm3):

        # Instancia de la capa de negocios para poder usar sus métodos
        self.capaNegocios =nTrabajador()

        #Limpiamos el frm1 antes de mostrar los elem de Trabajador
        for widget in frm1.winfo_children():
            widget.destroy()
        frm1.pack_propagate(False)

        # Ahora creamos los frm title, entrys y crud   
        self.frmTitle = ctk.CTkFrame(frm1, fg_color="transparent")
        self.frmTitle.pack(pady=10, padx=15, fill="x")

        self.frmEntrys = ctk.CTkFrame(frm1, fg_color="transparent")
        self.frmEntrys.pack(pady=10, padx=15, fill="x", expand=True)
        self.frmEntrys.grid_columnconfigure(1, weight=1)

        self.frmCrud = ctk.CTkFrame(frm1, fg_color="transparent")
        self.frmCrud.pack(pady=20, padx=15, fill="x", side="bottom")


    # Creamos los contenidos de los frm title, entrys y crud
        self.lblTitle = ctk.CTkLabel(self.frmTitle, text="Gestion Trabajadores", font=ctk.CTkFont(size=22, weight="bold"))
        self.lblTitle.pack(pady=10)

    # Colocamos los Entrys 
       
        self.lblIdTrabajador= ctk.CTkLabel(self.frmEntrys, text="ID Trabajador")
        self.lblIdTrabajador.grid(row=0, column=0, padx=5, pady=5)
        self.entIdTrabajador = ctk.CTkEntry(self.frmEntrys)
        self.entIdTrabajador.grid(row=0, column=1, padx=10, pady=10)

        self.lblnombre = ctk.CTkLabel(self.frmEntrys, text="Nombre")
        self.lblnombre.grid(row=1, column=0, padx=10, pady=10)
        self.entNombre = ctk.CTkEntry(self.frmEntrys)
        self.entNombre.grid(row=1, column=1, padx=10, pady=10)


        self.lblApPaterno = ctk.CTkLabel(self.frmEntrys, text="Apellido Paterno")
        self.lblApPaterno.grid(row=2, column=0, padx=10, pady=10)
        self.entApPaterno = ctk.CTkEntry(self.frmEntrys)
        self.entApPaterno.grid(row=2, column=1, padx=10, pady=10)


        self.lblApMaterno = ctk.CTkLabel(self.frmEntrys, text="Apellido Materno")
        self.lblApMaterno.grid(row=3, column=0, padx=10, pady=10)
        self.entApMaterno = ctk.CTkEntry(self.frmEntrys)
        self.entApMaterno.grid(row=3, column=1, padx=10, pady=10)


        self.lblDireccion = ctk.CTkLabel(self.frmEntrys, text="Direccion")
        self.lblDireccion.grid(row=4, column=0, padx=10, pady=10)
        self.entDireccion = ctk.CTkEntry(self.frmEntrys)
        self.entDireccion.grid(row=4, column=1, padx=10, pady=10)


        self.lblTelefono = ctk.CTkLabel(self.frmEntrys, text="telefono")
        self.lblTelefono.grid(row=5, column=0, padx=10, pady=10)
        self.entTelefono = ctk.CTkEntry(self.frmEntrys)
        self.entTelefono.grid(row=5, column=1, padx=10, pady=10)


        self.lblCargo = ctk.CTkLabel(self.frmEntrys, text="Cargo")
        self.lblCargo.grid(row=6, column=0, padx=10, pady=10)
        self.entCargo = ctk.CTkEntry(self.frmEntrys)
        self.entCargo.grid(row=6, column=1, padx=10, pady=10)


        self.lblSueldo = ctk.CTkLabel(self.frmEntrys, text="Sueldo")
        self.lblSueldo.grid(row=7, column=0, padx=10, pady=10)
        self.entSueldo = ctk.CTkEntry(self.frmEntrys)
        self.entSueldo.grid(row=7, column=1, padx=10, pady=10)


        self.lblFechaIngreso = ctk.CTkLabel(self.frmEntrys, text="Fecha Ingreso")
        self.lblFechaIngreso.grid(row=8, column=0, padx=10, pady=10)
        self.entFechaIngreso = ctk.CTkEntry(self.frmEntrys)
        self.entFechaIngreso.grid(row=8, column=1, padx=10, pady=10)


        self.lblFechaSalida = ctk.CTkLabel(self.frmEntrys, text="Fecha Salida")
        self.lblFechaSalida.grid(row=9, column=0, padx=10, pady=10)
        self.entFechaSalida = ctk.CTkEntry(self.frmEntrys)
        self.entFechaSalida.grid(row=9, column=1, padx=10, pady=10)

    # Colocamos los Botones crud en frm Crud

        self.btnInsertar = ctk.CTkButton(self.frmCrud, text="Insertar")
        self.btnInsertar.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(0, weight=1)

        self.btnModificar = ctk.CTkButton(self.frmCrud, text="Modificar")
        self.btnModificar.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(1, weight=1)

        self.btnEliminar = ctk.CTkButton(self.frmCrud, text="Eliminar")
        self.btnEliminar.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(2, weight=1)

        self.btnReporte = ctk.CTkButton(self.frmCrud, text="Reporte")
        self.btnReporte.grid(row=0, column=3, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(3, weight=1)


        self.lblBuscarNombreCliente = ctk.CTkLabel(self.frmCrud, text="Buscar Nombre")
        self.lblBuscarNombreCliente.grid(row=1, column=0, padx=10, pady=10)
        self.frmCrud.grid_columnconfigure(0, weight=1)

        self.entBuscar = ctk.CTkEntry(self.frmCrud)
        self.entBuscar.grid(row=1, column=1, padx=10, pady=10)
        self.frmCrud.grid_columnconfigure(1, weight=1)

        self.btnBuscar = ctk.CTkButton(self.frmCrud, text="Buscar")
        self.btnBuscar.grid(row=1, column=2, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(2, weight=1)

# Tranbajamos en el Treeview en frm3
    #Limpiamos el frm3 antes de mostrar los elem de Trabajador
        for widget in frm3.winfo_children():
            widget.destroy()
       
        self.lblArbolTrabajador = ctk.CTkLabel(frm3, text="Registros de Trabajadores", font=ctk.CTkFont(size=18, weight="bold"))
        self.lblArbolTrabajador.pack(pady=(15, 10))

        # setup_treeview_style()
    # Arbol Trabajador
        self.arbolTrabajador = ttk.Treeview(frm3, columns=('Id Trabajador', 'Nombre', 'Ap Paterno', 'Ap Materno', 'Direccion', 'Telefono','Cargo', 'Sueldo', 'Fecha Ingreso', 'Fecha Salida'), show='headings', height=5)
        self.arbolTrabajador.heading('#1', text='Id Trabajador')
        self.arbolTrabajador.column('#1', anchor=CENTER, width=50)
        self.arbolTrabajador.heading('#2', text='Nombre')
        self.arbolTrabajador.column('#2', anchor=CENTER, width=150)
        self.arbolTrabajador.heading('#3', text='Ap Paterno')
        self.arbolTrabajador.column('#3', anchor=CENTER, width=150)
        self.arbolTrabajador.heading('#4', text='Ap Materno')
        self.arbolTrabajador.column('#4', anchor=CENTER, width=150)
        self.arbolTrabajador.heading('#5', text='Direccion')
        self.arbolTrabajador.column('#5', anchor=CENTER, width=150)
        self.arbolTrabajador.heading('#6', text='Telefono')
        self.arbolTrabajador.column('#6', anchor=CENTER, width=100)
        self.arbolTrabajador.heading('#7', text='Cargo')
        self.arbolTrabajador.column('#7', anchor=CENTER, width=100)
        self.arbolTrabajador.heading('#8', text='Sueldo')
        self.arbolTrabajador.column('#8', anchor=CENTER, width=100)
        self.arbolTrabajador.heading('#9', text='Fecha Ingreso')
        self.arbolTrabajador.column('#9', anchor=CENTER, width=100)
        self.arbolTrabajador.heading('#10', text='Fecha Salida')
        self.arbolTrabajador.column('#10', anchor=CENTER, width=100)

        self.arbolTrabajador.pack(expand=True, fill="both", padx=15, pady=15)

    # Cargamos los datos iniciales en el Treeview
        self.cargarTrabajador()



    def cargarTrabajador(self):
        # Limpia el arbol antes de cargar nuevos datos
        self.arbolTrabajador.delete(*self.arbolTrabajador.get_children())
        
        # Obtiene los trabajador desde la capa de negocios
        trabajadores = self.capaNegocios.obtener_trabajador()
        
        # Inserta cada trabajador en el Treeview
        for trabajador in trabajadores:
            self.arbolTrabajador.insert("", "end", values=trabajador)

    def limpiarEntrys(self):
        self.entIdTrabajador.delete(0,'end')
        self.entNombre.delete(0,'end')
        self.entApPaterno.delete(0,'end')
        self.entApMaterno.delete(0,'end')
        self.entDireccion.delete(0,'end')
        self.entTelefono.delete(0,'end')
        self.entCargo.delete(0,'end')
        self.entSueldo.delete(0,'end')
        self.entFechaIngreso.delete(0,'end')
        self.entFechaSalida.delete(0,'end')
    #Insertar Datos Cliente
    def InsertarTrabajador(self):
        # obtenemos valores de Entrys
        id_trabajador = self.entIdTrabajador.get()
        nombre = self.entNombre.get()
        ap_paterno = self.entApPaterno.get()
        ap_materno = self.entApMaterno.get()
        direccion = self.entDireccion.get()
        telefono = self.entTelefono.get()
        cargo = self.entCargo.get()
        sueldo = self.entSueldo.get()
        f_ingreso = self.entFechaIngreso.get()
        f_egreso = self.entFechaSalida.get()

        # Llamamos al metodo inseratarCliente de la capa Negocios
        resultado = self.capaNegocios.insertar_trabajador(id_trabajador, nombre, ap_paterno, ap_materno, direccion, telefono, cargo, sueldo, f_ingreso, f_egreso)
       
        # Primero actualizamos el Treeview
        self.cargarTrabajador()

        # Mostramos el mensagebox after 100 ms
        
        if "Exito" in resultado:
            messagebox.showinfo("Exito", resultado)
                # Recarga los datos en el Treeview para mostrar el nuevo cliente
                #self.cargarCliente()
            self.limpiarEntrys()

        else: 
            messagebox.showerror("Error", resultado)
