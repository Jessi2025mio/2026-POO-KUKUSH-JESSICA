# servicios/restaurante.py

class Restaurante:
    """Clase encargada de administrar la lista de productos del menú"""

    def __init__(self, nombre_establecimiento: str):
        self.nombre_establecimiento = nombre_establecimiento
        # Lista para almacenar los objetos creados
        self.lista_productos = []

    def agregar_producto(self, producto):
        self.lista_productos.append(producto)
        print(f"✅ Producto registrado: {producto.nombre}")

    def mostrar_catalogo(self):
        print(f"\n--- MENÚ DEL RESTAURANTE: {self.nombre_establecimiento.upper()} ---")
        if not self.lista_productos:
            print("El menú no tiene productos registrados.")
            return

        # Aquí se demuestra el polimorfismo: el ciclo ejecuta el método mostrar_informacion
        # y cada objeto responde de forma diferente según su tipo (Platillo o Bebida).
        for producto in self.lista_productos:
            print(producto.mostrar_informacion())
        print("-" * 70)