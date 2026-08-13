from typing import Tuple, Dict, Callable
from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante

# TUPLE: Información estable del sistema que no cambia durante la ejecución
OPCIONES_MENU: Tuple[str, ...] = (
    "1. Registrar producto",
    "2. Buscar producto",
    "3. Actualizar producto",
    "4. Eliminar producto",
    "5. Listar productos",
    "6. Registrar usuario",
    "7. Listar usuarios",
    "8. Mostrar categorías",
    "9. Salir"
)


def mostrar_encabezado() -> None:
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE        ")
    print("========================================")
    for opcion in OPCIONES_MENU:
        if opcion.startswith("6.") or opcion.startswith("8."):
            print("----------------------------------------")
        print(opcion)
    print("========================================")


# --- FUNCIONES DE INTERACCIÓN (CONSOLA -> SERVICIO) ---

def opc_registrar_producto(servicio: Restaurante) -> None:
    print("\n--- Registrar Producto ---")
    codigo = input("Ingrese el código del producto: ").strip()
    if not codigo:
        print("❌ Error: El código no puede estar vacío.")
        return

    nombre = input("Ingrese el nombre del producto: ").strip()
    categoria = input("Ingrese la categoría: ").strip()

    try:
        precio = float(input("Ingrese el precio: "))
        if precio <= 0:
            print("❌ Error: El precio debe ser un número positivo.")
            return
    except ValueError:
        print("❌ Error: Debe ingresar un valor numérico válido para el precio.")
        return

    nuevo_producto = Producto(codigo, nombre, categoria, precio)
    if servicio.registrar_producto(nuevo_producto):
        print("✅ Producto registrado exitosamente.")
    else:
        print("❌ Error: Ya existe un producto registrado con ese código.")


def opc_buscar_producto(servicio: Restaurante) -> None:
    print("\n--- Buscar Producto ---")
    codigo = input("Ingrese el código a buscar: ").strip()
    producto = servicio.buscar_producto_por_codigo(codigo)
    if producto:
        print(f"✅ Producto encontrado: {producto}")
    else:
        print("❌ Producto no encontrado.")


def opc_actualizar_producto(servicio: Restaurante) -> None:
    print("\n--- Actualizar Producto ---")
    codigo = input("Ingrese el código del producto a actualizar: ").strip()
    producto = servicio.buscar_producto_por_codigo(codigo)

    if not producto:
        print("❌ Error: No existe un producto con ese código.")
        return

    print(f"Datos actuales: {producto}")
    nuevo_nombre = input("Ingrese el nuevo nombre: ").strip()
    nueva_categoria = input("Ingrese la nueva categoría: ").strip()

    try:
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        if nuevo_precio <= 0:
            print("❌ Error: El precio debe ser mayor a cero.")
            return
    except ValueError:
        print("❌ Error: Debe ingresar un número válido.")
        return

    if servicio.actualizar_producto(codigo, nuevo_nombre, nueva_categoria, nuevo_precio):
        print("✅ Producto actualizado correctamente.")


def opc_eliminar_producto(servicio: Restaurante) -> None:
    print("\n--- Eliminar Producto ---")
    codigo = input("Ingrese el código del producto a eliminar: ").strip()
    if servicio.eliminar_producto(codigo):
        print("✅ Producto eliminado exitosamente.")
    else:
        print("❌ Error: No se encontró ningún producto con ese código.")


def opc_listar_productos(servicio: Restaurante) -> None:
    print("\n--- Lista de Productos ---")
    productos = servicio.listar_productos()
    if not productos:
        print("ℹ️ No hay productos registrados.")
    else:
        for p in productos:
            print(f"  • {p}")


def opc_registrar_usuario(servicio: Restaurante) -> None:
    print("\n--- Registrar Usuario ---")
    identificacion = input("Ingrese la identificación (ID): ").strip()
    if not identificacion:
        print("❌ Error: La identificación no puede estar vacía.")
        return

    nombre = input("Ingrese el nombre completo: ").strip()
    correo = input("Ingrese el correo electrónico: ").strip()

    nuevo_usuario = Usuario(identificacion, nombre, correo)
    if servicio.registrar_usuario(nuevo_usuario):
        print("✅ Usuario registrado exitosamente.")
    else:
        print("❌ Error: Ya existe un usuario registrado con esa identificación.")


def opc_listar_usuarios(servicio: Restaurante) -> None:
    print("\n--- Lista de Usuarios ---")
    usuarios = servicio.listar_usuarios()
    if not usuarios:
        print("ℹ️ No hay usuarios registrados.")
    else:
        for u in usuarios:
            print(f"  • {u}")


def opc_mostrar_categorias(servicio: Restaurante) -> None:
    print("\n--- Categorías Únicas Registradas ---")
    categorias = servicio.obtener_categorias_unicas()
    if not categorias:
        print("ℹ️ No hay categorías disponibles (no se han registrado productos).")
    else:
        for cat in categorias:
            print(f"  • {cat}")


def main() -> None:
    servicio = Restaurante()

    # DICT: Relación clave -> valor asociando la opción seleccionada con su función handler
    despachador: Dict[str, Callable[[Restaurante], None]] = {
        "1": opc_registrar_producto,
        "2": opc_buscar_producto,
        "3": opc_actualizar_producto,
        "4": opc_eliminar_producto,
        "5": opc_listar_productos,
        "6": opc_registrar_usuario,
        "7": opc_listar_usuarios,
        "8": opc_mostrar_categorias,
    }

    while True:
        mostrar_encabezado()
        opcion = input("Seleccione una opción (1-9): ").strip()

        if opcion == "9":
            print("\n👋 ¡Gracias por utilizar el Sistema de Restaurante! Hasta luego.")
            break

        accion = despachador.get(opcion)
        if accion:
            accion(servicio)
        else:
            print("❌ Opción no válida. Por favor, intente de nuevo seleccionando entre 1 y 9.")


if __name__ == "__main__":
    main()