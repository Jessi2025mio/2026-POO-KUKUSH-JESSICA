# Módulo encargado de gestionar las operaciones y lógica principal del restaurante

class Restaurante:
    def __init__(self, nombre_establecimiento):
        """
        Constructor que inicializa el restaurante con su lista de productos y clientes.
        """
        self.nombre_establecimiento = nombre_establecimiento
        self.lista_productos = []  # Lista vacía para almacenar objetos de tipo Producto
        self.lista_clientes = []   # Lista vacía para almacenar objetos de tipo Cliente

    def registrar_producto(self, producto):
        """
        Método para añadir un nuevo producto al menú del restaurante.
        """
        self.lista_productos.append(producto)
        print(f"✔️ Producto registrado con éxito: {producto.nombre}")

    def registrar_cliente(self, cliente):
        """
        Método para registrar un cliente en una mesa.
        """
        self.lista_clientes.append(cliente)
        print(f"👥 Cliente asignado a mesa: {cliente.nombre} en Mesa {cliente.mesa}")

    def mostrar_menu(self):
        """
        Método que recorre la lista de productos y los muestra organizados en consola.
        """
        print(f"\n--- MENÚ DE {self.nombre_establecimiento.upper()} ---")
        if not self.lista_productos:
            print("El menú se encuentra vacío en este momento.")
        for prod in self.lista_productos:
            print(prod.mostrar_detalles())

    def mostrar_clientes_activos(self):
        """
        Método que recorre y muestra los clientes que están consumiendo actualmente.
        """
        print("\n--- CLIENTES ACTUALES EN EL LOCAL ---")
        if not self.lista_clientes:
            print("No hay clientes registrados en este momento.")
        for cli in self.lista_clientes:
            print(cli)