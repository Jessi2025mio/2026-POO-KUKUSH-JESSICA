from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class Restaurante:
    def __init__(self):
        self._productos: list[Producto] = ArchivoServicio.cargar_productos()
        self._usuarios: list[Usuario] = ArchivoServicio.cargar_usuarios()
        self._ventas: list[Venta] = ArchivoServicio.cargar_ventas()

    # Búsquedas
    def buscar_producto(self, codigo: str) -> Producto | None:
        for p in self._productos:
            if p.codigo == codigo:
                return p
        return None

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        for u in self._usuarios:
            if u.identificacion == identificacion:
                return u
        return None

    # Registros
    def registrar_producto(self, codigo: str, nombre: str, precio: float, stock: int) -> bool:
        if self.buscar_producto(codigo) is not None:
            return False
        try:
            nuevo_p = Producto(codigo, nombre, precio, stock)
            self._productos.append(nuevo_p)
            ArchivoServicio.guardar_datos(ArchivoServicio.RUTA_PRODUCTOS, self._productos)
            return True
        except ValueError:
            return False

    def registrar_usuario(self, identificacion: str, nombre: str) -> bool:
        if self.buscar_usuario(identificacion) is not None:
            return False
        nuevo_u = Usuario(identificacion, nombre)
        self._usuarios.append(nuevo_u)
        ArchivoServicio.guardar_datos(ArchivoServicio.RUTA_USUARIOS, self._usuarios)
        return True

    # Operación de Venta
    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int) -> tuple[bool, str]:
        usuario = self.buscar_usuario(identificacion_usuario)
        if usuario is None:
            return False, "El usuario especificado no existe."

        producto = self.buscar_producto(codigo_producto)
        if producto is None:
            return False, "El producto especificado no existe."

        if cantidad <= 0:
            return False, "La cantidad ingresada debe ser mayor a cero."

        if producto.stock < cantidad:
            return False, f"Stock insuficiente. Stock actual: {producto.stock}"

        try:
            producto.vender(cantidad)
            nueva_venta = Venta(usuario.identificacion, producto.codigo, cantidad)
            self._ventas.append(nueva_venta)

            # Persistencia de ambas colecciones afectadas
            ArchivoServicio.guardar_datos(ArchivoServicio.RUTA_PRODUCTOS, self._productos)
            ArchivoServicio.guardar_datos(ArchivoServicio.RUTA_VENTAS, self._ventas)
            return True, "Venta realizada y registrada con éxito."
        except ValueError as e:
            return False, str(e)

    # Consulta de ventas
    def obtener_ventas_usuario(self, identificacion_usuario: str) -> list[dict]:
        ventas_usuario = []
        for venta in self._ventas:
            if venta.usuario_id == identificacion_usuario:
                producto = self.buscar_producto(venta.producto_codigo)
                nombre_prod = producto.nombre if producto else "Producto no disponible"
                ventas_usuario.append({
                    "codigo_producto": venta.producto_codigo,
                    "nombre_producto": nombre_prod,
                    "cantidad": venta.cantidad
                })
        return ventas_usuario

    # Métodos aux para listar
    def listar_productos(self) -> list[Producto]:
        return self._productos

    def listar_usuarios(self) -> list[Usuario]:
        return self._usuarios