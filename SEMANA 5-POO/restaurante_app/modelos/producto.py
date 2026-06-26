# modelos/producto.py

class Producto:
    """Clase que representa un producto del restaurante (plato o bebida)"""

    # Aplicación de tipos de datos básicos y anotaciones de tipo
    def __init__(self, nombre: str, precio: float, cantidad_stock: int, disponible: bool):
        self.nombre: str = nombre  # Tipo str para texto
        self.precio: float = precio  # Tipo float para decimales
        self.cantidad_stock: int = cantidad_stock  # Tipo int para enteros
        self.disponible: bool = disponible  # Tipo bool para estados lógicos

    # Método especial __str__ para representar el objeto como texto
    def __str__(self) -> str:
        estado = "Disponible" if self.disponible else "Agotado"
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.cantidad_stock} unidades ({estado})"