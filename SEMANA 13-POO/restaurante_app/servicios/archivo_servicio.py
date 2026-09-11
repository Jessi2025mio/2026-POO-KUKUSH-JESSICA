import json
import os
from typing import Any


class ArchivoServicio:
    @staticmethod
    def cargar_json(ruta_relativa: str) -> list[Any] | tuple[()] | Any:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ruta_absoluta = os.path.join(base_dir, ruta_relativa)

        if not os.path.exists(ruta_absoluta):
            return []

        try:
            with open(ruta_absoluta, 'r', encoding='utf-8') as file:
                return json.load(file)
        except Exception:
            return []