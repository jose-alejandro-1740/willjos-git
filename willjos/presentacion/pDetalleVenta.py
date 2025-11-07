import sys
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk

class DetalleVenta:
    def __init__(self, frm1, frm3):
        #Limpiamos el frm1 antes de mostrar los elem de Cliente
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
        self.lblTitle = ctk.CTkLabel(self.frmTitle, text="Gestion Detalle Ventas", font=ctk.CTkFont(size=22, weight="bold"))
        self.lblTitle.pack(pady=10)

    # Colocamos los Entrys 
        self.lblIdDetalleVenta = tk.Label(self.frmEntrys, text="ID Detalle Venta")
        # Colocamos los Entrys
        self.lblIdDetalleVenta = ctk.CTkLabel(self.frmEntrys, text="ID Detalle Venta")
        self.lblIdDetalleVenta.grid(row=0, column=0, padx=5, pady=5)
        self.entIdDetalleVenta = ctk.CTkEntry(self.frmEntrys)
        self.entIdDetalleVenta.grid(row=0, column=1, padx=10, pady=10)

        self.lblCantidad = ctk.CTkLabel(self.frmEntrys, text="Cantidad")
        self.lblCantidad.grid(row=1, column=0, padx=10, pady=10)
        self.entCantidad = ctk.CTkEntry(self.frmEntrys)
        self.entCantidad.grid(row=1, column=1, padx=10, pady=10)


        self.lblPrecioUnidad = ctk.CTkLabel(self.frmEntrys, text="Precio Unidad")
        self.lblPrecioUnidad.grid(row=2, column=0, padx=10, pady=10)
        self.entPrecioUnidad = ctk.CTkEntry(self.frmEntrys)
        self.entPrecioUnidad.grid(row=2, column=1, padx=10, pady=10)


        self.lblSubTotal = ctk.CTkLabel(self.frmEntrys, text="IdVenta")
        self.lblSubTotal.grid(row=3, column=0, padx=10, pady=10)
        self.entSubTotal = ctk.CTkEntry(self.frmEntrys)
        self.entSubTotal.grid(row=3, column=1, padx=10, pady=10)


        self.lblIdVenta = ctk.CTkLabel(self.frmEntrys, text="Id Venta")
        self.lblIdVenta.grid(row=4, column=0, padx=10, pady=10)
        self.entIdVenta = ctk.CTkEntry(self.frmEntrys)
        self.entIdVenta.grid(row=4, column=1, padx=10, pady=10)


        self.lblIdProducto = ctk.CTkLabel(self.frmEntrys, text="Id Producto")
        self.lblIdProducto.grid(row=5, column=0, padx=10, pady=10)
        self.entIdProducto = ctk.CTkEntry(self.frmEntrys)
        self.entIdProducto.grid(row=5, column=1, padx=10, pady=10)

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

    #Limpiamos el frm1 antes de mostrar los elem de Cliente
    #Limpiamos el frm3 antes de mostrar los elem de Cliente
        for widget in frm3.winfo_children():
            widget.destroy()
       
        self.lblArbolDetalleVenta = tk.Label(frm3, text="Registro de Detalle de Ventas")
        self.lblArbolDetalleVenta = ctk.CTkLabel(frm3, text="Registro de Detalle de Ventas", font=ctk.CTkFont(size=18, weight="bold"))
        self.lblArbolDetalleVenta.pack(pady=(15, 10))

        
        # setup_treeview_style()
    # Arbol Cliente    
        self.arbolDetalleVenta = ttk.Treeview(frm3, columns=('Id Detalle Venta', 'Cantidad', 'Precio Unidad', 'Sub Total', 'Id Venta', 'Id Producto'), show='headings', height=5)
        self.arbolDetalleVenta.heading('#1', text='Id Detalle Venta')
        self.arbolDetalleVenta.column('#1', anchor=CENTER, width=50)
        self.arbolDetalleVenta.heading('#2', text='Cantidad')
        self.arbolDetalleVenta.column('#2', anchor=CENTER, width=150)
        self.arbolDetalleVenta.heading('#3', text='Precio Unidad')
        self.arbolDetalleVenta.column('#3', anchor=CENTER, width=150)
        self.arbolDetalleVenta.heading('#4', text='Sub Total')
        self.arbolDetalleVenta.column('#4', anchor=CENTER, width=150)
        self.arbolDetalleVenta.heading('#5', text='Id Venta')
        self.arbolDetalleVenta.column('#5', anchor=CENTER, width=150)
        self.arbolDetalleVenta.heading('#6', text='Id Producto')
        self.arbolDetalleVenta.column('#6', anchor=CENTER, width=100)


        self.arbolDetalleVenta.pack(expand=True, fill="both", padx=15, pady=15)

