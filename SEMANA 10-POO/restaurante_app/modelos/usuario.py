class Usuario:
    def __init__(self, id_usuario: int, nombre: str, rol: str) -> None:
        if id_usuario <= 0:
            raise ValueError("El ID del usuario debe ser mayor a 0.")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre de usuario no puede estar vacío.")

        self.id_usuario: int = id_usuario
        self.nombre: str = nombre.strip()
        self.rol: str = rol.strip()

    def __str__(self) -> str:
        return f"ID: {self.id_usuario} | Usuario: {self.nombre} | Rol: {self.rol}"