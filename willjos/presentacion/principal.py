import sys
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk

from pCliente import Cliente
from pDetalle import Detalles
from pDetalleVenta import DetalleVenta
from pMaterial import Material
from pProducto import Producto
from pProveedor import Proveedor
from pProyecto import Proyecto
from pTrabajador import Trabajador
from pTrabajadorProyecto import Trabajador_Proyecto
from pVenta import Venta

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from negocios import nCliente

from PIL import Image, ImageTk
from PIL import Image


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Importamos la clase específica que necesitamos de la capa de datos
class Principal(ctk.CTk):
    def __init__(self, master= None):
        super().__init__(master)
        self.master = master
        #self.pack(fill="both", expand=True)


        self.title("Ventana Principal")
        self.geometry("1200x700")

        ctk.set_appearance_mode("Light")  # Modes: "System" (default), "Dark", "Light"
        ctk.set_default_color_theme("green")

        # Configuramos el grid para que se expanda
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(0, weight=1)

        # Frame 1 de opciones (izquierda)
        self.frm1 = ctk.CTkFrame(self)
        self.frm1.grid(row=0, column=0, rowspan=3, sticky="nswe", padx=20, pady=20)
        self.frm1.grid_rowconfigure(1, weight=1)

        # Frame 2 de opciones Button de BD
        self.frm2 = ctk.CTkFrame(self)
        self.frm2.grid(row=0, column=1, sticky="ew", padx=(0, 20), pady=(20, 10))

        # Ordenamos las coumnas y filas de los botones en frm2
        for i in range(4):  # Acomoda las columnas
            self.frm2.grid_columnconfigure(i, weight=1)
        for j in range(4):  # Acomoda las filas
            self.frm2.grid_rowconfigure(j, weight=1)

        # Frame 3 de opciones de Treeview BD
        self.frm3 = ctk.CTkFrame(self)
        self.frm3.grid(row=1, column=1, sticky="nsew", padx=(0, 20), pady=10)
        self.frm3.grid_rowconfigure(1, weight=1)

        self.frm4 = ctk.CTkFrame(self)
        self.frm4.grid(row=2, column=1, sticky="ewns", padx=(0, 20), pady=(10, 20))
        self.frm4.grid_rowconfigure(0, weight=1)
        self.frm4.grid_columnconfigure(0, weight=1)

    # Configuramos el grid para que se expanda
        self.grid_rowconfigure(0, weight=0) # Title row
        self.grid_rowconfigure(1, weight=1) # Treeview row
        self.grid_rowconfigure(2, weight=0) # Chatbox row
        # Elaboramos los botones para frm2
        self.lblTitulo = ctk.CTkLabel(self.frm2, text="Sistema Base de Datos Willjos", font=ctk.CTkFont(size=20, weight="bold"))
        self.lblTitulo.grid(row=0, column=0, columnspan=4, padx=10, pady=15, sticky="ew")

        buttons = [
            ("CLIENTE", lambda: Cliente(self.frm1, self.frm3)),
            ("DETALLE VENTA", lambda: DetalleVenta(self.frm1, self.frm3)),
            ("PRODUCTO", lambda: Producto(self.frm1, self.frm3)),
            ("PROYECTO", lambda: Proyecto(self.frm1, self.frm3)),
            ("DETALLE", lambda: Detalles(self.frm1, self.frm3)),
            ("MATERIAL", lambda: Material(self.frm1, self.frm3)),
            ("PROVEEDOR", lambda: Proveedor(self.frm1, self.frm3)),
            ("TRABAJADOR", lambda: Trabajador(self.frm1, self.frm3)),
            ("TRABAJADOR PROYECTO", lambda: Trabajador_Proyecto(self.frm1, self.frm3)),
            ("VENTA", lambda: Venta(self.frm1, self.frm3))
        ]

        for i, (text, command) in enumerate(buttons):
            row = i // 4 + 1
            col = i % 4
            btn = ctk.CTkButton(self.frm2, text=text, command=command, height=40)
            btn.grid(row=row, column=col, padx=10, pady=10, sticky="ew")

    # Cargamos img en self.Frm 1
        # Cargamos img en self.frm1
        try:
            basedir= os.path.dirname(os.path.abspath(__file__))
            dir_img = os.path.normpath(os.path.join(basedir,"..", "img" ))
            basedir = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(basedir, "img4.png")
            mi_img = ctk.CTkImage(light_image=Image.open(img_path),
                                  dark_image=Image.open(img_path),
                                  size=(250, 350))
            self.lblImg = ctk.CTkLabel(self.frm1, image=mi_img, text="")
            self.lblImg.grid(row=0, column=0, pady=(40, 0), padx=40)

        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
            self.lblImg = ctk.CTkLabel(self.frm1, text="Error al cargar imagen", font=ctk.CTkFont(size=16))
            self.lblImg.grid(row=0, column=0, pady=50, padx=20)

        # Colocamos un MSM en el FRM 3
        self.lblMsm = ctk.CTkLabel(self.frm3, text="BIENVENIDO AL SISTEMA DE GESTION DE WILLJOS", font=ctk.CTkFont(size=20))
        self.lblMsm.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        # Colocamos un saludo al Chatbox del sis en el FRM 4
        self.lblSaludo = ctk.CTkLabel(self.frm4, text="Area de interaccion con Chatbox", font=ctk.CTkFont(size=16))
        self.lblSaludo.grid(row=0, column=0, padx=20, pady=10)

    def setup_treeview_style(self):
        style = ttk.Style(self)
        style.theme_use("default")
        # Treeview style
        style.configure("Treeview",
                        background="#2a2d2e",
                        foreground="white",
                        rowheight=28,
                        fieldbackground="#343638",
                        bordercolor="#343638",
                        borderwidth=0, font=("Roboto", 20))
        style.map('Treeview', background=[('selected', '#227242')],foreground=[('selected', 'black')])
        # Heading style
        style.configure("Treeview.Heading",
                        background="#3c8d40",
                        foreground="white",
                        relief="flat", font=("Roboto",25, "bold"))
        style.map("Treeview.Heading", background=[('active', '#4caf50')])
        
if __name__ == "__main__":
    app = Principal()
    app.mainloop()


