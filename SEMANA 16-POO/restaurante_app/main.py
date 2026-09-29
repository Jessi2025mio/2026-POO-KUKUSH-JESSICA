from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

def iniciar_app():
    # Instanciar el servicio central
    servicio = RestauranteServicio()

    def al_autenticar_exitosamente():
        app = MainView(servicio)
        app.mainloop()

    # Lanzar pantalla de Login
    login = LoginView(servicio, on_login_success=al_autenticar_exitosamente)
    login.mainloop()

if __name__ == "__main__":
    iniciar_app()