from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class RestauranteService:
    def __init__(self):
        # 1. Colecciones Principales (Listas para persistencia y recorrido general)
        self.productos = []
        self.usuarios = []
        self.ventas = []

        # 2. Estructuras Auxiliares / Índices en Memoria para Rendimiento
        self._index_productos_codigo = {}  # dict -> O(1) Búsqueda por código
        self._index_usuarios_id = {}  # dict -> O(1) Búsqueda por cédula/ID
        self._index_ventas_usuario = {}  # dict -> O(1) Agrupación: ID Usuario -> lista de ventas
        self._codigos_productos_set = set()  # set -> O(1) Validaciones rápidas de pertenencia/unicidad

        # Cargar datos e inicializar índices
        self.cargar_datos()

    def _reconstruir_indices(self):
        """Reconstruye todos los índices auxiliares en memoria."""
        self._index_productos_codigo = {p.codigo: p for p in self.productos}
        self._index_usuarios_id = {u.identificacion: u for u in self.usuarios}
        self._codigos_productos_set = {p.codigo for p in self.productos}

        # Reconstruir índice de ventas agrupadas por usuario
        self._index_ventas_usuario = {}
        for v in self.ventas:
            if v.identificacion_usuario not in self._index_ventas_usuario:
                self._index_ventas_usuario[v.identificacion_usuario] = []
            self._index_ventas_usuario[v.identificacion_usuario].append(v)

    # --- REGISTROS Y SINCRONIZACIÓN ---

    def registrar_producto(self, producto: Producto) -> bool:
        if producto.codigo in self._codigos_productos_set:  # Validación O(1) con set
            return False

        self.productos.append(producto)
        # Sincronización de índices
        self._index_productos_codigo[producto.codigo] = producto
        self._codigos_productos_set.add(producto.codigo)
        self.guardar_datos()
        return True

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if usuario.identificacion in self._index_usuarios_id:  # Validación O(1) con dict
            return False

        self.usuarios.append(usuario)
        # Sincronización de índice
        self._index_usuarios_id[usuario.identificacion] = usuario
        self.guardar_datos()
        return True

    def registrar_venta(self, id_venta: str, id_usuario: str, cod_producto: str, cantidad: int) -> bool:
        usuario = self.buscar_usuario_por_id(id_usuario)
        producto = self.buscar_producto_por_codigo(cod_producto)

        if not usuario or not producto or producto.stock < cantidad:
            return False

        # Descontar stock
        producto.stock -= cantidad
        total = producto.precio * cantidad

        nueva_venta = Venta(id_venta, id_usuario, cod_producto, cantidad, total)
        self.ventas.append(nueva_venta)

        # Sincronizar índice de ventas por usuario
        if id_usuario not in self._index_ventas_usuario:
            self._index_ventas_usuario[id_usuario] = []
        self._index_ventas_usuario[id_usuario].append(nueva_venta)

        self.guardar_datos()
        return True

    # --- BÚSQUEDAS OPTIMIZADAS ---

    def buscar_producto_por_codigo(self, codigo: str) -> Producto:
        # Búsqueda en O(1) mediante dict en lugar de O(n) con for
        return self._index_productos_codigo.get(codigo)

    def buscar_usuario_por_id(self, identificacion: str) -> Usuario:
        # Búsqueda en O(1) mediante dict
        return self._index_usuarios_id.get(identificacion)

    def consultar_ventas_por_usuario(self, identificacion: str) -> list:
        # Consulta O(1) del índice agrupado en lugar de filtrar toda la lista
        return self._index_ventas_usuario.get(identificacion, [])

    # --- PERSISTENCIA Y CARGA ---

    def guardar_datos(self):
        ArchivoServicio.guardar_json("datos/productos.json", [p.to_dict() for p in self.productos])
        ArchivoServicio.guardar_json("datos/usuarios.json", [u.to_dict() for u in self.usuarios])
        ArchivoServicio.guardar_json("datos/ventas.json", [v.to_dict() for v in self.ventas])

    def cargar_datos(self):
        raw_p = ArchivoServicio.cargar_json("datos/productos.json")
        self.productos = [Producto.from_dict(d) for d in raw_p]

        raw_u = ArchivoServicio.cargar_json("datos/usuarios.json")
        self.usuarios = [Usuario.from_dict(d) for d in raw_u]

        raw_v = ArchivoServicio.cargar_json("datos/ventas.json")
        self.ventas = [Venta.from_dict(d) for d in raw_v]

        # Reconstruir los índices al cargar datos desde JSON
        self._reconstruir_indices()