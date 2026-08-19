from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio
from modelos.producto import Producto


def guardar_cambios(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    """Solicita la persistencia en el servicio de archivos."""
    exito = archivo_servicio.guardar_productos(restaurante.obtener_productos())
    if exito:
        print("-> Cambios guardados correctamente en JSON.")
    else:
        print("-> Advertencia: No se pudieron guardar los cambios en el archivo.")


def main() -> None:
    archivo_servicio = ArchivoServicio()
    restaurante = Restaurante()

    # Cargar datos al iniciar
    productos_cargados = archivo_servicio.cargar_productos()
    restaurante.establecer_productos(productos_cargados)
    print(f"Sistema iniciado. Productos cargados: {len(productos_cargados)}")

    while True:
        print("\n--- SISTEMA DE GESTIÓN DE RESTAURANTE ---")
        print("1. Registrar Producto")
        print("2. Listar Productos")
        print("3. Buscar Producto por ID")
        print("4. Actualizar Producto")
        print("5. Eliminar Producto")
        print("6. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            try:
                id_prod = int(input("Ingrese el ID del producto: "))
                nombre = input("Ingrese el nombre del producto: ")
                precio = float(input("Ingrese el precio: "))
                categoria = input("Ingrese la categoría: ")

                nuevo_producto = Producto(id_prod, nombre, precio, categoria)
                restaurante.registrar_producto(nuevo_producto)
                guardar_cambios(restaurante, archivo_servicio)
                print("Producto registrado con éxito.")
            except ValueError as e:
                print(f"Error de validación: {e}")

        elif opcion == "2":
            productos = restaurante.obtener_productos()
            if not productos:
                print("No hay productos registrados actualmente.")
            else:
                print("\n--- LISTA DE PRODUCTOS ---")
                for prod in productos:
                    print(prod)

        elif opcion == "3":
            try:
                id_prod = int(input("Ingrese el ID del producto a buscar: "))
                prod = restaurante.buscar_producto_por_id(id_prod)
                if prod:
                    print(f"Encontrado: {prod}")
                else:
                    print("Producto no encontrado.")
            except ValueError:
                print("El ID debe ser un número entero válido.")

        elif opcion == "4":
            try:
                id_prod = int(input("Ingrese el ID del producto a actualizar: "))
                if restaurante.buscar_producto_por_id(id_prod) is None:
                    print("El producto con ese ID no existe.")
                    continue

                nombre = input("Ingrese el nuevo nombre: ")
                precio = float(input("Ingrese el nuevo precio: "))
                categoria = input("Ingrese la nueva categoría: ")

                if restaurante.actualizar_producto(id_prod, nombre, precio, categoria):
                    guardar_cambios(restaurante, archivo_servicio)
                    print("Producto actualizado correctamente.")
            except ValueError as e:
                print(f"Error de validación al actualizar: {e}")

        elif opcion == "5":
            try:
                id_prod = int(input("Ingrese el ID del producto a eliminar: "))
                if restaurante.eliminar_producto(id_prod):
                    guardar_cambios(restaurante, archivo_servicio)
                    print("Producto eliminado correctamente.")
                else:
                    print("No se encontró un producto con ese ID.")
            except ValueError:
                print("El ID debe ser un entero válido.")

        elif opcion == "6":
            print("Saliendo del programa... ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()