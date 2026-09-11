import tkinter as tk
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class RestauranteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurante App - Gestión")
        self.root.geometry("600x450")
        self.root.resizable(False, False)

        self.servicio = RestauranteServicio()

        self.login_view = None
        self.main_view = None

        self.mostrar_login()

    def mostrar_login(self):
        if self.main_view:
            self.main_view.destroy()
            self.main_view = None

        self.login_view = LoginView(
            parent=self.root,
            servicio=self.servicio,
            on_login_success=self.mostrar_main
        )
        self.login_view.pack(fill="both", expand=True)

    def mostrar_main(self, usuario):
        if self.login_view:
            self.login_view.destroy()
            self.login_view = None

        self.main_view = MainView(
            parent=self.root,
            servicio=self.servicio,
            usuario_actual=usuario,
            on_logout=self.mostrar_login
        )
        self.main_view.pack(fill="both", expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = RestauranteApp(root)
    root.mainloop()