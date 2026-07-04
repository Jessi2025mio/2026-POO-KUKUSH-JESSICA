# modelos/platillo.py
from modelos.producto import Producto


class Platillo(Producto):
    """Clase hija para los platos de comida, hereda de Producto"""

    def __init__(self, nombre: str, precio: float, calorias: int, disponible: bool = True):
        # Enviamos los datos comunes a la clase padre usando super()
        super().__init__(nombre, precio, disponible)
        # Atributo específico de esta clase hija
        self.calorias = calorias

    def mostrar_informacion(self) -> str:
        # Sobrescribimos el método para aplicar polimorfismo
        info_padre = super().mostrar_informacion()
        return f"{info_padre} | Calorías: {self.calorias} kcal"