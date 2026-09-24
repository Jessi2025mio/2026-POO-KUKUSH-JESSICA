
import tkinter as tk
from tkinter import ttk, messagebox
import os
from servicios.restaurante_servicio import RestauranteServicio

class MainView(tk.Tk):
    def __init__(self, base_dir: str):
        super().__init__()
        self.base_dir = base_dir
        self.servicio = RestauranteServicio(base_dir)

        self.title("Sistema de Gestión de Restaurante")
        self.geometry("850x550")

        self.cargos_recursos_assets()
        self.construir_interfaz()

    def cargos_recursos_assets(self):
        """Carga de recursos visuales e íconos desde la carpeta assets/"""
        self.assets_dir = os.path.join(self.base_dir, "assets")
        # Nota: Si los íconos PNG fallan por formato, Tkinter soporta GIF/PGM por defecto
        # o PNG si la versión de Tkinter es >= 8.6
        try:
            logo_path = os.path.join(self.assets_dir, "logo.png")
            if os.path.exists(logo_path):
                self.img_logo = tk.PhotoImage(file=logo_path)
            else:
                self.img_logo = None
        except Exception:
            self.img_logo = None

    def construir_interfaz(self):
        # Cabecera / Banner Superior
        header_frame = ttk.Frame(self, padding=10)
        header_frame.pack(fill=tk.X)

        if self.img_logo:
            lbl_logo = ttk.Label(header_frame, image=self.img_logo)
            lbl_logo.pack(side=tk.LEFT, padx=10)

        ttk.Label(header_frame, text="RESTAURANTE APP - PANEL PRINCIPAL", font=("Arial", 16, "bold")).pack(side=tk.LEFT, padx=10)

        # Contenedor de Pestañas
        notebook = ttk.Notebook(self)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Pestañas
        self.tab_ventas = ttk.Frame(notebook, padding=10)
        self.tab_usuarios = ttk.Frame(notebook, padding=10)
        self.tab_productos = ttk.Frame(notebook, padding=10)

        notebook.add(self.tab_ventas, text=" Módulo Ventas ")
        notebook.add(self.tab_usuarios, text=" Usuarios ")
        notebook.add(self.tab_productos, text=" Productos ")

        self.construir_modulo_ventas()
        self.construir_modulo_usuarios()
        self.construir_modulo_productos()

    # ==========================================
    # MÓDULO VENTAS (Demostración de Eventos)
    # ==========================================
    def construir_modulo_ventas(self):
        # Frame de Formulario
        form_frame = ttk.LabelFrame(self.tab_ventas, text=" Registrar Nueva Venta ", padding=10)
        form_frame.pack(fill=tk.X, pady=5)

        ttk.Label(form_frame, text="Seleccionar Usuario:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.cb_usuarios = ttk.Combobox(form_frame, state="readonly", width=35)
        self.cb_usuarios.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Seleccionar Producto:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.cb_productos = ttk.Combobox(form_frame, state="readonly", width=35)
        self.cb_productos.grid(row=1, column=1, padx=5, pady=5)

        # BOTÓN CON EVENTO command= ASOCIADO A CALLBACK SIN PARÉNTESIS command=self.callback_registrar_venta
        btn_registrar = ttk.Button(form_frame, text="Registrar Venta", command=self.callback_registrar_venta)
        btn_registrar.grid(row=0, column=2, rowspan=2, padx=20, pady=5, ipady=10)

        # Tabla de Ventas (Treeview)
        table_frame = ttk.LabelFrame(self.tab_ventas, text=" Historial de Ventas ", padding=10)
        table_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        columnas = ("id", "usuario", "producto", "total", "fecha")
        self.tree_ventas = ttk.Treeview(table_frame, columns=columnas, show="headings", height=8)

        self.tree_ventas.heading("id", text="ID Venta")
        self.tree_ventas.heading("usuario", text="Usuario / Cliente")
        self.tree_ventas.heading("producto", text="Producto")
        self.tree_ventas.heading("total", text="Total ($)")
        self.tree_ventas.heading("fecha", text="Fecha / Hora")

        self.tree_ventas.column("id", width=60, anchor=tk.CENTER)
        self.tree_ventas.column("usuario", width=200)
        self.tree_ventas.column("producto", width=200)
        self.tree_ventas.column("total", width=80, anchor=tk.E)
        self.tree_ventas.column("fecha", width=150, anchor=tk.CENTER)

        self.tree_ventas.pack(fill=tk.BOTH, expand=True)

        self.cargar_datos_combos()
        self.actualizar_tabla_ventas()

    # --- CALLBACK DEL EVENTO REGISTRAR VENTA ---
    def callback_registrar_venta(self):
        """
        FLUJO DE EVENTOS:
        1. El usuario hace clic -> command= invoca esta función callback.
        2. Obtenemos datos de los Comboboxes de la interfaz.
        3. Delegamos validación y guardado a RestauranteServicio.
        4. Actualizamos la vista y notificamos al usuario.
        """
        sel_user = self.cb_usuarios.get()
        sel_prod = self.cb_productos.get()

        if not sel_user or not sel_prod:
            messagebox.showwarning("Atención", "Por favor seleccione un usuario y un producto.")
            return

        # Extraer ID (formato esperado: "101 - Nombre")
        try:
            id_usuario = int(sel_user.split(" - ")[0])
            id_producto = int(sel_prod.split(" - ")[0])
        except ValueError:
            messagebox.showerror("Error", "Error al procesar las selecciones.")
            return

        # Delegar la operación al Servicio (Capa Logica/Persistencia)
        exito, mensaje = self.servicio.registrar_venta(id_usuario, id_producto)

        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self.actualizar_tabla_ventas()
            self.cb_usuarios.set('')
            self.cb_productos.set('')
        else:
            messagebox.showerror("Error", mensaje)

    def cargar_datos_combos(self):
        usuarios = self.servicio.obtener_usuarios()
        productos = self.servicio.obtener_productos()

        self.cb_usuarios['values'] = [f"{u.id} - {u.nombre}" for u in usuarios]
        self.cb_productos['values'] = [f"{p.id} - {p.nombre} (${p.precio:.2f})" for p in productos]

    def actualizar_tabla_ventas(self):
        # Limpiar tabla
        for row in self.tree_ventas.get_children():
            self.tree_ventas.delete(row)

        # Cargar del servicio
        ventas = self.servicio.obtener_ventas()
        for v in ventas:
            self.tree_ventas.insert("", tk.END, values=(v.id_venta, v.usuario_nombre, v.producto_nombre, f"${v.total:.2f}", v.fecha))

    # ==========================================
    # MÓDULOS SECUNDARIOS (Consulta)
    # ==========================================
    def construir_modulo_usuarios(self):
        ttk.Label(self.tab_usuarios, text="Listado de Usuarios Registrados", font=("Arial", 11, "bold")).pack(anchor=tk.W, pady=5)
        tree = ttk.Treeview(self.tab_usuarios, columns=("id", "nombre", "rol"), show="headings")
        tree.heading("id", text="ID")
        tree.heading("nombre", text="Nombre Completo")
        tree.heading("rol", text="Rol")
        tree.pack(fill=tk.BOTH, expand=True)

        for u in self.servicio.obtener_usuarios():
            tree.insert("", tk.END, values=(u.id, u.nombre, u.rol))

    def construir_modulo_productos(self):
        ttk.Label(self.tab_productos, text="Catálogo de Productos", font=("Arial", 11, "bold")).pack(anchor=tk.W, pady=5)
        tree = ttk.Treeview(self.tab_productos, columns=("id", "nombre", "precio", "categoria"), show="headings")
        tree.heading("id", text="ID")
        tree.heading("nombre", text="Producto")
        tree.heading("precio", text="Precio ($)")
        tree.heading("categoria", text="Categoría")
        tree.pack(fill=tk.BOTH, expand=True)

        for p in self.servicio.obtener_productos():
            tree.insert("", tk.END, values=(p.id, p.nombre, f"${p.precio:.2f}", p.categoria))