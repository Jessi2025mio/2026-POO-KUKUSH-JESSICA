# modelos/bebida.py
from modelos.producto import Producto


class Bebida(Producto):
    """Clase hija para las bebidas, hereda de Producto"""

    def __init__(self, nombre: str, precio: float, tamano_ml: int, disponible: bool = True):
        # Enviamos los datos comunes a la clase padre usando super()
        super().__init__(nombre, precio, disponible)
        # Atributo específico de esta clase hija
        self.tamano_ml = tamano_ml

    def mostrar_informacion(self) -> str:
        # Sobrescribimos el método para aplicar polimorfismo
        info_padre = super().mostrar_informacion()
        return f"{info_padre} | Tamaño: {self.tamano_ml} ml"

