import sys
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from negocios.nTrabajadorProyecto import nTrabajadorProyecto


class Trabajador_Proyecto:
    def __init__(self, frm1, frm3):

    #Instancia de la capa de negocios para poder usar sus métodos
        
        self.capaNegocios = nTrabajadorProyecto()

    #Limpiamos el frm1 antes de mostrar los elem de Trabajador_proyecto
        
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
        self.lblTitle = ctk.CTkLabel(self.frmTitle, text="Gestion Trabajador Proyecto", font=ctk.CTkFont(size=22, weight="bold"))
        self.lblTitle.pack(pady=10)

    # Colocamos los Entrys 
        
        self.lblIdTrabajador = ctk.CTkLabel(self.frmEntrys, text="ID Trabajador")
        self.lblIdTrabajador.grid(row=0, column=0, padx=5, pady=5)
        self.entIdTrabajador = ctk.CTkEntry(self.frmEntrys)
        self.entIdTrabajador.grid(row=0, column=1, padx=10, pady=10)

        self.lblIdProyecto = ctk.CTkLabel(self.frmEntrys, text="ID Proyecto")
        self.lblIdProyecto.grid(row=1, column=0, padx=10, pady=10)
        self.entIdProyecto = ctk.CTkEntry(self.frmEntrys)
        self.entIdProyecto.grid(row=1, column=1, padx=10, pady=10)


        self.lblRol = ctk.CTkLabel(self.frmEntrys, text="Rol")
        self.lblRol.grid(row=2, column=0, padx=10, pady=10)
        self.entRol = ctk.CTkEntry(self.frmEntrys)
        self.entRol.grid(row=2, column=1, padx=10, pady=10)

    # Colocamos los Botones crud en frm Crud

        self.btnInsertar = ctk.CTkButton(self.frmCrud, text="Insertar", command=self.insertarTrabajadorProyecto)
        self.btnInsertar.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(0, weight=1)

        self.btnModificar = ctk.CTkButton(self.frmCrud, text="Modificar", command= self.modificarTrabajadorProyecto)
        self.btnModificar.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(1, weight=1)

        self.btnEliminar = ctk.CTkButton(self.frmCrud, text="Eliminar",command=self.eliminarTrabajadorProyecto)
        self.btnEliminar.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(2, weight=1)

        self.btnReporte = ctk.CTkButton(self.frmCrud, text="Reporte")
        self.btnReporte.grid(row=0, column=3, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(3, weight=1)


        self.lblBuscarIdProyecto = ctk.CTkLabel(self.frmCrud, text="Id Proyecto")
        self.lblBuscarIdProyecto.grid(row=1, column=0, padx=10, pady=10)
        self.frmCrud.grid_columnconfigure(0, weight=1)

        self.entBuscar = ctk.CTkEntry(self.frmCrud)
        self.entBuscar.grid(row=1, column=1, padx=10, pady=10)
        self.frmCrud.grid_columnconfigure(1, weight=1)

        self.btnBuscar = ctk.CTkButton(self.frmCrud, text="Buscar", command=self.buscarTrabajadorProyecto)
        self.btnBuscar.grid(row=1, column=2, padx=5, pady=5, sticky="ew")
        self.frmCrud.grid_columnconfigure(2, weight=1)

    # Tranbajamos en el Treeview en frm3

    #Limpiamos el frm1 antes de mostrar los elem de Trabajador_Proyecto
    #Limpiamos el frm3 antes de mostrar los elem de Trabajador_Proyecto
        for widget in frm3.winfo_children():
            widget.destroy()
       
        self.lblArbolTrabajadorProyecto = tk.Label(frm3, text="Registros de Trabajador proyecto")
        self.lblArbolTrabajadorProyecto = ctk.CTkLabel(frm3, text="Registros de Trabajador proyecto", font=ctk.CTkFont(size=18, weight="bold"))
        self.lblArbolTrabajadorProyecto.pack(pady=(15, 10))


        # setup_treeview_style()
    # Arbol Trabajador_Proyecto
        self.arbolTrabajadorProyecto = ttk.Treeview(frm3, columns=('Id Trabajador', 'Id Proyecto', 'Rol'), show='headings', height=5)
        self.arbolTrabajadorProyecto.heading('#1', text='Id Trabajador')
        self.arbolTrabajadorProyecto.column('#1', anchor=CENTER, width=100)
        self.arbolTrabajadorProyecto.heading('#2', text='Id Proyecto')
        self.arbolTrabajadorProyecto.column('#2', anchor=CENTER, width=100)
        self.arbolTrabajadorProyecto.heading('#3', text='Rol')
        self.arbolTrabajadorProyecto.column('#3', anchor=CENTER, width=100)

        self.arbolTrabajadorProyecto.pack(expand=True, fill="both", padx=15, pady=15)

        # Para la seleccion del TreeView
        self.arbolTrabajadorProyecto.bind("<<TreeviewSelect>>", self.onSelectTrabajadorProyecto)

        # Cargamos los datos iniciales en el Treeview
        self.cargarTrabajadorProyecto()

    def cargarTrabajadorProyecto(self):
        # Limpia el arbol antes de cargar nuevos datos
        self.arbolTrabajadorProyecto.delete(*self.arbolTrabajadorProyecto.get_children())
        # Obtiene los clientes desde la capa de negocios
        registros = self.capaNegocios.obtener_trabajadorProyecto()
        # Inserta cada cliente en el Treeview
        for registro in registros:
            self.arbolTrabajadorProyecto.insert("", "end", values=registro)


    def limpiarEntrys(self):
        self.entIdTrabajador.delete(0,'end')
        self.entIdProyecto.delete(0,'end')
        self.entRol.delete(0,'end')
        self.entBuscar.delete(0, 'end')


    #Insertar Datos TrabajadorProyecto
    def insertarTrabajadorProyecto(self):
        # obtenemos valores de Entrys
        idTrabajador = self.entIdTrabajador.get()
        idProyecto = self.entIdProyecto.get()
        rol = self.entRol.get()

        # Llamamos al metodo insertar de la capa Negocios
        resultado = self.capaNegocios.insertar_trabajadorProyecto(idTrabajador, idProyecto, rol)
       
        # Primero actualizamos el Treeview
        self.cargarTrabajadorProyecto()

        
        if "Exito" in resultado:
            messagebox.showinfo("Exito", resultado)
            self.limpiarEntrys()

        else: 
            messagebox.showerror("Error", resultado)


    def buscarTrabajadorProyecto(self):
        idProyecto = self.entBuscar.get()
        if not idProyecto.strip():
            messagebox.showwarning("Advertencia ","Ingresar el id de proyecto a buscar.")
            return
        registros = self.capaNegocios.buscar_trabajadorProyecto(idProyecto)
        self.arbolTrabajadorProyecto.delete(*self.arbolTrabajadorProyecto.get_children())
        if registros: # Si es encontrado
            for registro in registros:
                self.arbolTrabajadorProyecto.insert("","end", values=registro)
            self.entBuscar.delete(0,'end')

        else:
            messagebox.showinfo("Informacion","No se encontraron registros con ese id de proyecto.")
            self.cargarTrabajadorProyecto()
            self.entBuscar.delete(0,'end')


    # Metodo Para Seleccionar en Treeview
    def onSelectTrabajadorProyecto(self, event):
        itemSeleccionado = self.arbolTrabajadorProyecto.selection()
        if itemSeleccionado:
            item = self.arbolTrabajadorProyecto.item(itemSeleccionado)
        # Obtenemos el Item  seleccionado
            registro = item["values"]
        
        # Cargamos los datos seleccionados en los entrys
            self.entIdTrabajador.delete(0,'end')
            self.entIdTrabajador.insert(0,registro[0])

            self.entIdProyecto.delete(0,'end')
            self.entIdProyecto.insert(0,registro[1])

            self.entRol.delete(0,'end')
            self.entRol.insert(0,registro[2])


    def eliminarTrabajadorProyecto(self):
        itemSeleccionado = self.arbolTrabajadorProyecto.selection()
        if itemSeleccionado:
            registro = self.arbolTrabajadorProyecto.item(itemSeleccionado)
            idTrabajador = registro["values"][0]
            resultado = self.capaNegocios.eliminar_trabajadorProyecto(idTrabajador)
            if "Exito" in resultado:
                messagebox.showinfo("Exito", resultado)
                self.arbolTrabajadorProyecto.delete(itemSeleccionado)
                self.limpiarEntrys()
            else:
                messagebox.showerror("Error", resultado)
        else:
            messagebox.showwarning("Advertencia ","Seleccione un registro para eliminar.")


    def modificarTrabajadorProyecto(self):
        itemSeleccionado = self.arbolTrabajadorProyecto.selection()
        if itemSeleccionado:
            try:
                registro = self.arbolTrabajadorProyecto.item(itemSeleccionado, 'values')
                if not registro:
                    messagebox.showerror("Error", "No se pudieron obtener los valores del registro seleccionado.")
                    return

                idTrabajador = registro[0]
                idProyecto = registro[1]
                nuevoRol = self.entRol.get()

                resultado = self.capaNegocios.modificar_trabajadorProyecto(idTrabajador, idProyecto, nuevoRol)

                if "Exito" in resultado:
                    messagebox.showinfo("Exito", resultado)
                    self.arbolTrabajadorProyecto.delete(*self.arbolTrabajadorProyecto.get_children())
                    self.cargarTrabajadorProyecto()
                    self.arbolTrabajadorProyecto.update()
                    self.limpiarEntrys()

                else:
                    messagebox.showerror("Error", resultado)
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error al modificar: {str(e)}")
        else:
            messagebox.showwarning("Advertencia ","Seleccione un registro para modificar.")
