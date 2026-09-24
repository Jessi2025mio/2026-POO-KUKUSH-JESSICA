import os
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self, base_dir: str):
        self.ruta_productos = os.path.join(base_dir, "datos", "productos.json")
        self.ruta_usuarios = os.path.join(base_dir, "datos", "usuarios.json")
        self.ruta_ventas = os.path.join(base_dir, "datos", "ventas.json")

    def obtener_usuarios(self) -> list[Usuario]:
        datos = ArchivoServicio.cargar_json(self.ruta_usuarios)
        return [Usuario.from_dict(d) for d in datos]

    def obtener_productos(self) -> list[Producto]:
        datos = ArchivoServicio.cargar_json(self.ruta_productos)
        return [Producto.from_dict(d) for d in datos]

    def obtener_ventas(self) -> list[Venta]:
        datos = ArchivoServicio.cargar_json(self.ruta_ventas)
        return [Venta.from_dict(d) for d in datos]

    def registrar_venta(self, id_usuario: int, id_producto: int) -> tuple[bool, str]:
        usuarios = self.obtener_usuarios()
        productos = self.obtener_productos()

        usuario = next((u for u in usuarios if u.id == id_usuario), None)
        producto = next((p for p in productos if p.id == id_producto), None)

        if not usuario:
            return False, "El usuario seleccionado no existe."
        if not producto:
            return False, "El producto seleccionado no existe."

        ventas = self.obtener_ventas()
        nuevo_id = len(ventas) + 1

        nueva_venta = Venta(
            id_venta=nuevo_id,
            id_usuario=usuario.id,
            usuario_nombre=usuario.nombre,
            id_producto=producto.id,
            producto_nombre=producto.nombre,
            total=producto.precio
        )

        ventas.append(nueva_venta)

        # Persistir en JSON
        datos_json = [v.to_dict() for v in ventas]
        ArchivoServicio.guardar_json(self.ruta_ventas, datos_json)

        return True, f"Venta #{nuevo_id} registrada con éxito."