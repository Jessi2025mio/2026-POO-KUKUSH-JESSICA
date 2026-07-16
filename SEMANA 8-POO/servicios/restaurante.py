from typing import List, Optional
from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    """Clase de servicio encargada de administrar las colecciones y operaciones del sistema."""

    def __init__(self) -> None:
        # Una única lista para productos (aplica polimorfismo para Producto y Bebida)
        self._productos: List[Producto] = []
        self._clientes: List[Cliente] = []

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        """Busca un producto en la lista por su código."""
        for prod in self._productos:
            if prod.codigo == codigo:
                return prod
        return None

    def registrar_producto(self, producto: Producto) -> bool:
        """Registra un producto o bebida validando que el código no se repita."""
        if self.buscar_producto(producto.codigo) is not None:
            print(f"Error: Ya existe un producto registrado con el código '{producto.codigo}'.")
            return False
        self._productos.append(producto)
        print("¡Producto/Bebida registrado(a) con éxito!")
        return True

    def listar_productos(self) -> None:
        """Lista todos los productos y bebidas aprovechando el polimorfismo."""
        if not self._productos:
            print("No hay productos o bebidas registrados en el sistema.")
            return
        print("\n--- LISTA DE PRODUCTOS Y BEBIDAS ---")
        for prod in self._productos:
            # Polimorfismo en acción: ejecuta el mostrar_informacion() correspondiente a cada objeto
            print(prod.mostrar_informacion())

    def buscar_cliente(self, identificacion: str) -> Optional[Cliente]:
        """Busca un cliente por su número de identificación."""
        for cli in self._clientes:
            if cli.identificacion == identificacion:
                return cli
        return None

    def registrar_cliente(self, cliente: Cliente) -> bool:
        """Registra un cliente validando que la identificación no se repita."""
        if self.buscar_cliente(cliente.identificacion) is not None:
            print(f"Error: Ya existe un cliente registrado con la identificación '{cliente.identificacion}'.")
            return False
        self._clientes.append(cliente)
        print("¡Cliente registrado con éxito!")
        return True

    def listar_clientes(self) -> None:
        """Lista todos los clientes registrados."""
        if not self._clientes:
            print("No hay clientes registrados en el sistema.")
            return
        print("\n--- LISTA DE CLIENTES ---")
        for cli in self._clientes:
            print(cli.mostrar_informacion())