# modelos/cliente.py
from dataclasses import dataclass

@dataclass
class Cliente:
    nombre: str
    correo: str
    id_cliente: str

    # Método para dar formato legible a los datos del cliente
    def mostrar_informacion(self) -> str:
        return f"ID Cliente: {self.id_cliente} | Nombre: {self.nombre} | Correo: {self.correo}"