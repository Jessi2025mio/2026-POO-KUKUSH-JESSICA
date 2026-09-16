from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

def iniciar_aplicacion():
    # Instancia del servicio general
    servicio = RestauranteServicio()

    def abrir_main_view(usuario_autenticado):
        app_principal = MainView(servicio, usuario_autenticado)
        app_principal.mainloop()

    # Iniciar con la vista de Login
    login_app = LoginView(servicio, on_login_success=abrir_main_view)
    login_app.mainloop()

if __name__ == "__main__":
    iniciar_aplicacion()