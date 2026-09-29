import tkinter as tk
from tkinter import ttk, messagebox
from servicios.restaurante_servicio import RestauranteServicio

class LoginView(tk.Tk):
    """Vista de autenticación al sistema."""

    def __init__(self, servicio: RestauranteServicio, on_login_success):
        super().__init__()
        self.servicio = servicio
        self.on_login_success = on_login_success

        self.title("Restaurante App - Inicio de Sesión")
        self.geometry("380x280")
        self.resizable(False, False)

        self._crear_interfaz()

    def _crear_interfaz(self):
        frame = ttk.Frame(self, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Iniciar Sesión", font=("Helvetica", 14, "bold")).pack(pady=10)

        ttk.Label(frame, text="Usuario:").pack(anchor=tk.W)
        self.txt_usuario = ttk.Entry(frame, width=30)
        self.txt_usuario.pack(pady=5)
        self.txt_usuario.focus()

        ttk.Label(frame, text="Contraseña:").pack(anchor=tk.W)
        self.txt_clave = ttk.Entry(frame, show="*", width=30)
        self.txt_clave.pack(pady=5)

        btn_ingresar = ttk.Button(frame, text="Ingresar", command=self._autenticar)
        btn_ingresar.pack(pady=15, fill=tk.X)

        self.bind("<Return>", lambda e: self._autenticar())

    def _autenticar(self):
        user = self.txt_usuario.get().strip()
        clave = self.txt_clave.get().strip()

        u = self.servicio.autenticar(user, clave)
        if u:
            self.destroy()
            self.on_login_success()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas. Intente nuevamente.")