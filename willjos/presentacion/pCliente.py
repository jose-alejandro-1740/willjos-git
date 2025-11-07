import sys
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from negocios.nCliente import nCliente

class Cliente:
    def __init__(self, frm1, frm3):

        # Instancia de la capa de negocios para poder usar sus métodos
        self.capaNegocios = nCliente()
      
        #Limpiamos el frm1 antes de mostrar los elem de Cliente
        for widget in frm1.winfo_children():
            widget.destroy()
        frm1.pack_propagate(False) # Evita que el frame cambie de tamaño

        # Ahora creamos los frm title, entrys y crud
        self.frmTitle = ctk.CTkFrame(frm1, fg_color="transparent")
        self.frmTitle.pack(pady=5, padx=5, fill="x")

        self.frmEntrys = ctk.CTkFrame(frm1, fg_color="transparent")
        self.frmEntrys.pack(pady=5, padx=5, fill="x", expand=True)
        self.frmEntrys.grid_columnconfigure(1, weight=1)

        self.frmCrud = ctk.CTkFrame(frm1, fg_color="transparent")
        self.frmCrud.pack(pady=10, padx=10, fill="x", side="bottom")


    # Creamos los contenidos de los frm title, entrys y crud
        self.lblTitle = ctk.CTkLabel(self.frmTitle, text="Gestion Clientes", font=ctk.CTkFont(size=22, weight="bold"))
        self.lblTitle.pack(pady=10)

    # Colocamos los Entrys 

        self.lblIdClinete = ctk.CTkLabel(self.frmEntrys, text="ID Cliente")
        self.lblIdClinete.grid(row=0, column=0, padx=5, pady=5)
        self.entIdClinete = ctk.CTkEntry(self.frmEntrys)
        self.entIdClinete.grid(row=0, column=1, padx=10, pady=10)

        self.lblnombre = ctk.CTkLabel(self.frmEntrys, text="Nombre")
        self.lblnombre.grid(row=1, column=0, padx=10, pady=10)
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


        self.lblBuscarNombreCliente = ctk.CTkLabel(self.frmCrud, text="Nombre")
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

        self.lblArbolCliente = ctk.CTkLabel(frm3, text="Registros de Clientes", font=ctk.CTkFont(size=18, weight="bold"))
        self.lblArbolCliente.pack(pady=(10, 10))

        # Arbol Cliente    
        self.arbolCliente = ttk.Treeview(frm3, columns=('Id Cliente', 'Nombre', 'Ap Paterno', 'Ap Materno', 'Direccion', 'Telefono'), show='headings', height=5)
        self.arbolCliente.heading('#1', text='Id Cliente')
        self.arbolCliente.column('#1', anchor=CENTER, width=50)
        self.arbolCliente.heading('#2', text='Nombre')
        self.arbolCliente.column('#2', anchor=CENTER, width=150)
        self.arbolCliente.heading('#3', text='Ap Paterno')
        self.arbolCliente.column('#3', anchor=CENTER, width=150)
        self.arbolCliente.heading('#4', text='Ap Materno')
        self.arbolCliente.column('#4', anchor=CENTER, width=150)
        self.arbolCliente.heading('#5', text='Direccion')
        self.arbolCliente.column('#5', anchor=CENTER, width=150)
        self.arbolCliente.heading('#6', text='Telefono')
        self.arbolCliente.column('#6', anchor=CENTER, width=100)

        self.arbolCliente.pack(expand=True, fill="both", padx=15, pady=15)

        # Para la seleccion del TreeView
        self.arbolCliente.bind("<<TreeviewSelect>>", self.onSelectCliente)

        # Cargamos los datos iniciales en el Treeview
        self.cargarCliente()

    def cargarCliente(self):
        # Limpia el arbol antes de cargar nuevos datos
        self.arbolCliente.delete(*self.arbolCliente.get_children())
        # Obtiene los clientes desde la capa de negocios
        clientes = self.capaNegocios.obtener_cliente()
        # Inserta cada cliente en el Treeview
        for cliente in clientes:
            self.arbolCliente.insert("", "end", values=cliente)


    def limpiarEntrys(self):
        self.entIdClinete.delete(0,'end')
        self.entNombre.delete(0,'end')
        self.entApPaterno.delete(0,'end')
        self.entApMaterno.delete(0,'end')
        self.entDireccion.delete(0,'end')
        self.entTelefono.delete(0,'end')


    #Insertar Datos Cliente
    def InsertarCliente(self):
        # obtenemos valores de Entrys
        idCliente = self.entIdClinete.get()
        nombre = self.entNombre.get()
        apPaterno = self.entApPaterno.get()
        apMaterno = self.entApMaterno.get()
        direccion = self.entDireccion.get()
        telefono = self.entTelefono.get()

        # Llamamos al metodo inseratarCliente de la capa Negocios
        resultado = self.capaNegocios.insertar_cliente(idCliente, nombre, apPaterno, apMaterno, direccion, telefono)
       
        # Primero actualizamos el Treeview
        self.cargarCliente()

        
        if "Exito" in resultado:
            messagebox.showinfo("Exito", resultado)
                # Recarga los datos en el Treeview para mostrar el nuevo cliente
                #self.cargarCliente()
            self.limpiarEntrys()

        else: 
            messagebox.showerror("Error", resultado)


    def buscarCliente(self):
        nombreCliente = self.entBuscar.get()
        if not nombreCliente.strip():
            messagebox.showwarning("Advertencia ","Ingresar el nombre del cliente. ")
            return
        clientes = self.capaNegocios.buscar_cliente(nombreCliente)
        self.arbolCliente.delete(*self.arbolCliente.get_children())
        if clientes: # Si es encontrado
            for cliente in clientes:
                self.arbolCliente.insert("","end", values=(cliente[0],cliente[1],cliente[2],cliente[3],cliente[4],cliente[5]))
            self.entBuscar.delete(0,'end')

        else:
            messagebox.showinfo("Informacion"," Cliente no encontrado")
            self.cargarCliente()
            self.entBuscar.delete(0,'end')


    # Metodo Para Seleccionar en Treeview
    def onSelectCliente(self, event):
        itemSeleccionado = self.arbolCliente.selection()
        if itemSeleccionado:
            item = self.arbolCliente.item(itemSeleccionado)
        # Obtenemos el Item  seleccionado
            cliente = item["values"]
        
        # Cargamos los datos seleccionados en los entrys
            self.entNombre.delete(0,'end')
            self.entNombre.insert(0,cliente[1])

            self.entApPaterno.delete(0,'end')
            self.entApPaterno.insert(0,cliente[2])

            self.entApMaterno.delete(0,'end')
            self.entApMaterno.insert(0,cliente[3])

            self.entDireccion.delete(0,'end')
            self.entDireccion.insert(0,cliente[4])

            self.entTelefono.delete(0,'end')
            self.entTelefono.insert(0,cliente[5])

            self.entIdClinete.delete(0,'end')
            self.entIdClinete.insert(0,cliente[0])


    def eliminarCliente(self):
        itemSeleccionado = self.arbolCliente.selection()
        if itemSeleccionado:
            cliente = self.arbolCliente.item(itemSeleccionado)
            idCliente = cliente["values"][0]
            resultado = self.capaNegocios.eliminar_cliente(idCliente)
            if "Exito" in resultado:
                messagebox.showinfo("Exito", resultado)

                #Elimina el cliente del arbol
                self.arbolCliente.delete(itemSeleccionado)
                self.limpiarEntrys()

            else:
                messagebox.showerror("Error", resultado)
        
        else:
            messagebox.showwarning("Advertencia ","Seleccione un Clienten para eliminar de la BD")


    def modificarCliente(self):
        itemSeleccionado =self.arbolCliente.selection()
        if itemSeleccionado:
            cliente = self.arbolCliente.item(itemSeleccionado)
            idCliente = cliente["values"][0]

        # Obtenemos los nuevos Valores

            nombre = self.entNombre.get()
            apPaterno = self.entApPaterno.get()
            apMaterno = self.entApMaterno.get()
            direccion = self.entDireccion.get()
            telefono = self.entTelefono.get()

        # Ahora Llamamos el metodo modificar de la Capa Negocios

            resultado = self.capaNegocios.modificar_cliente(idCliente, nombre, apPaterno, apMaterno, direccion, telefono)
            
            if "Exito" in resultado:
                messagebox.showinfo("Exito", resultado)
                self.arbolCliente.delete(*self.arbolCliente.get_children())
                self.cargarCliente()
                self.arbolCliente.update()
                self.limpiarEntrys()
            else:
                messagebox.showerror("Error",resultado)
        else:
            messagebox.showwarning("Advertencia ","seleccione un Cliente en el Arbol")

