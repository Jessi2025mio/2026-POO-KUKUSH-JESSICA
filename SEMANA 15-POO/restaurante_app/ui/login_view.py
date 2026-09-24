import tkinter as tk
from tkinter import ttk, messagebox

class LoginView(tk.Toplevel):
    def __init__(self, parent, on_login_success):
        super().__init__(parent)
        self.title("Restaurante App - Login")
        self.geometry("350x250")
        self.resizable(False, False)
        self.on_login_success = on_login_success

        ttk.Label(self, text="Bienvenido a Restaurante App", font=("Arial", 12, "bold")).pack(pady=20)

        frame = ttk.Frame(self)
        frame.pack(pady=10)

        ttk.Label(frame, text="Usuario:").grid(row=0, column=0, padx=5, pady=5)
        self.txt_user = ttk.Entry(frame)
        self.txt_user.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Clave:").grid(row=1, column=0, padx=5, pady=5)
        self.txt_pass = ttk.Entry(frame, show="*")
        self.txt_pass.grid(row=1, column=1, padx=5, pady=5)

        # Evento command= para el botón de inicio de sesión
        btn_login = ttk.Button(self, text="Ingresar", command=self.on_login_click)
        btn_login.pack(pady=15)

    def on_login_click(self):
        usuario = self.txt_user.get()
        clave = self.txt_pass.get()

        if usuario and clave:
            self.destroy()
            self.on_login_success()
        else:
            messagebox.showerror("Error", "Ingrese usuario y clave para continuar.")