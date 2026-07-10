# modelos/producto.py

class Producto:
    def __init__(self, nombre: str, categoria: str, precio: float, disponible: bool = True):
        # Se invocan directamente los setters para aplicar las validaciones desde la construcción
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    # Encapsulamiento del atributo 'nombre'
    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        self._nombre = valor.strip()

    # Encapsulamiento del atributo 'categoria'
    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("La categoría del producto no puede estar vacía.")
        self._categoria = valor.strip()

    # Encapsulamiento del atributo 'precio'
    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float):
        if valor <= 0:
            raise ValueError("El precio del producto debe ser mayor que cero.")
        self._precio = valor

    # Encapsulamiento del atributo 'disponible'
    @property
    def disponible(self) -> bool:
        return self._disponible

    @disponible.setter
    def disponible(self, valor: bool):
        self._disponible = valor

    # Método para dar formato legible a los datos del producto
    def mostrar_informacion(self) -> str:
        estado = "Disponible" if self._disponible else "Agotado"
        return f"Producto: {self._nombre} | Categoría: {self._categoria} | Precio: ${self._precio:.2f} | Estado: {estado}"