import os
from modelos.usuario import Usuario
from modelos.producto import Producto
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.ruta_usuarios = os.path.join(base_dir, 'datos', 'usuarios.json')
        self.ruta_productos = os.path.join(base_dir, 'datos', 'productos.json')

    # --- Autenticación y Usuarios ---
    def autenticar_usuario(self, username, password):
        if not username or not password:
            return False, "Por favor complete todos los campos de acceso."

        datos = ArchivoServicio.leer_json(self.ruta_usuarios)
        for u in datos:
            if u["username"] == username and u["password"] == password:
                return True, Usuario.from_dict(u)
        return False, "Usuario o contraseña incorrectos."

    def obtener_usuarios(self):
        datos = ArchivoServicio.leer_json(self.ruta_usuarios)
        return [Usuario.from_dict(u) for u in datos]

    # --- Gestión de Productos ---
    def obtener_productos(self):
        datos = ArchivoServicio.leer_json(self.ruta_productos)
        return [Producto.from_dict(p) for p in datos]

    def buscar_producto_por_id(self, id_producto):
        if not id_producto:
            return False, "Ingrese un ID para buscar.", None

        productos = self.obtener_productos()
        for p in productos:
            if p.id_producto == id_producto:
                return True, "Producto encontrado.", p
        return False, "No se encontró un producto con ese ID.", None

    def registrar_producto(self, id_producto, nombre, categoria, precio):
        if not id_producto or not nombre or not categoria or not precio:
            return False, "Todos los campos son obligatorios."

        try:
            precio_val = float(precio)
            if precio_val <= 0:
                return False, "El precio debe ser mayor a 0."
        except ValueError:
            return False, "El precio debe ser un valor numérico."

        productos = self.obtener_productos()
        for p in productos:
            if p.id_producto == id_producto:
                return False, "Ya existe un producto registrado con ese ID."

        nuevo_prod = Producto(id_producto, nombre, categoria, precio_val)
        productos.append(nuevo_prod)
        self._guardar_productos(productos)
        return True, "Producto registrado con éxito."

    def actualizar_producto(self, id_producto, nombre, categoria, precio):
        if not id_producto or not nombre or not categoria or not precio:
            return False, "Todos los campos son obligatorios."

        try:
            precio_val = float(precio)
            if precio_val <= 0:
                return False, "El precio debe ser mayor a 0."
        except ValueError:
            return False, "El precio debe ser un valor numérico."

        productos = self.obtener_productos()
        encontrado = False
        for i, p in enumerate(productos):
            if p.id_producto == id_producto:
                productos[i] = Producto(id_producto, nombre, categoria, precio_val)
                encontrado = True
                break

        if not encontrado:
            return False, "El ID no existe. No se pudo actualizar."

        self._guardar_productos(productos)
        return True, "Producto actualizado correctamente."

    def eliminar_producto(self, id_producto):
        if not id_producto:
            return False, "Debe especificar el ID del producto a eliminar."

        productos = self.obtener_productos()
        productos_filtrados = [p for p in productos if p.id_producto != id_producto]

        if len(productos) == len(productos_filtrados):
            return False, "No se encontró el producto a eliminar."

        self._guardar_productos(productos_filtrados)
        return True, "Producto eliminado exitosamente."

    def _guardar_productos(self, lista_productos):
        datos = [p.to_dict() for p in lista_productos]
        ArchivoServicio.guardar_json(self.ruta_productos, datos)