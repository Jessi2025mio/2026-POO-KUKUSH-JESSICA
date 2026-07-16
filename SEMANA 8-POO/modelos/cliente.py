class Cliente:
    """Clase que representa a un cliente registrado en el restaurante."""

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo

    def mostrar_informacion(self) -> str:
        """Devuelve la información formateada del cliente."""
        return f"[{self.identificacion}] Cliente: {self.nombre} | Correo: {self.correo}"