class Venta:
    def __init__(self, id_venta: str, identificacion_usuario: str, codigo_producto: str, cantidad: int, total: float):
        self.id_venta = id_venta
        self.identificacion_usuario = identificacion_usuario
        self.codigo_producto = codigo_producto
        self.cantidad = cantidad
        self.total = total

    def to_dict(self):
        return {
            "id_venta": self.id_venta,
            "identificacion_usuario": self.identificacion_usuario,
            "codigo_producto": self.codigo_producto,
            "cantidad": self.cantidad,
            "total": self.total
        }

    @staticmethod
    def from_dict(data):
        return Venta(
            data["id_venta"],
            data["identificacion_usuario"],
            data["codigo_producto"],
            int(data["cantidad"]),
            float(data["total"])
        )