import json
import os
from typing import List
from modelos.producto import Producto


class ArchivoServicio:
    def __init__(self, ruta_archivo: str = "datos/productos.json") -> None:
        self.ruta_archivo: str = ruta_archivo
        self._asegurar_directorio()

    def _asegurar_directorio(self) -> None:
        """Crea la carpeta 'datos' si no existe."""
        directorio = os.path.dirname(self.ruta_archivo)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)

    def cargar_productos(self) -> List[Producto]:
        """Carga productos desde el archivo JSON gestionando excepciones requeridas."""
        productos: List[Producto] = []

        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                if not isinstance(datos, list):
                    print("Advertencia: El archivo JSON no contiene una lista. Se iniciará vacío.")
                    return []

                for registro in datos:
                    try:
                        producto = Producto.desde_diccionario(registro)
                        productos.append(producto)
                    except (KeyError, ValueError) as e:
                        print(f"Error al reconstruir un registro del archivo JSON: {e}")

        except FileNotFoundError:
            print(f"Archivo '{self.ruta_archivo}' no encontrado. Se creará uno nuevo al guardar datos.")
        except json.JSONDecodeError:
            print("Error: El archivo JSON está corrupto o mal formateado. Se iniciará con lista vacía.")
        except PermissionError:
            print("Error: Permisos insuficientes para leer el archivo de productos.")
        except Exception as e:
            print(f"Error inesperado al cargar productos: {e}")

        return productos

    def guardar_productos(self, productos: List[Producto]) -> bool:
        """Guarda la lista de objetos Producto en el archivo JSON."""
        try:
            datos = [producto.a_diccionario() for producto in productos]
            with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
            return True
        except PermissionError:
            print("Error: Permisos insuficientes para escribir en el archivo.")
            return False
        except Exception as e:
            print(f"Error al guardar los productos en JSON: {e}")
            return False