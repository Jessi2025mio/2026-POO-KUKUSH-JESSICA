class Usuario:
    def __init__(self, identificacion: str, nombre: str, correo: str):
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    def to_dict(self):
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo
        }

    @staticmethod
    def from_dict(data):
        return Usuario(data["identificacion"], data["nombre"], data["correo"])