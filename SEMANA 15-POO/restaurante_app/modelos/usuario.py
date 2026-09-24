class Usuario:
    def __init__(self, id_user: int, nombre: str, rol: str):
        self.id = id_user
        self.nombre = nombre
        self.rol = rol

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "rol": self.rol
        }

    @staticmethod
    def from_dict(data: dict):
        return Usuario(data["id"], data["nombre"], data["rol"])