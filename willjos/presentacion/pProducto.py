import sys
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from negocios.nProducto import nProducto

class Producto:
    def __init__(self, frm1, frm3):
        # Instancia de la capa de negocios para poder usar sus métodos
        self.capaNegocios = nProducto()

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
        self.lblTitle = ctk.CTkLabel(self.frmTitle, text="Gestion Producto", font=ctk.CTkFont(size=22, weight="bold"))
        self.lblTitle.pack(pady=10)

    # Colocamos los Entrys 
        self.lblIdProducto = ctk.CTkLabel(self.frmEntrys, text="ID Producto")
        self.lblIdProducto.grid(row=0, column=0, padx=5, pady=5)
        self.entIdProducto = ctk.CTkEntry(self.frmEntrys)
        self.entIdProducto.grid(row=0, column=1, padx=10, pady=10)

        self.lblnombre = ctk.CTkLabel(self.frmEntrys, text="Nombre")
        self.lblnombre.grid(row=1, column=0, padx=10, pady=10)
        self.entNombre = ctk.CTkEntry(self.frmEntrys)
        self.entNombre.grid(row=1, column=1, padx=10, pady=10)


        self.lblDescripcion = ctk.CTkLabel(self.frmEntrys, text="Descriocion")
        self.lblDescripcion.grid(row=2, column=0, padx=10, pady=10)
        self.entDescripcion = ctk.CTkEntry(self.frmEntrys)
        self.entDescripcion.grid(row=2, column=1, padx=10, pady=10)


        self.lblAncho = ctk.CTkLabel(self.frmEntrys, text="Ancho")
        self.lblAncho.grid(row=3, column=0, padx=10, pady=10)
        self.entAncho = ctk.CTkEntry(self.frmEntrys)
        self.entAncho.grid(row=3, column=1, padx=10, pady=10)


        self.lblAlto = ctk.CTkLabel(self.frmEntrys, text="Alto")
        self.lblAlto.grid(row=4, column=0, padx=10, pady=10)
        self.entAlto = ctk.CTkEntry(self.frmEntrys)
        self.entAlto.grid(row=4, column=1, padx=10, pady=10)


        self.lblPrecio = ctk.CTkLabel(self.frmEntrys, text="Precio")
        self.lblPrecio.grid(row=5, column=0, padx=10, pady=10)
        self.entPrecio = ctk.CTkEntry(self.frmEntrys)
        self.entPrecio.grid(row=5, column=1, padx=10, pady=10)

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


    #Limpiamos el frm3 antes de mostrar los elem de Cliente
        for widget in frm3.winfo_children():
            widget.destroy()
       
        self.lblArbolProducto = ctk.CTkLabel(frm3, text="Registro Productos", font=ctk.CTkFont(size=18, weight="bold"))
        self.lblArbolProducto.pack(pady=(15, 10))

    # Arbol Cliente    
        self.arbolProducto = ttk.Treeview(frm3, columns=('Id Producto', 'Nombre', 'Descripcion', 'Ancho', 'Alto', 'Precio'), show='headings', height=5)
        self.arbolProducto.heading('#1', text='Id Producto')
        self.arbolProducto.column('#1', anchor=CENTER, width=50)
        self.arbolProducto.heading('#2', text='Nombre')
        self.arbolProducto.column('#2', anchor=CENTER, width=150)
        self.arbolProducto.heading('#3', text='Descripcion')
        self.arbolProducto.column('#3', anchor=CENTER, width=150)
        self.arbolProducto.heading('#4', text='Ancho')
        self.arbolProducto.column('#4', anchor=CENTER, width=150)
        self.arbolProducto.heading('#5', text='Alto')
        self.arbolProducto.column('#5', anchor=CENTER, width=150)
        self.arbolProducto.heading('#6', text='Precio')
        self.arbolProducto.column('#6', anchor=CENTER, width=100)

        self.arbolProducto.pack(expand=True, fill="both", padx=15, pady=15)

        # Cargamos los datos iniciales en el Treeview
        self.cargarProducto()

    # Limpieza de ENTRYs
    def cargarProducto(self):
        # Limpia el arbol antes de cargar nuevos datos
        self.arbolProducto.delete(*self.arbolProducto.get_children())
        # Obtiene los datos desde la capa de negocios
        productos = self.capaNegocios.obtener_producto()
        # Inserta cada dato en el Treeview
        for producto in productos:
            self.arbolProducto.insert("", "end", values=producto)
    
    def limpiarEntrys(self):
        self.entIdProducto.delete(0,'end')
        self.entNombre.delete(0,'end')
        self.entDescripcion.delete(0,'end')
        self.entAncho.delete(0,'end')
        self.entAlto.delete(0,'end')
        self.entPrecio.delete(0,'end')

      #Insertar Datos Producto
    def InsertarProducto(self):
        # ontenemos valores de Entrys
        id_producto = self.entIdProducto.get()
        nombre = self.entNombre.get()
        descripcion = self.entDescripcion.get()
        ancho = self.entAncho.get()
        alto = self.entAlto.get()
        precio = self.entPrecio.get()

        # Llamamos al metodo inseratarProducto de la capa Negocios
        resultado = self.capaNegocios.insertar_producto(id_producto, nombre, descripcion, ancho, alto, precio)
       
        # Primero actualizamos el Treeview
        self.cargarProducto()

        # Mostramos el mensagebox after 100 ms
        
        if "Exito" in resultado:
            messagebox.showinfo("Exito", resultado)
                # Recarga los datos en el Treeview para mostrar el nuevo cliente
                #self.cargarCliente()
            self.limpiarEntrys()

        else: 
            messagebox.showerror("Error", resultado)


      




