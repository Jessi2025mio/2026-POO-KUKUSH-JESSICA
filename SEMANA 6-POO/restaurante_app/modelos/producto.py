# modelos/producto.py

class Producto:
    """Clase padre que define los datos comunes de cualquier producto"""

    def __init__(self, nombre: str, precio: float, disponible: bool = True):
        self.nombre = nombre
        # Atributo privado con doble guion bajo para aplicar encapsulamiento
        self.__precio = 0.0
        # Usamos el método de modificación para validar el precio desde el inicio
        self.cambiar_precio(precio)
        self.disponible = disponible

    # Método para leer el precio (Getter)
    def obtener_precio(self) -> float:
        return self.__precio

    # Método para modificar el precio (Setter) con validación
    def cambiar_precio(self, nuevo_precio: float):
        # Validación para que el precio no sea negativo ni cero
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print(f"⚠️ Error: El precio de '{self.nombre}' debe ser mayor a cero. No se aplicó el cambio.")

    def mostrar_informacion(self) -> str:
        estado = "Disponible" if self.disponible else "Agotado"
        return f"Producto: {self.nombre} | Precio: ${self.obtener_precio():.2f} | Estado: {estado}"