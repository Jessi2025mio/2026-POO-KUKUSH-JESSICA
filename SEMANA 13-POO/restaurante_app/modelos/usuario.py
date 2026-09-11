class Usuario:
    def __init__(self, username: str, password: str, nombre: str, rol: str):
        self.username = username
        self.password = password
        self.nombre = nombre
        self.rol = rol

    @classmethod
    def from_dict(cls, data: dict):  # <-- REVISA QUE DIGA "def" AQUÍ
        return cls(
            username=data.get("username", ""),
            password=data.get("password", ""),
            nombre=data.get("nombre", ""),
            rol=data.get("rol", "")
        )