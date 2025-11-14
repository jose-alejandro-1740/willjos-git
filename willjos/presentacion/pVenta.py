
import sys
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from negocios.nVenta import nVenta


class Venta:
    def __init__(self, frm1, frm3):

        # Instancia de la capa de negocios para poder usar sus métodos
        self.capaNegocios = nVenta()
 
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

        self.btnInsertar = ctk.CTkButton(self.frmCrud, text="Insertar", command = self.insertarVenta)
        self.btnInsertar.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(0, weight=1)

        self.btnModificar = ctk.CTkButton(self.frmCrud, text="Modificar", command = self.modificarVenta)
        self.btnModificar.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(1, weight=1)

        self.btnEliminar = ctk.CTkButton(self.frmCrud, text="Eliminar", command = self.eliminarVenta)
        self.btnEliminar.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(2, weight=1)

        self.btnReporte = ctk.CTkButton(self.frmCrud, text="Reporte")
        self.btnReporte.grid(row=0, column=3, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(3, weight=1)


        self.lblBuscarIdventa = ctk.CTkLabel(self.frmCrud, text="Id venta")
        self.lblBuscarIdventa.grid(row=1, column=0, padx=10, pady=10)
        self.frmCrud.grid_columnconfigure(0, weight=1)

        self.entBuscar = ctk.CTkEntry(self.frmCrud)
        self.entBuscar.grid(row=1, column=1, padx=10, pady=10)
        self.frmCrud.grid_columnconfigure(1, weight=1)

        self.btnBuscar = ctk.CTkButton(self.frmCrud, text="Buscar", command= self.buscarVenta)
        self.btnBuscar.grid(row=1, column=2, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(2, weight=1)

    # Tranbajamos en el Treeview en frm3

    #Limpiamos el frm1 antes de mostrar los elem de Venta
    #Limpiamos el frm3 antes de mostrar los elem de Venta
        for widget in frm3.winfo_children():
            widget.destroy()

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


        # Para la seleccion del TreeView
        self.arbolVenta.bind("<<TreeviewSelect>>", self.onSelectVenta)

        # Cargamos los datos iniciales en el Treeview
        self.cargarVenta()

    def cargarVenta(self):
        # Limpia el arbol antes de cargar nuevos datos
        self.arbolVenta.delete(*self.arbolVenta.get_children())
        # Obtiene las ventas desde la capa de negocios
        ventas = self.capaNegocios.obtener_venta()
        # Inserta cada venta en el Treeview
        for venta in ventas:
            self.arbolVenta.insert("", "end", values=venta)


    def limpiarEntrys(self):
        self.entIdVenta.delete(0,'end')
        self.entFecha.delete(0,'end')
        self.entTotal.delete(0,'end')
        self.entFormaPago.delete(0,'end')
        self.entIdCliente.delete(0,'end')


    #Insertar Datos Venta
    def insertarVenta(self):
        # obtenemos valores de Entrys
        idVenta = self.entIdVenta.get()
        fecha = self.entFecha.get()
        total = self.entTotal.get()
        formaPago = self.entFormaPago.get()
        idCliente = self.entIdCliente.get()

        # Llamamos al metodo insertarVenta de la capa Negocios
        resultado = self.capaNegocios.insertar_venta(idVenta, fecha, total, formaPago, idCliente)
       
        # Primero actualizamos el Treeview
        self.cargarVenta()

        if "Exito" in resultado:
            messagebox.showinfo("Exito", resultado)
                # Recarga los datos en el Treeview para mostrar la nueva venta
            self.limpiarEntrys()

        else: 
            messagebox.showerror("Error", resultado)


    def buscarVenta(self):
        idVenta = self.entBuscar.get()
        if not idVenta.strip():
            messagebox.showwarning("Advertencia ","Ingresar el ID de la venta.")
            return
        ventas = self.capaNegocios.buscar_venta(idVenta)
        self.arbolVenta.delete(*self.arbolVenta.get_children())
        if ventas: # Si es encontrado
            for venta in ventas:
                self.arbolVenta.insert("","end", values=(venta[0],venta[1],venta[2],venta[3],venta[4]))
            self.entBuscar.delete(0,'end')

        else:
            messagebox.showinfo("Informacion"," Venta no encontrada")
            self.cargarVenta()
            self.entBuscar.delete(0,'end')


    # Metodo Para Seleccionar en Treeview
    def onSelectVenta(self, event):
        itemSeleccionado = self.arbolVenta.selection()
        if itemSeleccionado:
            item = self.arbolVenta.item(itemSeleccionado)
        # Obtenemos el Item  seleccionado
            venta = item["values"]
        
        # Cargamos los datos seleccionados en los entrys
            self.entIdVenta.delete(0,'end')
            self.entIdVenta.insert(0,venta[0])

            self.entFecha.delete(0,'end')
            self.entFecha.insert(0,venta[1])

            self.entTotal.delete(0,'end')
            self.entTotal.insert(0,venta[2])

            self.entFormaPago.delete(0,'end')
            self.entFormaPago.insert(0,venta[3])

            self.entIdCliente.delete(0,'end')
            self.entIdCliente.insert(0,venta[4])


    def eliminarVenta(self):
        itemSeleccionado = self.arbolVenta.selection()
        if itemSeleccionado:
            venta = self.arbolVenta.item(itemSeleccionado)
            idVenta = venta["values"][0]
            resultado = self.capaNegocios.eliminar_venta(idVenta)
            if "Exito" in resultado:
                messagebox.showinfo("Exito", resultado)

                #Elimina la venta del arbol
                self.arbolVenta.delete(itemSeleccionado)
                self.limpiarEntrys()

            else:
                messagebox.showerror("Error", resultado)
        
        else:
            messagebox.showwarning("Advertencia ","Seleccione una Venta para eliminar de la BD")


    def modificarVenta(self):
        itemSeleccionado =self.arbolVenta.selection()
        if itemSeleccionado:
            venta = self.arbolVenta.item(itemSeleccionado)
            idVenta = venta["values"][0]

        # Obtenemos los nuevos Valores
            fecha = self.entFecha.get()
            total = self.entTotal.get()
            formaPago = self.entFormaPago.get()
            idCliente = self.entIdCliente.get()

        # Ahora Llamamos el metodo modificar de la Capa Negocios
            resultado = self.capaNegocios.modificar_venta(idVenta, fecha, total, formaPago, idCliente)
            
            if "Exito" in resultado:
                messagebox.showinfo("Exito", resultado)
                self.arbolVenta.delete(*self.arbolVenta.get_children())
                self.cargarVenta()
                self.arbolVenta.update()
                self.limpiarEntrys()
            else:
                messagebox.showerror("Error",resultado)
        else:
            messagebox.showwarning("Advertencia ","Seleccione una Venta en el Arbol")
