import tkinter as tk
from tkinter import messagebox

class LoginView(tk.Frame):
    def __init__(self, parent, servicio, on_login_success):
        super().__init__(parent)
        self.servicio = servicio
        self.on_login_success = on_login_success

        self.configure(padx=20, pady=20)
        self._crear_widgets()

    def _crear_widgets(self):
        tk.Label(self, text="Sistema Restaurante App", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(self, text="Inicio de Sesión", font=("Arial", 12)).pack(pady=5)

        tk.Label(self, text="Usuario:").pack(anchor="w", pady=(10, 0))
        self.entry_usuario = tk.Entry(self, width=30)
        self.entry_usuario.pack(pady=5)

        tk.Label(self, text="Contraseña:").pack(anchor="w", pady=(5, 0))
        self.entry_password = tk.Entry(self, show="*", width=30)
        self.entry_password.pack(pady=5)

        tk.Button(
            self,
            text="Ingresar",
            command=self._procesar_login,
            bg="#4CAF50",
            fg="white",
            width=15,
            font=("Arial", 10, "bold")
        ).pack(pady=15)

    def _procesar_login(self):
        usuario = self.entry_usuario.get().strip()
        password = self.entry_password.get().strip()

        if not usuario or not password:
            messagebox.showwarning("Atención", "Por favor complete todos los campos.")
            return

        usuario_valido = self.servicio.validar_acceso(usuario, password)

        if usuario_valido:
            self.entry_usuario.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)
            self.on_login_success(usuario_valido)
        else:
            messagebox.showerror("Error de Autenticación", "Usuario o contraseña incorrectos.")