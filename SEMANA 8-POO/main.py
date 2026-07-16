from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def mostrar_menu() -> None:
    """Muestra las opciones del menú principal."""
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE        ")
    print("========================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("----------------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("----------------------------------------")
    print("6. Salir")
    print("========================================")


def opcion_registrar_producto(servicio: Restaurante) -> None:
    print("\n--- Registrar Nuevo Producto ---")
    codigo = input("Ingrese el código del producto: ").strip()
    nombre = input("Ingrese el nombre del producto: ").strip()
    categoria = input("Ingrese la categoría del producto: ").strip()

    try:
        precio = float(input("Ingrese el precio: "))
        producto = Producto(codigo, nombre, categoria, precio)
        servicio.registrar_producto(producto)
    except ValueError:
        print("Error: El precio debe ser un número válido.")


def opcion_registrar_bebida(servicio: Restaurante) -> None:
    print("\n--- Registrar Nueva Bebida ---")
    codigo = input("Ingrese el código de la bebida: ").strip()
    nombre = input("Ingrese el nombre de la bebida: ").strip()
    categoria = input("Ingrese la categoría (ej: Fría, Caliente): ").strip()

    try:
        precio = float(input("Ingrese el precio: "))
        tamano = input("Ingrese el tamaño (ej: 500ml, 1 Litro): ").strip()
        envase = input("Ingrese el tipo de envase (ej: Botella, Vidrio, Lata): ").strip()

        bebida = Bebida(codigo, nombre, categoria, precio, tamano, envase)
        servicio.registrar_producto(bebida)
    except ValueError:
        print("Error: El precio debe ser un número válido.")


def opcion_registrar_cliente(servicio: Restaurante) -> None:
    print("\n--- Registrar Nuevo Cliente ---")
    identificacion = input("Ingrese número de identificación/Cédula: ").strip()
    nombre = input("Ingrese el nombre del cliente: ").strip()
    correo = input("Ingrese el correo electrónico: ").strip()

    cliente = Cliente(identificacion, nombre, correo)
    servicio.registrar_cliente(cliente)


def main() -> None:
    servicio_restaurante = Restaurante()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            opcion_registrar_producto(servicio_restaurante)
        elif opcion == "2":
            opcion_registrar_bebida(servicio_restaurante)
        elif opcion == "3":
            opcion_registrar_cliente(servicio_restaurante)
        elif opcion == "4":
            servicio_restaurante.listar_productos()
        elif opcion == "5":
            servicio_restaurante.listar_clientes()
        elif opcion == "6":
            print("\n¡Gracias por utilizar el sistema del restaurante! Hasta luego.")
            break
        else:
            print("Opción no válida. Por favor intente de nuevo.")


if __name__ == "__main__":
    main()