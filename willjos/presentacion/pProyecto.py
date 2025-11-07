import sys
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk

class Proyecto:
    def __init__(self, frm1, frm3):
        #Limpiamos el frm1 antes de mostrar los elem de Proyecto
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
        self.lblTitle = ctk.CTkLabel(self.frmTitle, text="Gestion Proyectos", font=ctk.CTkFont(size=22, weight="bold"))
        self.lblTitle.pack(pady=10)

    # Colocamos los Entrys 
        
        self.lblIdProyecto = ctk.CTkLabel(self.frmEntrys, text="ID Proyecto")
        self.lblIdProyecto.grid(row=0, column=0, padx=5, pady=5)
        self.entIdProyecto = ctk.CTkEntry(self.frmEntrys)
        self.entIdProyecto.grid(row=0, column=1, padx=10, pady=10)

        self.lblnombre = ctk.CTkLabel(self.frmEntrys, text="Nombre")
        self.lblnombre.grid(row=1, column=0, padx=10, pady=10)
        self.entNombre = ctk.CTkEntry(self.frmEntrys)
        self.entNombre.grid(row=1, column=1, padx=10, pady=10)

        self.lblDireccion = ctk.CTkLabel(self.frmEntrys, text="Direccion")
        self.lblDireccion.grid(row=2, column=0, padx=10, pady=10)
        self.entDireccion = ctk.CTkEntry(self.frmEntrys)
        self.entDireccion.grid(row=2, column=1, padx=10, pady=10)


        self.lblFechaProyecto = ctk.CTkLabel(self.frmEntrys, text="Fecha Proyecto")
        self.lblFechaProyecto.grid(row=3, column=0, padx=10, pady=10)
        self.entFechaProyecto = ctk.CTkEntry(self.frmEntrys)
        self.entFechaProyecto.grid(row=3, column=1, padx=10, pady=10)


        self.lblDescuento = ctk.CTkLabel(self.frmEntrys, text="Descuento")
        self.lblDescuento.grid(row=4, column=0, padx=10, pady=10)
        self.entDescuento = ctk.CTkEntry(self.frmEntrys)
        self.entDescuento.grid(row=4, column=1, padx=10, pady=10)


        self.lblTotal = ctk.CTkLabel(self.frmEntrys, text="Total")
        self.lblTotal.grid(row=5, column=0, padx=10, pady=10)
        self.entTotal = ctk.CTkEntry(self.frmEntrys)
        self.entTotal.grid(row=5, column=1, padx=10, pady=10)


        self.lblIdCliente = ctk.CTkLabel(self.frmEntrys, text="ID Cliente")
        self.lblIdCliente.grid(row=6, column=0, padx=10, pady=10)
        self.entIdCliente = ctk.CTkEntry(self.frmEntrys)
        self.entIdCliente.grid(row=6, column=1, padx=10, pady=10)

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

    #Limpiamos el frm1 antes de mostrar los elem de Proyecto
    #Limpiamos el frm3 antes de mostrar los elem de Proyecto
        for widget in frm3.winfo_children():
            widget.destroy()

        self.lblArbolProyecto = tk.Label(frm3, text="Registros de Proyecto")
        self.lblArbolProyecto = ctk.CTkLabel(frm3, text="Registros de Proyecto", font=ctk.CTkFont(size=18, weight="bold"))
        self.lblArbolProyecto.pack(pady=(15, 10))

        
        # setup_treeview_style()
    # Arbol Proyecto    
        self.arbolProyecto = ttk.Treeview(frm3, columns=('Id Proyecto', 'Nombre', 'Direccion', 'Fecha Proyecto', 'Descuento', 'Total', 'Id Cliente'), show='headings', height=5)
        self.arbolProyecto.heading('#1', text='Id Proyecto')
        self.arbolProyecto.column('#1', anchor=CENTER, width=50)
        self.arbolProyecto.heading('#2', text='Nombre')
        self.arbolProyecto.column('#2', anchor=CENTER, width=150)
        self.arbolProyecto.heading('#3', text='Direccion')
        self.arbolProyecto.column('#3', anchor=CENTER, width=150)
        self.arbolProyecto.heading('#4', text='Fecha Proyecto')
        self.arbolProyecto.column('#4', anchor=CENTER, width=150)
        self.arbolProyecto.heading('#5', text='Descuento')
        self.arbolProyecto.column('#5', anchor=CENTER, width=150)
        self.arbolProyecto.heading('#6', text='Total')
        self.arbolProyecto.column('#6', anchor=CENTER, width=100)
        self.arbolProyecto.heading('#7', text='Id Cliente')
        self.arbolProyecto.column('#7', anchor=CENTER, width=100)


        self.arbolProyecto.pack(expand=True, fill="both", padx=15, pady=15)

