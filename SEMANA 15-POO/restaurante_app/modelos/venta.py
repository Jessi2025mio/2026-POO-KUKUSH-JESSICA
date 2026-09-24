from datetime import datetime

class Venta:
    def __init__(self, id_venta: int, id_usuario: int, usuario_nombre: str, id_producto: int, producto_nombre: str, total: float, fecha: str = None):
        self.id_venta = id_venta
        self.id_usuario = id_usuario
        self.usuario_nombre = usuario_nombre
        self.id_producto = id_producto
        self.producto_nombre = producto_nombre
        self.total = total
        self.fecha = fecha if fecha else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id_venta": self.id_venta,
            "id_usuario": self.id_usuario,
            "usuario_nombre": self.usuario_nombre,
            "id_producto": self.id_producto,
            "producto_nombre": self.producto_nombre,
            "total": self.total,
            "fecha": self.fecha
        }

    @staticmethod
    def from_dict(data: dict):
        return Venta(
            id_venta=data["id_venta"],
            id_usuario=data["id_usuario"],
            usuario_nombre=data["usuario_nombre"],
            id_producto=data["id_producto"],
            producto_nombre=data["producto_nombre"],
            total=float(data["total"]),
            fecha=data["fecha"]
        )