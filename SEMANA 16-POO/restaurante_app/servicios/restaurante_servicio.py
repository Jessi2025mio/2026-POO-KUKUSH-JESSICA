import os
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    """Servicio central que gestiona la lógica de negocio y persistencia del restaurante."""

    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.ruta_usuarios = os.path.join(base_dir, "datos", "usuarios.json")
        self.usuarios = []
        self.usuario_actual = None
        self._cargar_datos()

    def _cargar_datos(self):
        datos_raw = ArchivoServicio.cargar_json(self.ruta_usuarios)
        self.usuarios = [Usuario.from_dict(d) for d in datos_raw]

    def _guardar_usuarios(self) -> bool:
        datos_raw = [u.to_dict() for u in self.usuarios]
        return ArchivoServicio.guardar_json(self.ruta_usuarios, datos_raw)

    def autenticar(self, usuario: str, clave: str) -> Usuario:
        """Valida las credenciales de un usuario."""
        for u in self.usuarios:
            if u.usuario == usuario and u.clave == clave:
                self.usuario_actual = u
                return u
        return None

    def obtener_usuarios(self) -> list:
        return self.usuarios

    def buscar_usuario_por_id(self, id_usuario: str) -> Usuario:
        for u in self.usuarios:
            if u.id_usuario == id_usuario:
                return u
        return None

    def registrar_usuario(self, id_usuario: str, nombre: str, usuario: str, clave: str, rol: str) -> tuple[bool, str]:
        """Registra un nuevo usuario con validación de datos y duplicados."""
        if not id_usuario or not nombre or not usuario or not clave:
            return False, "Todos los campos son obligatorios."

        if self.buscar_usuario_por_id(id_usuario):
            return False, f"El ID '{id_usuario}' ya está registrado."

        if any(u.usuario == usuario for u in self.usuarios):
            return False, f"El nombre de usuario '{usuario}' ya existe."

        nuevo_u = Usuario(id_usuario, nombre, usuario, clave, rol)
        self.usuarios.append(nuevo_u)
        if self._guardar_usuarios():
            return True, "Usuario registrado exitosamente."
        return False, "Error al guardar el usuario en disco."

    def actualizar_usuario(self, id_usuario: str, nombre: str, usuario: str, clave: str, rol: str) -> tuple[bool, str]:
        """Actualiza la información de un usuario existente."""
        u = self.buscar_usuario_por_id(id_usuario)
        if not u:
            return False, "El usuario a actualizar no existe."

        if not nombre or not usuario:
            return False, "Nombre y Usuario no pueden estar vacíos."

        # Verificar duplicado de nombre de usuario en otros registros
        if any(other.usuario == usuario and other.id_usuario != id_usuario for other in self.usuarios):
            return False, f"El nombre de usuario '{usuario}' ya pertenece a otro registro."

        u.nombre = nombre
        u.usuario = usuario
        if clave:  # Si se ingresó clave nueva, se actualiza
            u.clave = clave
        u.rol = rol

        if self._guardar_usuarios():
            return True, "Usuario actualizado exitosamente."
        return False, "Error al actualizar en disco."

    def eliminar_usuario(self, id_usuario: str) -> tuple[bool, str]:
        """Elimina un usuario asegurando que no se elimine la cuenta activa."""
        u = self.buscar_usuario_por_id(id_usuario)
        if not u:
            return False, "El usuario especificado no existe."

        if self.usuario_actual and self.usuario_actual.id_usuario == id_usuario:
            return False, "No puedes eliminar tu propia cuenta en sesión activa."

        self.usuarios.remove(u)
        if self._guardar_usuarios():
            return True, "Usuario eliminado correctamente."
        return False, "Error al persistir la eliminación."