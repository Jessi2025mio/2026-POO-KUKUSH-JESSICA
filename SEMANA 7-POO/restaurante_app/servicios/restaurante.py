# servicios/restaurante.py
from modelos.producto import Producto
from modelos.cliente import Cliente
from typing import List, Optional

class Restaurante:
    def __init__(self):
        # Listas en memoria para almacenar dinámicamente los objetos
        self._productos: List[Producto] = []
        self._clientes: List[Cliente] = []

    # --- Métodos de Gestión para Productos ---
    def registrar_producto(self, producto: Producto) -> None:
        self._productos.append(producto)

    def listar_productos(self) -> List[Producto]:
        return self._productos

    def buscar_producto(self, nombre: str) -> Optional[Producto]:
        for prod in self._productos:
            if prod.nombre.lower() == nombre.lower().strip():
                return prod
        return None

    # --- Métodos de Gestión para Clientes ---
    def registrar_cliente(self, cliente: Cliente) -> None:
        self._clientes.append(cliente)

    def listar_clientes(self) -> List[Cliente]:
        return self._clientes

    def buscar_cliente(self, id_cliente: str) -> Optional[Cliente]:
        for cli in self._clientes:
            if cli.id_cliente.strip() == id_cliente.strip():
                return cli
        return None