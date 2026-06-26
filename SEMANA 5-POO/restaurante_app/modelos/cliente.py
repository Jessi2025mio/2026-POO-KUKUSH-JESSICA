# modelos/cliente.py

class Cliente:
    """Clase que representa a un cliente registrado en el restaurante"""

    # Aplicación de tipos de datos básicos y anotaciones de tipo
    def __init__(self, cedula: str, nombre_completo: str, edad: int, cliente_frecuente: bool):
        self.cedula: str = cedula  # Tipo str
        self.nombre_completo: str = nombre_completo  # Tipo str
        self.edad: int = edad  # Tipo int
        self.cliente_frecuente: bool = cliente_frecuente  # Tipo bool

    # Método especial __str__ para representar el objeto como texto
    def __str__(self) -> str:
        tipo_cliente = "Frecuente" if self.cliente_frecuente else "Regular"
        return f"Cliente: {self.nombre_completo} | Cédula: {self.cedula} | Edad: {self.edad} años | Tipo: {tipo_cliente}"