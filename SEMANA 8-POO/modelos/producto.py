class Producto:
    """Clase base que representa un producto general del restaurante."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.categoria: str = categoria
        self.precio: float = precio

    def mostrar_informacion(self) -> str:
        """Devuelve la representación en texto de la información general del producto."""
        return f"[{self.codigo}] Producto: {self.nombre} | Categoría: {self.categoria} | Precio: ${self.precio:.2f}"