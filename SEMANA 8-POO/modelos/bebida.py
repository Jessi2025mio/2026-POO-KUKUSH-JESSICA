from modelos.producto import Producto

class Bebida(Producto):
    """Clase especializada que representa una bebida, heredando de Producto."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, tamano: str, envase: str) -> None:
        super().__init__(codigo, nombre, categoria, precio)
        self.tamano: str = tamano      # Ej: "500ml", "1 Liter", "Personal"
        self.envase: str = envase      # Ej: "Vidrio", "Plástico", "Lata"

    def mostrar_informacion(self) -> str:
        """Sobrescribe el método base agregando detalles específicos de la bebida."""
        info_base: str = super().mostrar_informacion()
        return f"{info_base} | Tamaño: {self.tamano} | Envase: {self.envase}"