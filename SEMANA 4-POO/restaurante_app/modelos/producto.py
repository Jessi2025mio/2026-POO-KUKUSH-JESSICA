# Módulo que representa un producto del restaurante (Plato, bebida, etc.)

class Producto:
    def __init__(self, nombre, precio, categoria):
        """
        Constructor para inicializar los atributos de un producto.
        """
        self.nombre = nombre        # Atributo: nombre del plato o bebida
        self.precio = precio        # Atributo: costo del producto
        self.categoria = categoria  # Atributo: entrada, plato fuerte, bebida, etc.

    def mostrar_detalles(self):
        """
        Método que retorna la información detallada del producto.
        """
        return f"[{self.categoria.upper()}] {self.nombre} - ${self.precio:.2f}"

    def __str__(self):
        """
        Método especial para representar el objeto como cadena de texto.
        """
        return f"{self.nombre} (${self.precio:.2f})"