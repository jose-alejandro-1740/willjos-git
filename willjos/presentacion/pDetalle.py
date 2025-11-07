import sys
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk

class Detalles:
    def __init__(self, frm1, frm3):
        #Limpiamos el frm1 antes de mostrar los elem de Detalles
        for widget in frm1.winfo_children():
            widget.destroy()
        frm1.pack_propagate(False)

        # Ahora creamos los frm Title, Entry y Crud
       
        self.frmTitle = ctk.CTkFrame(frm1, fg_color="transparent")
        self.frmTitle.pack(pady=10, padx=15, fill="x")
 
        self.frmEntrys = ctk.CTkFrame(frm1, fg_color="transparent")
        self.frmEntrys.pack(pady=10, padx=15, fill="x", expand=True)
        self.frmEntrys.grid_columnconfigure(1, weight=1)

      
        self.frmCrud = ctk.CTkFrame(frm1, fg_color="transparent")
        self.frmCrud.pack(pady=20, padx=15, fill="x", side="bottom")


    # Creamos los contenidos de los frm title, entrys y crud
        self.lblTitle = ctk.CTkLabel(self.frmTitle, text="Gestion Detalles", font=ctk.CTkFont(size=22, weight="bold"))
        self.lblTitle.pack(pady=10)

    # Colocamos los Entrys 

        self.lblIdDetalle = ctk.CTkLabel(self.frmEntrys, text="ID Detalle")
        self.lblIdDetalle.grid(row=0, column=0, padx=5, pady=5)
        self.entIdDetalle = ctk.CTkEntry(self.frmEntrys)
        self.entIdDetalle.grid(row=0, column=1, padx=10, pady=10)

        self.lblCantidad = ctk.CTkLabel(self.frmEntrys, text="Cantidad")
        self.lblCantidad.grid(row=1, column=0, padx=10, pady=10)
        self.entCantidad = ctk.CTkEntry(self.frmEntrys)
        self.entCantidad.grid(row=1, column=1, padx=10, pady=10)


        self.lblPrecioUnidad = ctk.CTkLabel(self.frmEntrys, text="Precio Unidad")
        self.lblPrecioUnidad.grid(row=2, column=0, padx=10, pady=10)
        self.entPrecioUnidad = ctk.CTkEntry(self.frmEntrys)
        self.entPrecioUnidad.grid(row=2, column=1, padx=10, pady=10)


        self.lblSubTotal = ctk.CTkLabel(self.frmEntrys, text="Sub Total")
        self.lblSubTotal.grid(row=3, column=0, padx=10, pady=10)
        self.entSubTotal = ctk.CTkEntry(self.frmEntrys)
        self.entSubTotal.grid(row=3, column=1, padx=10, pady=10)


        self.lblIdProveedor = ctk.CTkLabel(self.frmEntrys, text="Id Proveedor")
        self.lblIdProveedor.grid(row=4, column=0, padx=10, pady=10)
        self.entIdProveedor = ctk.CTkEntry(self.frmEntrys)
        self.entIdProveedor.grid(row=4, column=1, padx=10, pady=10)


        self.lblIdProducto = ctk.CTkLabel(self.frmEntrys, text="Id Producto")
        self.lblIdProducto.grid(row=5, column=0, padx=10, pady=10)
        self.entIdProducto = ctk.CTkEntry(self.frmEntrys)
        self.entIdProducto.grid(row=5, column=1, padx=10, pady=10)

    # Colocamos los Botones crud en frm Crud

        self.btnInsertar = ctk.CTkButton(self.frmCrud, text="Insertar", command= self.InsertarCliente)
        self.btnInsertar.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(0, weight=1)

        self.btnModificar = ctk.CTkButton(self.frmCrud, text="Modificar", command= self.modificarCliente)
        self.btnModificar.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(1, weight=1)

        self.btnEliminar = ctk.CTkButton(self.frmCrud, text="Eliminar", command= self.eliminarCliente)
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

        self.btnBuscar = ctk.CTkButton(self.frmCrud, text="Buscar", command= self.buscarCliente)
        self.btnBuscar.grid(row=1, column=2, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(2, weight=1)


# Tranbajamos en el Treeview en frm3
    #Limpiamos el frm3 antes de mostrar los elem de Cliente
        for widget in frm3.winfo_children():
            widget.destroy()
 
        self.lblArbolDetalle = ctk.CTkLabel(frm3, text="Registros de Detalles", font=ctk.CTkFont(size=18, weight="bold"))
        self.lblArbolDetalle.pack(pady=(15, 10))

    # Arbol Detalles
        self.arbolDetalle = ttk.Treeview(frm3, columns=('Id Detalle', 'Cantidad', 'Precio Unidad', 'Sub Total', 'Id Proveedor', 'Id Producto'), show='headings', height=5)
        self.arbolDetalle.heading('#1', text='Id Detalle')
        self.arbolDetalle.column('#1', anchor=CENTER, width=100)
        self.arbolDetalle.heading('#2', text='Cantidad')
        self.arbolDetalle.column('#2', anchor=CENTER, width=100)
        self.arbolDetalle.heading('#3', text='Precio Unidad')
        self.arbolDetalle.column('#3', anchor=CENTER, width=150)
        self.arbolDetalle.heading('#4', text='Sub Total')
        self.arbolDetalle.column('#4', anchor=CENTER, width=150)
        self.arbolDetalle.heading('#5', text='Id Proveedor')
        self.arbolDetalle.column('#5', anchor=CENTER, width=150)
        self.arbolDetalle.heading('#6', text='Id Producto')
        self.arbolDetalle.column('#6', anchor=CENTER, width=100)


        self.arbolDetalle.pack(expand=True, fill="both", padx=15, pady=15)

