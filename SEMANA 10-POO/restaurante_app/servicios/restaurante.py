from typing import List, Optional
from modelos.producto import Producto


class Restaurante:
    def __init__(self) -> None:
        self.productos: List[Producto] = []

    def establecer_productos(self, productos: List[Producto]) -> None:
        """Asigna la lista inicial recuperada del servicio de archivos."""
        self.productos = productos

    def obtener_productos(self) -> List[Producto]:
        return self.productos

    def registrar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto_por_id(producto.id_producto) is not None:
            raise ValueError(f"Ya existe un producto registrado con el ID {producto.id_producto}.")
        self.productos.append(producto)
        return True

    def buscar_producto_por_id(self, id_producto: int) -> Optional[Producto]:
        for producto in self.productos:
            if producto.id_producto == id_producto:
                return producto
        return None

    def actualizar_producto(self, id_producto: int, nuevo_nombre: str, nuevo_precio: float,
                            nueva_categoria: str) -> bool:
        producto = self.buscar_producto_por_id(id_producto)
        if producto is None:
            return False

        # Las validaciones se disparan mediante el setter/constructor si falla alguno
        producto_actualizado = Producto(id_producto, nuevo_nombre, nuevo_precio, nueva_categoria)
        producto.nombre = producto_actualizado.nombre
        producto.precio = producto_actualizado.precio
        producto.categoria = producto_actualizado.categoria
        return True

    def eliminar_producto(self, id_producto: int) -> bool:
        producto = self.buscar_producto_por_id(id_producto)
        if producto:
            self.productos.remove(producto)
            return True
        return False