import os
import tkinter as tk
from ui.login_view import LoginView
from ui.main_view import MainView


def main():
    # Obtener la ruta base del proyecto
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Iniciar MainView oculta hasta que el login sea exitoso
    app = MainView(base_dir)
    app.withdraw()

    def abrir_main_view():
        app.deiconify()

    # Mostrar la vista de Login
    login = LoginView(app, on_login_success=abrir_main_view)

    app.mainloop()


if __name__ == "__main__":
    main()