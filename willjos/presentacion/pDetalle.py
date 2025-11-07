import sys
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from negocios.nDetalles import nDetalles

class Detalles:
    def __init__(self, frm1, frm3):

        # Instancia de la capa de negocios para poder usar sus métodos
        self.capaNegocios = nDetalles()

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

        self.btnInsertar = ctk.CTkButton(self.frmCrud, text="Insertar", command= self.InsertarDetalle)
        self.btnInsertar.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(0, weight=1)

        self.btnModificar = ctk.CTkButton(self.frmCrud, text="Modificar", command= self.modificarDetalle)
        self.btnModificar.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(1, weight=1)

        self.btnEliminar = ctk.CTkButton(self.frmCrud, text="Eliminar", command= self.eliminarDetalle)
        self.btnEliminar.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(2, weight=1)

        self.btnReporte = ctk.CTkButton(self.frmCrud, text="Reporte")
        self.btnReporte.grid(row=0, column=3, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(3, weight=1)


        self.lblBuscarNombreCliente = ctk.CTkLabel(self.frmCrud, text="Id detalle")
        self.lblBuscarNombreCliente.grid(row=1, column=0, padx=10, pady=10)
        self.frmCrud.grid_columnconfigure(0, weight=1)

        self.entBuscar = ctk.CTkEntry(self.frmCrud)
        self.entBuscar.grid(row=1, column=1, padx=10, pady=10)
        self.frmCrud.grid_columnconfigure(1, weight=1)

        self.btnBuscar = ctk.CTkButton(self.frmCrud, text="Buscar", command= self.buscarDetalle )
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

        # Para la seleccion del TreeView
        self.arbolDetalle.bind("<<TreeviewSelect>>", self.onSelectDetalle)

        # Cargamos los datos iniciales en el Treeview
        self.cargarDetalle()

    def cargarDetalle(self):
        # Limpia el arbol antes de cargar nuevos datos
        self.arbolDetalle.delete(*self.arbolDetalle.get_children())
        # Obtiene los clientes desde la capa de negocios
        detalles = self.capaNegocios.obtener_detalles()
        # Inserta cada cliente en el Treeview
        for detalle in detalles:
            self.arbolDetalle.insert("", "end", values=detalle)


    def limpiarEntrys(self):
        self.entIdDetalle.delete(0,'end')
        self.entCantidad.delete(0,'end')
        self.entPrecioUnidad.delete(0,'end')
        self.entSubTotal.delete(0,'end')
        self.entIdProveedor.delete(0,'end')
        self.entIdProducto.delete(0,'end')


    #Insertar Datos Cliente
    def InsertarDetalle(self):
        # obtenemos valores de Entrys
        idDetalle = self.entIdDetalle.get()
        cantidad = self.entCantidad.get()
        precioUnidad = self.entPrecioUnidad.get()
        subTotal = self.entSubTotal.get()
        idProveedor = self.entIdProveedor.get()
        idProducto = self.entIdProducto.get()

        # Llamamos al metodo inseratarCliente de la capa Negocios
        resultado = self.capaNegocios.insertar_detalles(idDetalle, cantidad, precioUnidad, subTotal, idProveedor, idProducto)
       
        # Primero actualizamos el Treeview
        self.cargarDetalle()
       
        if "Exito" in resultado:
            messagebox.showinfo("Exito", resultado)
                # Recarga los datos en el Treeview para mostrar el nuevo cliente
            self.limpiarEntrys()

        else: 
            messagebox.showerror("Error", resultado)


    def buscarDetalle(self):
        id_detalle = self.entBuscar.get()
        if not id_detalle.strip():
            messagebox.showwarning("Advertencia ","Ingresar el id detalle. ")
            return
        detalles = self.capaNegocios.buscar_detalles(id_detalle)
        self.arbolDetalle.delete(*self.arbolDetalle.get_children())
        if detalles: # Si es encontrado
            for detalle in detalles:
                self.arbolDetalle.insert("","end", values=(detalle[0],detalle[1],detalle[2],detalle[3],detalle[4],detalle[5]))
            self.entBuscar.delete(0,'end')

        else:
            messagebox.showinfo("Informacion", "Detalle no encontrado")
            self.cargarDetalle()
            self.entBuscar.delete(0,'end')


    # Metodo Para Seleccionar en Treeview
    def onSelectDetalle(self, event):
        itemSeleccionado = self.arbolDetalle.selection()
        if itemSeleccionado:
            item = self.arbolDetalle.item(itemSeleccionado)
        # Obtenemos el Item  seleccionado
            detalle = item["values"]
        
        # Cargamos los datos seleccionados en los entrys
            self.entCantidad.delete(0,'end')
            self.entCantidad.insert(0,detalle[1])

            self.entPrecioUnidad.delete(0,'end')
            self.entPrecioUnidad.insert(0,detalle[2])

            self.entSubTotal.delete(0,'end')
            self.entSubTotal.insert(0,detalle[3])

            self.entIdProveedor.delete(0,'end')
            self.entIdProveedor.insert(0,detalle[4])

            self.entIdProducto.delete(0,'end')
            self.entIdProducto.insert(0,detalle[5])

            self.entIdDetalle.delete(0,'end')
            self.entIdDetalle.insert(0,detalle[0])


    def eliminarDetalle(self):
        itemSeleccionado = self.arbolDetalle.selection()
        if itemSeleccionado:
            detalle = self.arbolDetalle.item(itemSeleccionado)
            idDetalle = detalle["values"][0]
            resultado = self.capaNegocios.eliminar_detalles(idDetalle)
            if "Exito" in resultado:
                messagebox.showinfo("Exito", resultado)

                #Elimina el cliente del arbol
                self.arbolDetalle.delete(itemSeleccionado)
                self.limpiarEntrys()

            else:
                messagebox.showerror("Error", resultado)
        
        else:
            messagebox.showwarning("Advertencia ","Seleccione un detalle para eliminar de la BD")


    def modificarDetalle(self):
        itemSeleccionado =self.arbolDetalle.selection()
        if itemSeleccionado:
            detalle = self.arbolDetalle.item(itemSeleccionado)
            idDetalle = detalle["values"][0]

        # Obtenemos los nuevos Valores

            cantidad = self.entCantidad.get()
            precioUnidad = self.entPrecioUnidad.get()
            subTotal = self.entSubTotal.get()
            idProveedor = self.entIdProveedor.get()
            idProducto = self.entIdProducto.get()

        # Ahora Llamamos el metodo modificar de la Capa Negocios

            resultado = self.capaNegocios.modificar_detalles(idDetalle, cantidad, precioUnidad, subTotal, idProveedor, idProducto)
            
            if "Exito" in resultado:
                messagebox.showinfo("Exito", resultado)
                self.arbolDetalle.delete(*self.arbolDetalle.get_children())
                self.cargarDetalle()
                self.arbolDetalle.update()
                self.limpiarEntrys()
            else:
                messagebox.showerror("Error",resultado)
        else:
            messagebox.showwarning("Advertencia ","seleccione un Cliente en el Arbol")

