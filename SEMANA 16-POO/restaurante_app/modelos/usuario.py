class Usuario:
    """Modelo que representa un usuario dentro del sistema del restaurante."""

    ROLES_PERMITIDOS = ["Administrador", "Empleado", "Cliente"]

    def __init__(self, id_usuario: str, nombre: str, usuario: str, clave: str, rol: str = "Cliente"):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.usuario = usuario
        self.clave = clave
        self.rol = rol if rol in self.ROLES_PERMITIDOS else "Cliente"

    def to_dict(self) -> dict:
        """Convierte la instancia de Usuario a un diccionario para su persistencia en JSON."""
        return {
            "id": self.id_usuario,
            "nombre": self.nombre,
            "usuario": self.usuario,
            "clave": self.clave,
            "rol": self.rol
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Crea una instancia de Usuario a partir de un diccionario."""
        return cls(
            id_usuario=data.get("id", ""),
            nombre=data.get("nombre", ""),
            usuario=data.get("usuario", ""),
            clave=data.get("clave", ""),
            rol=data.get("rol", "Cliente")
        )