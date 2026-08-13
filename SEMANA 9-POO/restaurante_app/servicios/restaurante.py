from typing import List, Optional, Set
from modelos.producto import Producto
from modelos.usuario import Usuario

class Restaurante:
    """
    Servicio encargado de administrar las colecciones del sistema
    y la lógica de negocio para productos y usuarios.
    """

    def __init__(self) -> None:
        # LIST: Administran las colecciones dinámicas de productos y usuarios
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []

    # --- OPERACIONES DE PRODUCTOS (LIST) ---

    def registrar_producto(self, producto: Producto) -> bool:
        """Registra un producto evitando códigos duplicados."""
        if self.buscar_producto_por_codigo(producto.codigo) is not None:
            return False  # El código ya existe
        self._productos.append(producto)
        return True

    def buscar_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
        """Busca un producto por su código."""
        for prod in self._productos:
            if prod.codigo.lower() == codigo.lower():
                return prod
        return None

    def actualizar_producto(self, codigo: str, nuevo_nombre: str, nueva_categoria: str, nuevo_precio: float) -> bool:
        """Actualiza los datos de un producto existente."""
        producto = self.buscar_producto_por_codigo(codigo)
        if producto:
            producto.nombre = nuevo_nombre
            producto.categoria = nueva_categoria.strip().capitalize()
            producto.precio = nuevo_precio
            return True
        return False

    def eliminar_producto(self, codigo: str) -> bool:
        """Elimina un producto por su código."""
        producto = self.buscar_producto_por_codigo(codigo)
        if producto:
            self._productos.remove(producto)
            return True
        return False

    def listar_productos(self) -> List[Producto]:
        """Devuelve la lista completa de productos."""
        return self._productos

    # --- OPERACIONES DE USUARIOS (LIST) ---

    def registrar_usuario(self, usuario: Usuario) -> bool:
        """Registra un usuario evitando identificaciones duplicadas."""
        if self.buscar_usuario_por_id(usuario.identificacion) is not None:
            return False  # La identificación ya existe
        self._usuarios.append(usuario)
        return True

    def buscar_usuario_por_id(self, identificacion: str) -> Optional[Usuario]:
        """Busca un usuario por su identificación."""
        for usr in self._usuarios:
            if usr.identificacion == identificacion:
                return usr
        return None

    def listar_usuarios(self) -> List[Usuario]:
        """Devuelve la lista completa de usuarios."""
        return self._usuarios

    # --- USO DE CONJUNTO (SET) ---

    def obtener_categorias_unicas(self) -> Set[str]:
        """
        SET: Utiliza un conjunto para extraer y retornar las categorías
        únicas de productos sin elementos duplicados.
        """
        categorias: Set[str] = {prod.categoria for prod in self._productos}
        return categorias