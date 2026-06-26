# servicios/restaurante.py

# Importación correcta de las clases desde el módulo de modelos
from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """Clase de servicio que gestiona las listas de productos y clientes"""

    def __init__(self, nombre_establecimiento: str):
        self.nombre_establecimiento: str = nombre_establecimiento
        # Uso de listas como tipo de dato compuesto para almacenar múltiples objetos
        self.lista_productos: list[Producto] = []
        self.lista_clientes: list[Cliente] = []

    # Métodos para agregar y gestionar la información
    def registrar_producto(self, producto: Producto) -> None:
        """Agrega un objeto Producto a la lista compuesta"""
        self.lista_productos.append(producto)
        print(f"[Sistema]: Producto '{producto.nombre}' registrado exitosamente.")

    def registrar_cliente(self, cliente: Cliente) -> None:
        """Agrega un objeto Cliente a la lista compuesta"""
        self.lista_clientes.append(cliente)
        print(f"[Sistema]: Cliente '{cliente.nombre_completo}' registrado exitosamente.")

    def mostrar_informacion_general(self) -> None:
        """Muestra de forma organizada toda la información registrada en el restaurante"""
        print(f"\n==============================================")
        print(f" REPORTES DEL RESTAURANTE: {self.nombre_establecimiento.upper()}")
        print(f"==============================================")

        print("\n--- LISTADO DE PRODUCTOS EN MENÚ ---")
        if not self.lista_productos:
            print("No hay productos registrados.")
        else:
            for prod in self.lista_productos:
                print(prod)  # Llama automáticamente al método __str__() de Producto

        print("\n--- LISTADO DE CLIENTES REGISTRADOS ---")
        if not self.lista_clientes:
            print("No hay clientes registrados.")
        else:
            for cli in self.lista_clientes:
                print(cli)  # Llama automáticamente al método __str__() de Cliente
        print(f"==============================================\n")

    def mostrar_totales(self) -> None:
        """Muestra el total de productos y clientes registrados (Método de gestión adicional)."""
        print("--- RESUMEN DE CONTROL ---")
        print(f"Total de productos registrados: {len(self.lista_productos)}")
        print(f"Total de clientes registrados: {len(self.lista_clientes)}")
        print(f"==============================================\n")