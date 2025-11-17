import sys
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from negocios.nDetalleVenta import nDetalleVenta

class DetalleVenta:
    def __init__(self, frm1, frm3):

        # Instancia de la capa de negocios para poder usar sus métodos
        self.capaNegocios = nDetalleVenta()

        #Limpiamos el frm1 antes de mostrar los elem de detalle venta
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

        self.btnInsertar = ctk.CTkButton(self.frmCrud, text="Insertar", command=self.InsertarDetalleVenta)
        self.btnInsertar.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(0, weight=1)

        self.btnModificar = ctk.CTkButton(self.frmCrud, text="Modificar", command=self.modificarDetalleVenta)
        self.btnModificar.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(1, weight=1)

        self.btnEliminar = ctk.CTkButton(self.frmCrud, text="Eliminar", command=self.eliminarDetalleVenta)
        self.btnEliminar.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(2, weight=1)

        self.btnReporte = ctk.CTkButton(self.frmCrud, text="Reporte")
        self.btnReporte.grid(row=0, column=3, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(3, weight=1)


        self.lblBuscarIdDetalleVenta = ctk.CTkLabel(self.frmCrud, text="Id detalle venta")
        self.lblBuscarIdDetalleVenta.grid(row=1, column=0, padx=10, pady=10)
        self.frmCrud.grid_columnconfigure(0, weight=1)

        self.entBuscar = ctk.CTkEntry(self.frmCrud)
        self.entBuscar.grid(row=1, column=1, padx=10, pady=10)
        self.frmCrud.grid_columnconfigure(1, weight=1)

        self.btnBuscar = ctk.CTkButton(self.frmCrud, text="Buscar", command= self.buscarDetalleVenta)
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


        # Para la seleccion del TreeView
        self.arbolDetalleVenta.bind("<<TreeviewSelect>>", self.onSelectDetalleVenta)

        # Cargamos los datos iniciales en el Treeview
        self.cargarDetalleVenta()

    def cargarDetalleVenta(self):
        # Limpia el arbol antes de cargar nuevos datos
        self.arbolDetalleVenta.delete(*self.arbolDetalleVenta.get_children())
        # Obtiene los clientes desde la capa de negocios
        DetalleVentas = self.capaNegocios.obtener_detalleVenta()
        # Inserta cada cliente en el Treeview
        for detalleVenta in DetalleVentas:
            self.arbolDetalleVenta.insert("", "end", values=detalleVenta)


    def limpiarEntrys(self):
        self.entIdDetalleVenta.delete(0,'end')
        self.entCantidad.delete(0,'end')
        self.entPrecioUnidad.delete(0,'end')
        self.entSubTotal.delete(0,'end')
        self.entIdVenta.delete(0,'end')
        self.entIdProducto.delete(0,'end')


    #Insertar Datos Cliente
    def InsertarDetalleVenta(self):
        # obtenemos valores de Entrys
        idDetalleVenta = self.entIdDetalleVenta.get()
        cantidad = self.entCantidad.get()
        precioUnidad = self.entPrecioUnidad.get()
        subTotal = self.entSubTotal.get()
        idVenta = self.entIdVenta.get()
        idProducto = self.entIdProducto.get()

        # Llamamos al metodo inseratarCliente de la capa Negocios
        resultado = self.capaNegocios.insertar_detalleVenta(idDetalleVenta, cantidad, precioUnidad, subTotal, idVenta, idProducto)
       
        # Primero actualizamos el Treeview
        self.cargarDetalleVenta()

        
        if "Exito" in resultado:
            messagebox.showinfo("Exito", resultado)
                # Recarga los datos en el Treeview para mostrar el nuevo dato
                #self.cargarCliente()
            self.limpiarEntrys()

        else: 
            messagebox.showerror("Error", resultado)


    def buscarDetalleVenta(self):
        idDetalleVenta = self.entBuscar.get()
        if not idDetalleVenta.strip():
            messagebox.showwarning("Advertencia ","Ingresar el id de detalle de venta. ")
            return
        detalleVentas = self.capaNegocios.buscar_detalleVenta(idDetalleVenta)
        self.arbolDetalleVenta.delete(*self.arbolDetalleVenta.get_children())
        if detalleVentas: # Si es encontrado
            for detalleVenta in detalleVentas:
                self.arbolDetalleVenta.insert("","end", values=(detalleVenta[0],detalleVenta[1],detalleVenta[2],detalleVenta[3],detalleVenta[4],detalleVenta[5]))
            self.entBuscar.delete(0,'end')

        else:
            messagebox.showinfo("Informacion"," Cliente no encontrado")
            self.cargarDetalleVenta()
            self.entBuscar.delete(0,'end')


    # Metodo Para Seleccionar en Treeview
    def onSelectDetalleVenta(self, event):
        itemSeleccionado = self.arbolDetalleVenta.selection()
        if itemSeleccionado:
            item = self.arbolDetalleVenta.item(itemSeleccionado)
        # Obtenemos el Item  seleccionado
            detalleVenta = item["values"]
        
        # Cargamos los datos seleccionados en los entrys
            self.entCantidad.delete(0,'end')
            self.entCantidad.insert(0,detalleVenta[1])

            self.entPrecioUnidad.delete(0,'end')
            self.entPrecioUnidad.insert(0,detalleVenta[2])

            self.entSubTotal.delete(0,'end')
            self.entSubTotal.insert(0,detalleVenta[3])

            self.entIdVenta.delete(0,'end')
            self.entIdVenta.insert(0,detalleVenta[4])

            self.entIdProducto.delete(0,'end')
            self.entIdProducto.insert(0,detalleVenta[5])

            self.entIdDetalleVenta.delete(0,'end')
            self.entIdDetalleVenta.insert(0,detalleVenta[0])


    def eliminarDetalleVenta(self):
        itemSeleccionado = self.arbolDetalleVenta.selection()
        if itemSeleccionado:
            detalleVenta = self.arbolDetalleVenta.item(itemSeleccionado)
            idDetalleVenta = detalleVenta["values"][0]
            resultado = self.capaNegocios.eliminar_detalleVenta(idDetalleVenta)
            if "Exito" in resultado:
                messagebox.showinfo("Exito", resultado)

                #Elimina el cliente del arbol
                self.arbolDetalleVenta.delete(itemSeleccionado)
                self.limpiarEntrys()

            else:
                messagebox.showerror("Error", resultado)
        
        else:
            messagebox.showwarning("Advertencia ","Seleccione un Id Detalle Venta para eliminar de la BD")


    def modificarDetalleVenta(self):
        itemSeleccionado =self.arbolDetalleVenta.selection()
        if itemSeleccionado:
            detalleVenta = self.arbolDetalleVenta.item(itemSeleccionado)
            idDetalleVenta = detalleVenta["values"][0]

        # Obtenemos los nuevos Valores

            cantidad = self.entCantidad.get()
            precioUnidad = self.entPrecioUnidad.get()
            subTotal = self.entSubTotal.get()
            idVenta = self.entIdVenta.get()
            idProducto = self.entIdProducto.get()

        # Ahora Llamamos el metodo modificar de la Capa Negocios

            resultado = self.capaNegocios.modificar_detalleVenta(idDetalleVenta, cantidad, precioUnidad, subTotal, idVenta, idProducto)
            
            if "Exito" in resultado:
                messagebox.showinfo("Exito", resultado)
                self.arbolDetalleVenta.delete(*self.arbolDetalleVenta.get_children())
                self.cargarDetalleVenta()
                self.arbolDetalleVenta.update()
                self.limpiarEntrys()
            else:
                messagebox.showerror("Error",resultado)
        else:
            messagebox.showwarning("Advertencia ","seleccione un Id de Detalle Venta en el Arbol")

