import sys
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from negocios.nMedidor import nMedidor

class Medidor:
    def __init__(self, frm1, frm3):

        # Instancia de la capa de negocios para poder usar sus métodos
        self.capaNegocios = nMedidor()
      
        #Limpiamos el frm1 antes de mostrar los elem de Medidor
        for widget in frm1.winfo_children():
            widget.destroy()
        frm1.pack_propagate(False) # Evita que el frame cambie de tamaño

        # Ahora creamos los frames para el título, las entradas y los botones CRUD
        self.frmTitle = ctk.CTkFrame(frm1, fg_color="transparent")
        self.frmTitle.pack(pady=5, padx=5, fill="x")

        self.frmEntrys = ctk.CTkFrame(frm1, fg_color="transparent")
        self.frmEntrys.pack(pady=5, padx=5, fill="x", expand=True)
        self.frmEntrys.grid_columnconfigure(1, weight=1)

        self.frmCrud = ctk.CTkFrame(frm1, fg_color="transparent")
        self.frmCrud.pack(pady=10, padx=10, fill="x", side="bottom")


    # Creamos los contenidos de los frm title, entrys y crud
        self.lblTitle = ctk.CTkLabel(self.frmTitle, text="Gestión de Medidores", font=ctk.CTkFont(size=22, weight="bold"))
        self.lblTitle.pack(pady=10)

    # Colocamos los Entrys 

        self.lblIdMedidor = ctk.CTkLabel(self.frmEntrys, text="ID Medidor")
        self.lblIdMedidor.grid(row=0, column=0, padx=5, pady=5)
        self.entIdMedidor = ctk.CTkEntry(self.frmEntrys)
        self.entIdMedidor.grid(row=0, column=1, padx=10, pady=10)

        self.lblDireccion = ctk.CTkLabel(self.frmEntrys, text="Direccion")
        self.lblDireccion.grid(row=1, column=0, padx=10, pady=10)
        self.entDireccion = ctk.CTkEntry(self.frmEntrys)
        self.entDireccion.grid(row=1, column=1, padx=10, pady=10)

    # Colocamos los Botones crud en frm Crud

        self.btnInsertar = ctk.CTkButton(self.frmCrud, text="Insertar", command= self.insertarMedidor)
        self.btnInsertar.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(0, weight=1)

        self.btnModificar = ctk.CTkButton(self.frmCrud, text="Modificar", command= self.modificarMedidor)
        self.btnModificar.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(1, weight=1)

        self.btnEliminar = ctk.CTkButton(self.frmCrud, text="Eliminar", command= self.eliminarMedidor)
        self.btnEliminar.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(2, weight=1)

        self.btnReporte = ctk.CTkButton(self.frmCrud, text="Reporte")
        self.btnReporte.grid(row=0, column=3, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(3, weight=1)

        self.lblBuscarDireccion = ctk.CTkLabel(self.frmCrud, text="Dirección")
        self.lblBuscarDireccion.grid(row=1, column=0, padx=10, pady=10)
        self.frmCrud.grid_columnconfigure(0, weight=1)

        self.entBuscar = ctk.CTkEntry(self.frmCrud)
        self.entBuscar.grid(row=1, column=1, padx=10, pady=10)
        self.frmCrud.grid_columnconfigure(1, weight=1)

        self.btnBuscar = ctk.CTkButton(self.frmCrud, text="Buscar", command= self.buscarMedidor)
        self.btnBuscar.grid(row=1, column=2, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(2, weight=1)
        
# Tranbajamos en el Treeview en frm3
    #Limpiamos el frm3 antes de mostrar los elem de Medidor
        for widget in frm3.winfo_children():
            widget.destroy()

        self.lblArbolMedidor = ctk.CTkLabel(frm3, text="Registros de Medidores", font=ctk.CTkFont(size=18, weight="bold"))
        self.lblArbolMedidor.pack(pady=(10, 10))

        # Arbol Medidor    
        self.arbolMedidor = ttk.Treeview(frm3, columns=('Id Medidor', 'Direccion'), show='headings', height=5)
        self.arbolMedidor.heading('#1', text='Id Medidor')
        self.arbolMedidor.column('#1', anchor=CENTER, width=100)
        self.arbolMedidor.heading('#2', text='Dirección')
        self.arbolMedidor.column('#2', anchor=CENTER, width=400)

        self.arbolMedidor.pack(expand=True, fill="both", padx=15, pady=15)

        # Para la seleccion del TreeView
        self.arbolMedidor.bind("<<TreeviewSelect>>", self.onSelectMedidor)

        # Cargamos los datos iniciales en el Treeview
        self.cargarMedidor()

    def cargarMedidor(self):
        # Limpia el arbol antes de cargar nuevos datos
        self.arbolMedidor.delete(*self.arbolMedidor.get_children())
        # Obtiene los medidores desde la capa de negocios
        medidores = self.capaNegocios.obtener_medidor()
        # Inserta cada medidor en el Treeview
        for medidor in medidores:
            self.arbolMedidor.insert("", "end", values=medidor)


    def limpiarEntrys(self):
        self.entIdMedidor.delete(0,'end')
        self.entDireccion.delete(0,'end')


    #Insertar Datos Medidor
    def insertarMedidor(self):
        # obtenemos valores de Entrys
        codMedidor = self.entIdMedidor.get()
        direccion = self.entDireccion.get()

        # Llamamos al metodo insertarMedidor de la capa Negocios
        resultado = self.capaNegocios.insertar_medidor(codMedidor, direccion)
       
        # Primero actualizamos el Treeview
        self.cargarMedidor()

        
        if "Exito" in resultado:
            messagebox.showinfo("Exito", resultado)
            self.limpiarEntrys()

        else: 
            messagebox.showerror("Error", resultado)


    def buscarMedidor(self):
        direccionMedidor = self.entBuscar.get()
        if not direccionMedidor.strip():
            messagebox.showwarning("Advertencia ","Ingresar la dirección del medidor.")
            return
        medidores = self.capaNegocios.buscar_medidor(direccionMedidor)
        self.arbolMedidor.delete(*self.arbolMedidor.get_children())
        if medidores: # Si es encontrado
            for medidor in medidores:
                self.arbolMedidor.insert("","end", values=(medidor[0],medidor[1]))
            self.entBuscar.delete(0,'end')

        else:
            messagebox.showinfo("Informacion"," Medidor no encontrado")
            self.cargarMedidor()
            self.entBuscar.delete(0,'end')


    # Metodo Para Seleccionar en Treeview
    def onSelectMedidor(self, event):
        itemSeleccionado = self.arbolMedidor.selection()
        if itemSeleccionado:
            item = self.arbolMedidor.item(itemSeleccionado)
        # Obtenemos el Item  seleccionado
            medidor = item["values"]
        
        # Cargamos los datos seleccionados en los entrys
            self.entDireccion.delete(0,'end')
            self.entDireccion.insert(0,medidor[1])


            self.entIdMedidor.delete(0,'end')
            self.entIdMedidor.insert(0,medidor[0])


    def eliminarMedidor(self):
        itemSeleccionado = self.arbolMedidor.selection()
        if itemSeleccionado:
            medidor = self.arbolMedidor.item(itemSeleccionado)
            codMedidor = medidor["values"][0]
            resultado = self.capaNegocios.eliminar_medidor(codMedidor)
            if "Exito" in resultado:
                messagebox.showinfo("Exito", resultado)

                #Elimina el medidor del arbol
                self.arbolMedidor.delete(itemSeleccionado)
                self.limpiarEntrys()

            else:
                messagebox.showerror("Error", resultado)
        
        else:
            messagebox.showwarning("Advertencia ","Seleccione un Medidor para eliminar de la BD")


    def modificarMedidor(self):
        itemSeleccionado =self.arbolMedidor.selection()
        if itemSeleccionado:
            medidor = self.arbolMedidor.item(itemSeleccionado)
            codMedidor = medidor["values"][0]

        # Obtenemos los nuevos Valores
            direccion = self.entDireccion.get()

        # Ahora Llamamos el metodo modificar de la Capa Negocios

            resultado = self.capaNegocios.modificar_medidor(codMedidor, direccion)
            
            if "Exito" in resultado:
                messagebox.showinfo("Exito", resultado)
                self.cargarMedidor()
                self.limpiarEntrys()
            else:
                messagebox.showerror("Error",resultado)
        else:
            messagebox.showwarning("Advertencia ","Seleccione un Medidor en el Arbol")
