import sys
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from negocios.nMaterial import nMaterial


class Material:
    def __init__(self, frm1, frm3):

        # Instancia de la capa de negocios para poder usar sus métodos
        self.capaNegocios = nMaterial()

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
        self.lblTitle = ctk.CTkLabel(self.frmTitle, text="Gestion Material", font=ctk.CTkFont(size=22, weight="bold"))
        self.lblTitle.pack(pady=10)

    # Colocamos los Entrys 
        self.lblIdMaterial = ctk.CTkLabel(self.frmEntrys, text="ID Material")
        self.lblIdMaterial.grid(row=0, column=0, padx=5, pady=5)
        self.entIdMaterial = ctk.CTkEntry(self.frmEntrys)
        self.entIdMaterial.grid(row=0, column=1, padx=10, pady=10)

        self.lblnombre = ctk.CTkLabel(self.frmEntrys, text="Nombre")
        self.lblnombre.grid(row=1, column=0, padx=10, pady=10)
        self.entNombre = ctk.CTkEntry(self.frmEntrys)
        self.entNombre.grid(row=1, column=1, padx=10, pady=10)


        self.lblDescripcion = ctk.CTkLabel(self.frmEntrys, text="Descripcion")
        self.lblDescripcion.grid(row=2, column=0, padx=10, pady=10)
        self.entDescripcion = ctk.CTkEntry(self.frmEntrys)
        self.entDescripcion.grid(row=2, column=1, padx=10, pady=10)


        self.lblTipo = ctk.CTkLabel(self.frmEntrys, text="Tipo")
        self.lblTipo.grid(row=3, column=0, padx=10, pady=10)
        self.entTipo = ctk.CTkEntry(self.frmEntrys)
        self.entTipo.grid(row=3, column=1, padx=10, pady=10)


        self.lblPrecio = ctk.CTkLabel(self.frmEntrys, text="Precio")
        self.lblPrecio.grid(row=4, column=0, padx=10, pady=10)
        self.entPrecio = ctk.CTkEntry(self.frmEntrys)
        self.entPrecio.grid(row=4, column=1, padx=10, pady=10)


        self.lblStock = ctk.CTkLabel(self.frmEntrys, text="Stock")
        self.lblStock.grid(row=5, column=0, padx=10, pady=10)
        self.entStock = ctk.CTkEntry(self.frmEntrys)
        self.entStock.grid(row=5, column=1, padx=10, pady=10)
        
        self.lblUnidad = ctk.CTkLabel(self.frmEntrys, text="Unidad")
        self.lblUnidad.grid(row=6, column=0, padx=10, pady=10)
        self.entUnidad = ctk.CTkEntry(self.frmEntrys)
        self.entUnidad.grid(row=6, column=1, padx=10, pady=10)
        
        self.lblIdProveedor = ctk.CTkLabel(self.frmEntrys, text="Id Proveedor")
        self.lblIdProveedor.grid(row=7, column=0, padx=10, pady=10)
        self.entIdProveedor = ctk.CTkEntry(self.frmEntrys)
        self.entIdProveedor.grid(row=7, column=1, padx=10, pady=10)

    # Colocamos los Botones crud en frm Crud

        self.btnInsertar = ctk.CTkButton(self.frmCrud, text="Insertar", command= self.InsertarMaterial)
        self.btnInsertar.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(0, weight=1)

        self.btnModificar = ctk.CTkButton(self.frmCrud, text="Modificar", command= self.modificarMaterial)
        self.btnModificar.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(1, weight=1)

        self.btnEliminar = ctk.CTkButton(self.frmCrud, text="Eliminar", command= self.eliminarMaterial)
        self.btnEliminar.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(2, weight=1)

        self.btnReporte = ctk.CTkButton(self.frmCrud, text="Reporte")
        self.btnReporte.grid(row=0, column=3, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(3, weight=1)


        self.lblBuscarMaterial = ctk.CTkLabel(self.frmCrud, text="Nombre material")
        self.lblBuscarMaterial.grid(row=1, column=0, padx=10, pady=10)
        self.frmCrud.grid_columnconfigure(0, weight=1)

        self.entBuscar = ctk.CTkEntry(self.frmCrud)
        self.entBuscar.grid(row=1, column=1, padx=10, pady=10)
        self.frmCrud.grid_columnconfigure(1, weight=1)

        self.btnBuscar = ctk.CTkButton(self.frmCrud, text="Buscar", command=self.buscarMaterial)
        self.btnBuscar.grid(row=1, column=2, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(2, weight=1)



    # Tranbajamos en el Treeview en frm3

    #Limpiamos el frm1 antes de mostrar los elem de Cliente
    #Limpiamos el frm3 antes de mostrar los elem de Cliente
        for widget in frm3.winfo_children():
            widget.destroy()
       
        self.lblArbolMaterial = tk.Label(frm3, text="Registros de Material")
        self.lblArbolMaterial = ctk.CTkLabel(frm3, text="Registros de Material", font=ctk.CTkFont(size=18, weight="bold"))
        self.lblArbolMaterial.pack(pady=(15, 10))

        
        # setup_treeview_style()
    # Arbol Cliente    
        self.arbolMaterial = ttk.Treeview(frm3, columns=('Id Material', 'Nombre', 'Descripcion', 'Tipo', 'Precio', 'Stock','Unidad','Id Proveedor'), show='headings', height=5)
        self.arbolMaterial.heading('#1', text='Id Material')
        self.arbolMaterial.column('#1', anchor=CENTER, width=50)
        self.arbolMaterial.heading('#2', text='Nombre')
        self.arbolMaterial.column('#2', anchor=CENTER, width=150)
        self.arbolMaterial.heading('#3', text='Descripcion')
        self.arbolMaterial.column('#3', anchor=CENTER, width=150)
        self.arbolMaterial.heading('#4', text='Tipo')
        self.arbolMaterial.column('#4', anchor=CENTER, width=100)
        self.arbolMaterial.heading('#5', text='Precio')
        self.arbolMaterial.column('#5', anchor=CENTER, width=100)
        self.arbolMaterial.heading('#6', text='Stock')
        self.arbolMaterial.column('#6', anchor=CENTER, width=50)
        self.arbolMaterial.heading('#7', text='Unidad')
        self.arbolMaterial.column('#7', anchor=CENTER, width=100)
        self.arbolMaterial.heading('#8', text='Id Proveedor')
        self.arbolMaterial.column('#8', anchor=CENTER, width=50)


        self.arbolMaterial.pack(expand=True, fill="both", padx=15, pady=15)


        # Para la seleccion del TreeView
        self.arbolMaterial.bind("<<TreeviewSelect>>", self.onSelectMaterial)

        # Cargamos los datos iniciales en el Treeview
        self.cargarMaterial()

    def cargarMaterial(self):
        # Limpia el arbol antes de cargar nuevos datos
        self.arbolMaterial.delete(*self.arbolMaterial.get_children())
        # Obtiene los material desde la capa de negocios
        materiales = self.capaNegocios.obtener_material()
        # Inserta cada material en el Treeview
        for material in materiales:
            self.arbolMaterial.insert("", "end", values=material)


    def limpiarEntrys(self):
        self.entIdMaterial.delete(0,'end')
        self.entNombre.delete(0,'end')
        self.entDescripcion.delete(0,'end')
        self.entTipo.delete(0,'end')
        self.entPrecio.delete(0,'end')
        self.entStock.delete(0,'end')
        self.entUnidad.delete(0,'end')
        self.entIdProveedor.delete(0,'end')

    #Insertar Datos Cliente
    def InsertarMaterial(self):
        # obtenemos valores de Entrys
        idMaterial = self.entIdMaterial.get()
        nombre = self.entNombre.get()
        descripcion = self.entDescripcion.get()
        tipo = self.entTipo.get()
        precio = self.entPrecio.get()
        stock = self.entStock.get()
        unidad = self.entUnidad.get()
        idProveedor = self.entIdProveedor.get()
        # Llamamos al metodo inseratarCliente de la capa Negocios
        resultado = self.capaNegocios.insertar_material(idMaterial, nombre, descripcion, tipo, precio, stock, unidad, idProveedor)
       
        # Primero actualizamos el Treeview
        self.cargarMaterial()

        
        if "Exito" in resultado:
            messagebox.showinfo("Exito", resultado)
                # Recarga los datos en el Treeview para mostrar el nuevo cliente
                #self.cargarCliente()
            self.limpiarEntrys()

        else: 
            messagebox.showerror("Error", resultado)


    def buscarMaterial(self):
        nombreMaterial = self.entBuscar.get()
        if not nombreMaterial.strip():
            messagebox.showwarning("Advertencia ","Ingresar el nombre del material.")
            return
        materiales = self.capaNegocios.buscar_material(nombreMaterial)
        self.arbolMaterial.delete(*self.arbolMaterial.get_children())
        if materiales: # Si es encontrado
            for material in materiales:
                self.arbolMaterial.insert("","end", values=(material[0],material[1],material[2],material[3],material[4],material[5],material[6],material[7]))
            self.entBuscar.delete(0,'end')

        else:
            messagebox.showinfo("Informacion"," Material no encontrado")
            self.cargarMaterial()
            self.entBuscar.delete(0,'end')


    # Metodo Para Seleccionar en Treeview
    def onSelectMaterial(self, event):
        itemSeleccionado = self.arbolMaterial.selection()
        if itemSeleccionado:
            item = self.arbolMaterial.item(itemSeleccionado)
        # Obtenemos el Item  seleccionado
            material = item["values"]
        
        # Cargamos los datos seleccionados en los entrys
            self.entNombre.delete(0,'end')
            self.entNombre.insert(0,material[1])

            self.entDescripcion.delete(0,'end')
            self.entDescripcion.insert(0,material[2])

            self.entTipo.delete(0,'end')
            self.entTipo.insert(0,material[3])

            self.entPrecio.delete(0,'end')
            self.entPrecio.insert(0,material[4])

            self.entStock.delete(0,'end')
            self.entStock.insert(0,material[5])

            self.entUnidad.delete(0,'end')
            self.entUnidad.insert(0,material[6])

            self.entIdProveedor.delete(0,'end')
            self.entIdProveedor.insert(0,material[7])

            self.entIdMaterial.delete(0,'end')
            self.entIdMaterial.insert(0,material[0])


    def eliminarMaterial(self):
        itemSeleccionado = self.arbolMaterial.selection()
        if itemSeleccionado:
            material = self.arbolMaterial.item(itemSeleccionado)
            idMaterial = material["values"][0]
            resultado = self.capaNegocios.eliminar_material(idMaterial)
            if "Exito" in resultado:
                messagebox.showinfo("Exito", resultado)

                #Elimina el cliente del arbol
                self.arbolMaterial.delete(itemSeleccionado)
                self.limpiarEntrys()

            else:
                messagebox.showerror("Error", resultado)
        
        else:
            messagebox.showwarning("Advertencia ","Seleccione un material para eliminar de la BD")


    def modificarMaterial(self):
        itemSeleccionado =self.arbolMaterial.selection()
        if itemSeleccionado:
            material = self.arbolMaterial.item(itemSeleccionado)
            idMaterial = material["values"][0]

        # Obtenemos los nuevos Valores

            nombre = self.entNombre.get()
            descripcion = self.entDescripcion.get()
            tipo = self.entTipo.get()
            precio = self.entPrecio.get()
            stock = self.entStock.get()
            unidad = self.entUnidad.get()
            proveedor = self.entIdProveedor.get()

        # Ahora Llamamos el metodo modificar de la Capa Negocios

            resultado = self.capaNegocios.modificar_material(idMaterial, nombre, descripcion, tipo, precio, stock, unidad, proveedor)
            
            if "Exito" in resultado:
                messagebox.showinfo("Exito", resultado)
                self.arbolMaterial.delete(*self.arbolMaterial.get_children())
                self.cargarMaterial()
                self.arbolMaterial.update()
                self.limpiarEntrys()
            else:
                messagebox.showerror("Error",resultado)
        else:
            messagebox.showwarning("Advertencia ","seleccione un material en el Arbol")
