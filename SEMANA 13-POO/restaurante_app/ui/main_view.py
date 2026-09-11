import tkinter as tk
from tkinter import ttk

class MainView(tk.Frame):
    def __init__(self, parent, servicio, usuario_actual, on_logout):
        super().__init__(parent)
        self.servicio = servicio
        self.usuario_actual = usuario_actual
        self.on_logout = on_logout

        self.configure(padx=15, pady=15)
        self._crear_widgets()

    def _crear_widgets(self):
        header_frame = tk.Frame(self)
        header_frame.pack(fill="x", pady=5)

        tk.Label(
            header_frame,
            text=f"Bienvenido/a, {self.usuario_actual.nombre} ({self.usuario_actual.rol})",
            font=("Arial", 11, "bold")
        ).pack(side="left")

        tk.Button(
            header_frame,
            text="Cerrar Sesión",
            command=self.on_logout,
            bg="#f44336",
            fg="white"
        ).pack(side="right")

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, pady=10)

        # Tab Productos
        tab_productos = ttk.Frame(notebook)
        notebook.add(tab_productos, text="Productos")
        self._construir_tabla_productos(tab_productos)

        # Tab Usuarios
        tab_usuarios = ttk.Frame(notebook)
        notebook.add(tab_usuarios, text="Usuarios")
        self._construir_tabla_usuarios(tab_usuarios)

        # Tab Ventas (Pendiente)
        tab_ventas = ttk.Frame(notebook)
        notebook.add(tab_ventas, text="Ventas (Pendiente)")
        self._construir_tab_pendiente(tab_ventas)

    def _construir_tabla_productos(self, parent):
        columnas = ("ID", "Nombre", "Categoría", "Precio", "Stock")
        tabla = ttk.Treeview(parent, columns=columnas, show="headings", height=8)

        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, anchor="center", width=100)

        tabla.pack(fill="both", expand=True, padx=5, pady=5)

        for p in self.servicio.obtener_productos():
            tabla.insert("", "end", values=(p.id, p.nombre, p.categoria, f"${p.precio:.2f}", p.stock))

    def _construir_tabla_usuarios(self, parent):
        columnas = ("Username", "Nombre", "Rol")
        tabla = ttk.Treeview(parent, columns=columnas, show="headings", height=8)

        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, anchor="center", width=120)

        tabla.pack(fill="both", expand=True, padx=5, pady=5)

        for u in self.servicio.obtener_usuarios():
            tabla.insert("", "end", values=(u.username, u.nombre, u.rol))

    def _construir_tab_pendiente(self, parent):
        msg = "Módulo de Ventas en desarrollo.\nEstará disponible en las próximas entregas."
        tk.Label(parent, text=msg, font=("Arial", 10, "italic"), fg="gray").pack(expand=True)