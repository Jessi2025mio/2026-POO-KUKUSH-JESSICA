class Producto:
    def __init__(self, id_producto: int, nombre: str, precio: float, categoria: str) -> None:
        if id_producto <= 0:
            raise ValueError("El ID debe ser un número positivo mayor a 0.")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0.")
        if not categoria or not categoria.strip():
            raise ValueError("La categoría no puede estar vacía.")

        self.id_producto: int = id_producto
        self.nombre: str = nombre.strip()
        self.precio: float = precio
        self.categoria: str = categoria.strip()

    def a_diccionario(self) -> dict:
        """Convierte el objeto Producto a un diccionario para serialización JSON."""
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria
        }

    @staticmethod
    def desde_diccionario(datos: dict) -> 'Producto':
        """Reconstruye un objeto Producto desde un diccionario sacado de JSON."""
        try:
            return Producto(
                id_producto=int(datos["id_producto"]),
                nombre=str(datos["nombre"]),
                precio=float(datos["precio"]),
                categoria=str(datos["categoria"])
            )
        except KeyError as e:
            raise KeyError(f"Falta la clave requerida {e} en el registro del producto.")
        except ValueError as e:
            raise ValueError(f"Datos con formato o tipo incorrecto: {e}")

    def __str__(self) -> str:
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Precio: ${self.precio:.2f} | Categoría: {self.categoria}"