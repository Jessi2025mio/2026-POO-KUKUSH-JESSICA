import tkinter as tk
from tkinter import ttk, messagebox

class MainView(tk.Tk):
    def __init__(self, servicio, usuario_actual):
        super().__init__()
        self.servicio = servicio
        self.usuario_actual = usuario_actual

        self.title(f"Restaurante App - {self.usuario_actual.nombre} ({self.usuario_actual.rol})")
        self.geometry("820x540")
        self.minsize(750, 480)

        self._crear_componentes()
        self._cargar_tabla_usuarios()
        self._cargar_tabla_productos()

    def _crear_componentes(self):
        # Notebook para organizar pestañas
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Pestañas principales
        self.tab_productos = ttk.Frame(self.notebook)
        self.tab_usuarios = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_productos, text="  Gestión de Productos  ")
        self.notebook.add(self.tab_usuarios, text="  Consulta de Usuarios  ")

        self._construir_tab_productos()
        self._construir_tab_usuarios()

    # --- PESTAÑA: PRODUCTOS ---
    def _construir_tab_productos(self):
        # 1. Contenedor del Formulario (LabelFrame)
        frame_form = ttk.LabelFrame(self.tab_productos, text=" Datos del Producto ", padding=10)
        frame_form.pack(fill="x", padx=10, pady=5)

        # Campos en cuadrícula (grid)
        ttk.Label(frame_form, text="ID Producto:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.txt_prod_id = ttk.Entry(frame_form, width=15)
        self.txt_prod_id.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(frame_form, text="Nombre:").grid(row=0, column=2, sticky="w", padx=5, pady=5)
        self.txt_prod_nombre = ttk.Entry(frame_form, width=25)
        self.txt_prod_nombre.grid(row=0, column=3, sticky="w", padx=5, pady=5)

        ttk.Label(frame_form, text="Categoría:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.combo_categoria = ttk.Combobox(
            frame_form,
            values=["Comida Rapida", "Bebidas", "Postres", "Platos Fuertes", "Entradas"],
            state="readonly",
            width=18
        )
        self.combo_categoria.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(frame_form, text="Precio ($):").grid(row=1, column=2, sticky="w", padx=5, pady=5)
        self.txt_prod_precio = ttk.Entry(frame_form, width=15)
        self.txt_prod_precio.grid(row=1, column=3, sticky="w", padx=5, pady=5)

        # 2. Contenedor de Botones de Acción
        frame_acciones = ttk.Frame(self.tab_productos, padding=5)
        frame_acciones.pack(fill="x", padx=10, pady=5)

        ttk.Button(frame_acciones, text="Registrar", command=self._registrar_prod).pack(side="left", padx=5)
        ttk.Button(frame_acciones, text="Cargar/Consultar", command=self._cargar_prod).pack(side="left", padx=5)
        ttk.Button(frame_acciones, text="Actualizar", command=self._actualizar_prod).pack(side="left", padx=5)
        ttk.Button(frame_acciones, text="Eliminar", command=self._eliminar_prod).pack(side="left", padx=5)
        ttk.Button(frame_acciones, text="Limpiar Formulario", command=self._limpiar_formulario_prod).pack(side="left", padx=5)

        # 3. Contenedor de Visualización (Tabla Treeview)
        frame_tabla = ttk.LabelFrame(self.tab_productos, text=" Inventario de Productos ", padding=10)
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=5)

        columnas = ("id", "nombre", "categoria", "precio")
        self.tabla_productos = ttk.Treeview(frame_tabla, columns=columnas, show="headings")

        self.tabla_productos.heading("id", text="ID")
        self.tabla_productos.heading("nombre", text="Nombre")
        self.tabla_productos.heading("categoria", text="Categoría")
        self.tabla_productos.heading("precio", text="Precio ($)")

        self.tabla_productos.column("id", width=80, anchor="center")
        self.tabla_productos.column("nombre", width=250)
        self.tabla_productos.column("categoria", width=150)
        self.tabla_productos.column("precio", width=100, anchor="e")

        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tabla_productos.yview)
        self.tabla_productos.configure(yscrollcommand=scrollbar.set)

        self.tabla_productos.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    # --- PESTAÑA: USUARIOS ---
    def _construir_tab_usuarios(self):
        frame_tabla_usr = ttk.LabelFrame(self.tab_usuarios, text=" Usuarios del Sistema ", padding=10)
        frame_tabla_usr.pack(fill="both", expand=True, padx=10, pady=10)

        cols = ("username", "nombre", "rol")
        self.tabla_usuarios = ttk.Treeview(frame_tabla_usr, columns=cols, show="headings")

        self.tabla_usuarios.heading("username", text="Usuario")
        self.tabla_usuarios.heading("nombre", text="Nombre Completo")
        self.tabla_usuarios.heading("rol", text="Rol / Cargo")

        self.tabla_usuarios.column("username", width=120)
        self.tabla_usuarios.column("nombre", width=250)
        self.tabla_usuarios.column("rol", width=150)

        self.tabla_usuarios.pack(fill="both", expand=True)

    # --- ACCIONES DE PRODUCTOS ---
    def _cargar_tabla_productos(self):
        for item in self.tabla_productos.get_children():
            self.tabla_productos.delete(item)

        productos = self.servicio.obtener_productos()
        for p in productos:
            self.tabla_productos.insert(
                "", "end",
                values=(p.id_producto, p.nombre, p.categoria, f"{p.precio:.2f}")
            )

    def _registrar_prod(self):
        id_p = self.txt_prod_id.get().strip()
        nom = self.txt_prod_nombre.get().strip()
        cat = self.combo_categoria.get().strip()
        pre = self.txt_prod_precio.get().strip()

        exito, msg = self.servicio.registrar_producto(id_p, nom, cat, pre)
        if exito:
            messagebox.showinfo("Éxito", msg)
            self._limpiar_formulario_prod()
            self._cargar_tabla_productos()
        else:
            messagebox.showerror("Atención", msg)

    def _cargar_prod(self):
        id_p = self.txt_prod_id.get().strip()
        exito, msg, prod = self.servicio.buscar_producto_por_id(id_p)

        if exito and prod:
            self.txt_prod_nombre.delete(0, tk.END)
            self.txt_prod_nombre.insert(0, prod.nombre)

            self.combo_categoria.set(prod.categoria)

            self.txt_prod_precio.delete(0, tk.END)
            self.txt_prod_precio.insert(0, str(prod.precio))
            messagebox.showinfo("Información", msg)
        else:
            messagebox.showwarning("Atención", msg)

    def _actualizar_prod(self):
        id_p = self.txt_prod_id.get().strip()
        nom = self.txt_prod_nombre.get().strip()
        cat = self.combo_categoria.get().strip()
        pre = self.txt_prod_precio.get().strip()

        exito, msg = self.servicio.actualizar_producto(id_p, nom, cat, pre)
        if exito:
            messagebox.showinfo("Éxito", msg)
            self._limpiar_formulario_prod()
            self._cargar_tabla_productos()
        else:
            messagebox.showerror("Error", msg)

    def _eliminar_prod(self):
        id_p = self.txt_prod_id.get().strip()
        if not id_p:
            messagebox.showwarning("Atención", "Ingrese el ID del producto que desea eliminar.")
            return

        confirmar = messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar el producto '{id_p}'?")
        if confirmar:
            exito, msg = self.servicio.eliminar_producto(id_p)
            if exito:
                messagebox.showinfo("Éxito", msg)
                self._limpiar_formulario_prod()
                self._cargar_tabla_productos()
            else:
                messagebox.showerror("Error", msg)

    def _limpiar_formulario_prod(self):
        self.txt_prod_id.delete(0, tk.END)
        self.txt_prod_nombre.delete(0, tk.END)
        self.combo_categoria.set("")
        self.txt_prod_precio.delete(0, tk.END)

    # --- ACCIONES DE USUARIOS ---
    def _cargar_tabla_usuarios(self):
        for item in self.tabla_usuarios.get_children():
            self.tabla_usuarios.delete(item)

        usuarios = self.servicio.obtener_usuarios()
        for u in usuarios:
            self.tabla_usuarios.insert("", "end", values=(u.username, u.nombre, u.rol))