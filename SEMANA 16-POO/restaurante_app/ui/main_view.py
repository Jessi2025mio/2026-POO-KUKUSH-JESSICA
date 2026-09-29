import tkinter as tk
from tkinter import ttk, messagebox
from servicios.restaurante_servicio import RestauranteServicio


class MainView(tk.Tk):
    """Vista principal del sistema que gestiona la navegación y el módulo de Usuarios."""

    def __init__(self, servicio: RestauranteServicio):
        super().__init__()
        self.servicio = servicio
        self.title("Restaurante App - Gestión de Usuarios")
        self.geometry("900x600")  # Correcto (sin espacios)
        self.minsize(850, 550)

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self._crear_interfaz()

    def _crear_interfaz(self):
        # Panel superior (Header)
        header = ttk.Frame(self, padding=10)
        header.pack(fill=tk.X, side=tk.TOP)

        lbl_titulo = ttk.Label(
            header,
            text=f"Restaurante App | Usuario: {self.servicio.usuario_actual.nombre} ({self.servicio.usuario_actual.rol})",
            font=("Helvetica", 12, "bold")
        )
        lbl_titulo.pack(side=tk.LEFT)

        # Panel de contenido
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Solo el Administrador ve el módulo de Usuarios
        if self.servicio.usuario_actual.rol == "Administrador":
            self.tab_usuarios = ttk.Frame(self.notebook)
            self.notebook.add(self.tab_usuarios, text="Gestión de Usuarios")
            self._construir_modulo_usuarios()
        else:
            tab_inicio = ttk.Frame(self.notebook)
            self.notebook.add(tab_inicio, text="Inicio")
            ttk.Label(tab_inicio, text="Bienvenido. Seleccione un módulo disponible.", font=("Helvetica", 14)).pack(
                pady=50)

    def _construir_modulo_usuarios(self):
        # Contenedor principal de Usuarios
        frame_main = ttk.Frame(self.tab_usuarios, padding=10)
        frame_main.pack(fill=tk.BOTH, expand=True)

        # --- FORMULARIO ---
        frame_form = ttk.LabelFrame(frame_main, text=" Formulario de Usuario ", padding=10)
        frame_form.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

        ttk.Label(frame_form, text="ID Usuario:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.txt_id = ttk.Entry(frame_form, width=22)
        self.txt_id.grid(row=0, column=1, pady=5)

        ttk.Label(frame_form, text="Nombre:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.txt_nombre = ttk.Entry(frame_form, width=22)
        self.txt_nombre.grid(row=1, column=1, pady=5)

        ttk.Label(frame_form, text="Usuario:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.txt_usuario = ttk.Entry(frame_form, width=22)
        self.txt_usuario.grid(row=2, column=1, pady=5)

        ttk.Label(frame_form, text="Contraseña:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.txt_clave = ttk.Entry(frame_form, show="*", width=22)
        self.txt_clave.grid(row=3, column=1, pady=5)

        ttk.Label(frame_form, text="Rol:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.cmb_rol = ttk.Combobox(frame_form, values=["Administrador", "Empleado", "Cliente"], state="readonly",
                                    width=19)
        self.cmb_rol.current(2)  # Predeterminado: Cliente
        self.cmb_rol.grid(row=4, column=1, pady=5)

        # --- BOTONES (Asociados con command=) ---
        frame_btn = ttk.Frame(frame_form, padding=5)
        frame_btn.grid(row=5, column=0, columnspan=2, pady=15)

        self.btn_registrar = ttk.Button(frame_btn, text="Registrar", command=self.action_registrar)
        self.btn_registrar.pack(fill=tk.X, pady=2)

        self.btn_actualizar = ttk.Button(frame_btn, text="Actualizar", command=self.action_actualizar)
        self.btn_actualizar.pack(fill=tk.X, pady=2)

        self.btn_eliminar = ttk.Button(frame_btn, text="Eliminar", command=self.action_eliminar)
        self.btn_eliminar.pack(fill=tk.X, pady=2)

        self.btn_limpiar = ttk.Button(frame_btn, text="Limpiar", command=self.action_limpiar)
        self.btn_limpiar.pack(fill=tk.X, pady=2)

        # --- TABLA TREEVIEW ---
        frame_tabla = ttk.LabelFrame(frame_main, text=" Usuarios Registrados ", padding=10)
        frame_tabla.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        columnas = ("id", "nombre", "usuario", "rol")
        self.tree = ttk.Treeview(frame_tabla, columns=columnas, show="headings", selectmode="browse")

        self.tree.heading("id", text="ID")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("usuario", text="Usuario")
        self.tree.heading("rol", text="Rol")

        self.tree.column("id", width=60, anchor=tk.CENTER)
        self.tree.column("nombre", width=150)
        self.tree.column("usuario", width=100)
        self.tree.column("rol", width=100, anchor=tk.CENTER)

        scrollbar = ttk.Scrollbar(frame_tabla, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # ==========================================
        #  EVENT BINDINGS (Semanas 16 - Requisito)
        # ==========================================
        # 1. Evento Virtual TreeviewSelect
        self.tree.bind("<<TreeviewSelect>>", self.on_treeview_select)

        # 2. Evento Virtual ComboboxSelected
        self.cmb_rol.bind("<<ComboboxSelected>>", self.on_combobox_change)

        # 3. Atajos de Teclado
        self.bind("<Return>", self.on_key_return)
        self.bind("<Escape>", self.on_key_escape)

        # Cargar datos iniciales
        self.actualizar_treeview()

    # --- CALLBACKS & EVENT HANDLERS ---

    def on_treeview_select(self, event):
        """Callback al seleccionar un registro de la tabla."""
        selected_item = self.tree.selection()
        if not selected_item:
            return

        item_values = self.tree.item(selected_item[0], "values")
        id_usuario = item_values[0]

        # Consultar directamente al servicio evitando datos sensibles en la UI
        u = self.servicio.buscar_usuario_por_id(id_usuario)
        if u:
            self.txt_id.delete(0, tk.END)
            self.txt_id.insert(0, u.id_usuario)
            self.txt_id.config(state="disabled")  # ID no modificable durante edición

            self.txt_nombre.delete(0, tk.END)
            self.txt_nombre.insert(0, u.nombre)

            self.txt_usuario.delete(0, tk.END)
            self.txt_usuario.insert(0, u.usuario)

            self.txt_clave.delete(0, tk.END)
            self.txt_clave.insert(0, "")  # No mostramos la clave por seguridad

            self.cmb_rol.set(u.rol)

    def on_combobox_change(self, event):
        """Callback al cambiar de rol en el Combobox."""
        nuevo_rol = self.cmb_rol.get()
        # Lógica de respuesta visual inmediata si se requiere
        print(f"[EVENT] Rol seleccionado: {nuevo_rol}")

    def on_key_return(self, event):
        """Atajo de teclado <Return> para confirmar registro."""
        # Solo ejecuta registro si el campo ID está habilitado (modo nuevo registro)
        if self.txt_id["state"] != "disabled":
            self.action_registrar()

    def on_key_escape(self, event):
        """Atajo de teclado <Escape> para limpiar el formulario y la selección."""
        self.action_limpiar()

    # --- MÉTODOS DE ACCIÓN (command=) ---

    def action_registrar(self):
        exito, msj = self.servicio.registrar_usuario(
            self.txt_id.get().strip(),
            self.txt_nombre.get().strip(),
            self.txt_usuario.get().strip(),
            self.txt_clave.get().strip(),
            self.cmb_rol.get()
        )
        if exito:
            messagebox.showinfo("Éxito", msj)
            self.actualizar_treeview()
            self.action_limpiar()
        else:
            messagebox.showwarning("Atención", msj)

    def action_actualizar(self):
        id_u = self.txt_id.get().strip()
        if not id_u:
            messagebox.showwarning("Atención", "Seleccione un usuario de la tabla para actualizar.")
            return

        exito, msj = self.servicio.actualizar_usuario(
            id_u,
            self.txt_nombre.get().strip(),
            self.txt_usuario.get().strip(),
            self.txt_clave.get().strip(),
            self.cmb_rol.get()
        )
        if exito:
            messagebox.showinfo("Éxito", msj)
            self.actualizar_treeview()
            self.action_limpiar()
        else:
            messagebox.showwarning("Atención", msj)

    def action_eliminar(self):
        id_u = self.txt_id.get().strip()
        if not id_u:
            messagebox.showwarning("Atención", "Seleccione un usuario de la tabla para eliminar.")
            return

        if messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar al usuario '{id_u}'?"):
            exito, msj = self.servicio.eliminar_usuario(id_u)
            if exito:
                messagebox.showinfo("Éxito", msj)
                self.actualizar_treeview()
                self.action_limpiar()
            else:
                messagebox.showerror("Error", msj)

    def action_limpiar(self):
        """Restablece el formulario al estado inicial."""
        self.txt_id.config(state="normal")
        self.txt_id.delete(0, tk.END)
        self.txt_nombre.delete(0, tk.END)
        self.txt_usuario.delete(0, tk.END)
        self.txt_clave.delete(0, tk.END)
        self.cmb_rol.current(2)

        # Desseleccionar item en Treeview
        for item in self.tree.selection():
            self.tree.selection_remove(item)

    def actualizar_treeview(self):
        """Limpia y repuebla el Treeview desde el servicio."""
        for row in self.tree.get_children():
            self.tree.delete(row)

        for u in self.servicio.obtener_usuarios():
            self.tree.insert("", tk.END, values=(u.id_usuario, u.nombre, u.usuario, u.rol))