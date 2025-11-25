import sys
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from negocios.nProveedor import nProveedor

class Proveedor:
    def __init__(self, frm1, frm3):

        # Instancia de la capa de negocios para poder usar sus métodos
        self.capaNegocios = nProveedor()

        #Limpiamos el frm1 antes de mostrar los elem de Proveedor
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
        self.lblTitle = ctk.CTkLabel(self.frmTitle, text="Gestion de Proveedores", font=ctk.CTkFont(size=22, weight="bold"))
        self.lblTitle.pack(pady=10)

    # Colocamos los Entrys 

        self.lblIdProveedor = ctk.CTkLabel(self.frmEntrys, text="ID Proveedor")
        self.lblIdProveedor.grid(row=0, column=0, padx=5, pady=5)
        self.entIdProveedor = ctk.CTkEntry(self.frmEntrys)
        self.entIdProveedor.grid(row=0, column=1, padx=10, pady=10)

        self.lblNombre = ctk.CTkLabel(self.frmEntrys, text="Nombre")
        self.lblNombre.grid(row=1, column=0, padx=10, pady=10)
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


        self.lblEmail = ctk.CTkLabel(self.frmEntrys, text="E-mail")
        self.lblEmail.grid(row=6, column=0, padx=10, pady=10)
        self.entEmail = ctk.CTkEntry(self.frmEntrys)
        self.entEmail.grid(row=6, column=1, padx=10, pady=10)


        self.lblContacto = ctk.CTkLabel(self.frmEntrys, text="Contacto")
        self.lblContacto.grid(row=7, column=0, padx=10, pady=10)
        self.entContacto = ctk.CTkEntry(self.frmEntrys)
        self.entContacto.grid(row=7, column=1, padx=10, pady=10)

    # Colocamos los Botones crud en frm Crud

        self.btnInsertar = ctk.CTkButton(self.frmCrud, text="Insertar", command=self.InsertarProveedor)
        self.btnInsertar.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(0, weight=1)

        self.btnModificar = ctk.CTkButton(self.frmCrud, text="Modificar", command=self.modificarProveedor)
        self.btnModificar.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(1, weight=1)

        self.btnEliminar = ctk.CTkButton(self.frmCrud, text="Eliminar", command=self.eliminarProveedor)
        self.btnEliminar.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(2, weight=1)

        self.btnReporte = ctk.CTkButton(self.frmCrud, text="Reporte")
        self.btnReporte.grid(row=0, column=3, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(3, weight=1)


        self.lblBuscarNombreProveedor = ctk.CTkLabel(self.frmCrud, text="Nombre")
        self.lblBuscarNombreProveedor.grid(row=1, column=0, padx=10, pady=10)
        self.frmCrud.grid_columnconfigure(0, weight=1)

        self.entBuscar = ctk.CTkEntry(self.frmCrud)
        self.entBuscar.grid(row=1, column=1, padx=10, pady=10)
        self.frmCrud.grid_columnconfigure(1, weight=1)

        self.btnBuscar = ctk.CTkButton(self.frmCrud, text="Buscar", command=self.buscarProveedor)
        self.btnBuscar.grid(row=1, column=2, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(2, weight=1)

# Tranbajamos en el Treeview en frm3
    #Limpiamos el frm3 antes de mostrar los elem de Proveedor
        for widget in frm3.winfo_children():
            widget.destroy()

        self.lblArbolProveedor = ctk.CTkLabel(frm3, text="Registros de Proveedores", font=ctk.CTkFont(size=18, weight="bold"))
        self.lblArbolProveedor.pack(pady=(15, 10))

        
        # setup_treeview_style()
    # Arbol Proveedor    
        self.arbolProveedor = ttk.Treeview(frm3, columns=('Id Proveedor', 'Nombre', 'Ap Paterno', 'Ap Materno', 'Direccion', 'Telefono', 'Email', 'Contacto'), show='headings', height=5)
        self.arbolProveedor.heading('#1', text='Id Proveedor')
        self.arbolProveedor.column('#1', anchor=CENTER, width=50)
        self.arbolProveedor.heading('#2', text='Nombre')
        self.arbolProveedor.column('#2', anchor=CENTER, width=100)
        self.arbolProveedor.heading('#3', text='Ap Paterno')
        self.arbolProveedor.column('#3', anchor=CENTER, width=100)
        self.arbolProveedor.heading('#4', text='Ap Materno')
        self.arbolProveedor.column('#4', anchor=CENTER, width=100)
        self.arbolProveedor.heading('#5', text='Direccion')
        self.arbolProveedor.column('#5', anchor=CENTER, width=100)
        self.arbolProveedor.heading('#6', text='Telefono')
        self.arbolProveedor.column('#6', anchor=CENTER, width=100)
        self.arbolProveedor.heading('#7', text='Email')
        self.arbolProveedor.column('#7', anchor=CENTER, width=100)
        self.arbolProveedor.heading('#8', text='Contacto')
        self.arbolProveedor.column('#8', anchor=CENTER, width=100)

        self.arbolProveedor.pack(expand=True, fill="both", padx=15, pady=15)

        # Para la seleccion del TreeView
        self.arbolProveedor.bind("<<TreeviewSelect>>", self.onSelectProveedor)


        # Cargamos los datos iniciales en el Treeview
        self.cargarProveedor()

   
    def cargarProveedor(self):
        # Limpia el arbol antes de cargar nuevos datos
        self.arbolProveedor.delete(*self.arbolProveedor.get_children())
        # Obtiene los clientes desde la capa de negocios
        proveedores = self.capaNegocios.obtener_proveedor()
        # Inserta cada cliente en el Treeview
        for proveedor in proveedores:
            self.arbolProveedor.insert("", "end", values=proveedor)

    def limpiarEntrys(self):
        self.entIdProveedor.delete(0,'end')
        self.entNombre.delete(0,'end')
        self.entApPaterno.delete(0,'end')
        self.entApMaterno.delete(0,'end')
        self.entDireccion.delete(0,'end')
        self.entTelefono.delete(0,'end')
        self.entEmail.delete(0,'end')
        self.entContacto.delete(0,'end')


    def InsertarProveedor(self):
        # obtenemos valores de Entrys
        IdProveedor = self.entIdProveedor.get()
        nombre = self.entNombre.get()
        apPaterno = self.entApPaterno.get()
        apMaterno = self.entApMaterno.get()
        direccion = self.entDireccion.get()
        telefono = self.entTelefono.get()
        email = self.entEmail.get()
        contacto = self.entContacto.get()

        # Llamamos al metodo inseratarProveedor de la capa Negocios
        resultado = self.capaNegocios.insertar_proveedor(IdProveedor, nombre, apPaterno, apMaterno, direccion, telefono, email, contacto)
       
        # Primero actualizamos el Treeview
        self.cargarProveedor()

        # Mostramos el mensagebox after 100 ms
        
        if "Exito" in resultado:
            messagebox.showinfo("Exito", resultado)
                # Recarga los datos en el Treeview para mostrar el nuevo cliente
                #self.cargarCliente()
            self.limpiarEntrys()

        else: 
            messagebox.showerror("Error", resultado)



    def buscarProveedor(self):
        nombreProveedor = self.entBuscar.get()
        if not nombreProveedor.strip():
            messagebox.showwarning("Advertencia ","Ingresar el nombre del proveedor. ")
            return
        proveedores = self.capaNegocios.buscar_proveedor(nombreProveedor)
        self.arbolProveedor.delete(*self.arbolProveedor.get_children())
        if proveedores: # Si es encontrado
            for proveedor in proveedores:
                self.arbolProveedor.insert("","end", values=(proveedor[0],proveedor[1],proveedor[2],proveedor[3],proveedor[4],proveedor[5],proveedor[6],proveedor[7]))
            self.entBuscar.delete(0,'end')

        else:
            messagebox.showinfo("Informacion"," Proveedor no encontrado")
            self.cargarProveedor()
            self.entBuscar.delete(0,'end')


    # Metodo Para Seleccionar en Treeview
    def onSelectProveedor(self, event):
        itemSeleccionado = self.arbolProveedor.selection()
        if itemSeleccionado:
            item = self.arbolProveedor.item(itemSeleccionado)
        # Obtenemos el Item  seleccionado
            proveedor = item["values"]
        
        # Cargamos los datos seleccionados en los entrys
            self.entNombre.delete(0,'end')
            self.entNombre.insert(0,proveedor[1])

            self.entApPaterno.delete(0,'end')
            self.entApPaterno.insert(0,proveedor[2])

            self.entApMaterno.delete(0,'end')
            self.entApMaterno.insert(0,proveedor[3])

            self.entDireccion.delete(0,'end')
            self.entDireccion.insert(0,proveedor[4])

            self.entTelefono.delete(0,'end')
            self.entTelefono.insert(0,proveedor[5])

            self.entEmail.delete(0,'end')
            self.entEmail.insert(0,proveedor[6])

            self.entContacto.delete(0,'end')
            self.entContacto.insert(0,proveedor[7])

            self.entIdProveedor.delete(0,'end')
            self.entIdProveedor.insert(0,proveedor[0])


    def eliminarProveedor(self):
        itemSeleccionado = self.arbolProveedor.selection()
        if itemSeleccionado:
            proveedor = self.arbolProveedor.item(itemSeleccionado)
            idProveedor = proveedor["values"][0]
            resultado = self.capaNegocios.eliminar_proveedor(idProveedor)
            if "Exito" in resultado:
                messagebox.showinfo("Exito", resultado)

                #Elimina el cliente del arbol
                self.arbolProveedor.delete(itemSeleccionado)
                self.limpiarEntrys()

            else:
                messagebox.showerror("Error", resultado)
        
        else:
            messagebox.showwarning("Advertencia ","Seleccione un proveedor para eliminar de la BD")


    def modificarProveedor(self):
        itemSeleccionado =self.arbolProveedor.selection()
        if itemSeleccionado:
            proveedor = self.arbolProveedor.item(itemSeleccionado)
            idProveedor = proveedor["values"][0]

        # Obtenemos los nuevos Valores

            nombre = self.entNombre.get()
            apPaterno = self.entApPaterno.get()
            apMaterno = self.entApMaterno.get()
            direccion = self.entDireccion.get()
            telefono = self.entTelefono.get()
            email = self.entEmail.get()
            contacto = self.entContacto.get()

        # Ahora Llamamos el metodo modificar de la Capa Negocios

            resultado = self.capaNegocios.modificar_proveedor(idProveedor, nombre, apPaterno, apMaterno, direccion, telefono,email, contacto)
            
            if "Exito" in resultado:
                messagebox.showinfo("Exito", resultado)
                self.arbolProveedor.delete(*self.arbolProveedor.get_children())
                self.cargarProveedor()
                self.arbolProveedor.update()
                self.limpiarEntrys()
            else:
                messagebox.showerror("Error",resultado)
        else:
            messagebox.showwarning("Advertencia ","seleccione un proveedor en el Arbol")



