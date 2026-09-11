class Producto:
    def __init__(self, id_prod: int, nombre: str, precio: float, categoria: str, stock: int):
        self.id = id_prod
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock

    @classmethod
    def from_dict(cls, data: dict):  # <-- REVISA QUE DIGA "def" AQUÍ
        return cls(
            id_prod=data.get("id", 0),
            nombre=data.get("nombre", ""),
            precio=float(data.get("precio", 0.0)),
            categoria=data.get("categoria", ""),
            stock=int(data.get("stock", 0))
        )