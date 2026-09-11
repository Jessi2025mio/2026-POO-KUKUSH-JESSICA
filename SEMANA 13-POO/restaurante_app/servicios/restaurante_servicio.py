from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self):
        self._usuarios = []
        self._productos = []
        self._cargar_datos()

    def _cargar_datos(self):
        data_usuarios = ArchivoServicio.cargar_json("datos/usuarios.json")
        self._usuarios = [Usuario.from_dict(u) for u in data_usuarios]

        data_productos = ArchivoServicio.cargar_json("datos/productos.json")
        self._productos = [Producto.from_dict(p) for p in data_productos]

    def validar_acceso(self, username: str, password: str):
        for usr in self._usuarios:
            if usr.username == username and usr.password == password:
                return usr
        return None

    def obtener_usuarios(self) -> list:
        return self._usuarios

    def obtener_productos(self) -> list:
        return self._productos