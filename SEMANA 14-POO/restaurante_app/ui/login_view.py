import tkinter as tk
from tkinter import ttk, messagebox

class LoginView(tk.Tk):
    def __init__(self, servicio, on_login_success):
        super().__init__()
        self.servicio = servicio
        self.on_login_success = on_login_success

        self.title("Restaurante App - Acceso al Sistema")
        self.geometry("380x280")
        self.resizable(False, False)

        self._crear_interfaz()

    def _crear_interfaz(self):
        # Contenedor Principal (Frame)
        frame_login = ttk.LabelFrame(self, text=" Inicio de Sesión ", padding=20)
        frame_login.pack(padx=20, pady=20, fill="both", expand=True)

        # Campos
        ttk.Label(frame_login, text="Usuario:").grid(row=0, column=0, sticky="w", pady=5)
        self.txt_usuario = ttk.Entry(frame_login, width=25)
        self.txt_usuario.grid(row=0, column=1, pady=5)

        ttk.Label(frame_login, text="Contraseña:").grid(row=1, column=0, sticky="w", pady=5)
        self.txt_password = ttk.Entry(frame_login, show="*", width=25)
        self.txt_password.grid(row=1, column=1, pady=5)

        # Botón de Ingreso
        btn_ingresar = ttk.Button(
            frame_login,
            text="Ingresar",
            command=self._ejecutar_login
        )
        btn_ingresar.grid(row=2, column=0, columnspan=2, pady=15)

    def _ejecutar_login(self):
        usr = self.txt_usuario.get().strip()
        pwd = self.txt_password.get().strip()

        exito, resultado = self.servicio.autenticar_usuario(usr, pwd)

        if exito:
            messagebox.showinfo("Éxito", f"Bienvenido/a, {resultado.nombre}")
            self.destroy()
            self.on_login_success(resultado)
        else:
            messagebox.showerror("Error", resultado)