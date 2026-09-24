class Producto:
    def __init__(self, id_prod: int, nombre: str, precio: float, categoria: str):
        self.id = id_prod
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria
        }

    @staticmethod
    def from_dict(data: dict):
        return Producto(data["id"], data["nombre"], float(data["precio"]), data["categoria"])