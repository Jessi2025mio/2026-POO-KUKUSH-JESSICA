import json
import os
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATOS_DIR = os.path.join(BASE_DIR, "datos")

    RUTA_PRODUCTOS = os.path.join(DATOS_DIR, "productos.json")
    RUTA_USUARIOS = os.path.join(DATOS_DIR, "usuarios.json")
    RUTA_VENTAS = os.path.join(DATOS_DIR, "ventas.json")

    @classmethod
    def _asegurar_directorio(cls):
        if not os.path.exists(cls.DATOS_DIR):
            os.makedirs(cls.DATOS_DIR)

    @classmethod
    def guardar_datos(cls, ruta: str, lista_objetos: list) -> None:
        cls._asegurar_directorio()
        try:
            datos = [obj.a_diccionario() for obj in lista_objetos]
            with open(ruta, "w", encoding="utf-8") as f:
                json.dump(datos, f, ensure_ascii=False, indent=4)
        except (PermissionError, IOError) as e:
            print(f"Error al guardar datos en {ruta}: {e}")

    @classmethod
    def cargar_productos(cls) -> list[Producto]:
        try:
            with open(cls.RUTA_PRODUCTOS, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return [Producto.desde_diccionario(d) for d in datos]
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            return []
        except PermissionError as e:
            print(f"Error de permisos al leer productos: {e}")
            return []

    @classmethod
    def cargar_usuarios(cls) -> list[Usuario]:
        try:
            with open(cls.RUTA_USUARIOS, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return [Usuario.desde_diccionario(d) for d in datos]
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            return []
        except PermissionError as e:
            print(f"Error de permisos al leer usuarios: {e}")
            return []

    @classmethod
    def cargar_ventas(cls) -> list[Venta]:
        try:
            with open(cls.RUTA_VENTAS, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return [Venta.desde_diccionario(d) for d in datos]
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            return []
        except PermissionError as e:
            print(f"Error de permisos al leer ventas: {e}")
            return []