
import sys
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk

class Venta:
    def __init__(self, frm1, frm3):
        #Limpiamos el frm1 antes de mostrar los elem de Venta
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
        self.lblTitle = ctk.CTkLabel(self.frmTitle, text="Gestion Ventas", font=ctk.CTkFont(size=22, weight="bold"))
        self.lblTitle.pack(pady=10)

    # Colocamos los Entrys 
        
        self.lblIdVenta = ctk.CTkLabel(self.frmEntrys, text="ID Venta")
        self.lblIdVenta.grid(row=0, column=0, padx=5, pady=5)
        self.entIdVenta = ctk.CTkEntry(self.frmEntrys)
        self.entIdVenta.grid(row=0, column=1, padx=10, pady=10)

        self.lblFecha = ctk.CTkLabel(self.frmEntrys, text="Fecha")
        self.lblFecha.grid(row=1, column=0, padx=10, pady=10)
        self.entFecha = ctk.CTkEntry(self.frmEntrys)
        self.entFecha.grid(row=1, column=1, padx=10, pady=10)


        self.lblTotal = ctk.CTkLabel(self.frmEntrys, text="Total")
        self.lblTotal.grid(row=2, column=0, padx=10, pady=10)
        self.entTotal = ctk.CTkEntry(self.frmEntrys)
        self.entTotal.grid(row=2, column=1, padx=10, pady=10)


        self.lblFormaPago = ctk.CTkLabel(self.frmEntrys, text="Forma de Pago")
        self.lblFormaPago.grid(row=3, column=0, padx=10, pady=10)
        self.entFormaPago = ctk.CTkEntry(self.frmEntrys)
        self.entFormaPago.grid(row=3, column=1, padx=10, pady=10)


        self.lblIdCliente = ctk.CTkLabel(self.frmEntrys, text="Id Cliente")
        self.lblIdCliente.grid(row=4, column=0, padx=10, pady=10)
        self.entIdCliente = ctk.CTkEntry(self.frmEntrys)
        self.entIdCliente.grid(row=4, column=1, padx=10, pady=10)

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

    #Limpiamos el frm1 antes de mostrar los elem de Venta
    #Limpiamos el frm3 antes de mostrar los elem de Venta
        for widget in frm3.winfo_children():
            widget.destroy()

        self.lblArbolVenta = tk.Label(frm3, text="Registros de Ventas")
        self.lblArbolVenta = ctk.CTkLabel(frm3, text="Registros de Ventas", font=ctk.CTkFont(size=18, weight="bold"))
        self.lblArbolVenta.pack(pady=(15, 10))

        
        # setup_treeview_style()
    # Arbol Venta    
        self.arbolVenta = ttk.Treeview(frm3, columns=('Id Venta', 'Fecha', 'Total', 'Forma de Pago', 'Id Cliente'), show='headings', height=5)
        self.arbolVenta.heading('#1', text='Id Venta')
        self.arbolVenta.column('#1', anchor=CENTER, width=50)
        self.arbolVenta.heading('#2', text='Fecha')
        self.arbolVenta.column('#2', anchor=CENTER, width=150)
        self.arbolVenta.heading('#3', text='Total')
        self.arbolVenta.column('#3', anchor=CENTER, width=150)
        self.arbolVenta.heading('#4', text='Forma de Pago')
        self.arbolVenta.column('#4', anchor=CENTER, width=150)
        self.arbolVenta.heading('#5', text='Id Cliente')
        self.arbolVenta.column('#5', anchor=CENTER, width=150)


        self.arbolVenta.pack(expand=True, fill="both", padx=15, pady=15)

