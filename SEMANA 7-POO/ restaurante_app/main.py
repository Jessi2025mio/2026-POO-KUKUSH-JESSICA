# main.py
from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente


def mostrar_menu():
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("----------------------------------------")
    print("4. Registrar cliente.py")
    print("5. Listar clientes")
    print("6. Buscar cliente.py")
    print("----------------------------------------")
    print("7. Salir")
    print("========================================")


def ejecutar_sistema():
    # Instancia del servicio encargado de la lógica del negocio
    servicio_restaurante = Restaurante()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ").strip()

        if opcion == "1":
            # Registrar un nuevo producto
            print("\n--- Registrar Nuevo Producto ---")
            try:
                nombre = input("Nombre del producto: ")
                categoria = input("Categoría: ")
                precio = float(input("Precio: "))
                disponible_input = input("¿Está disponible? (S/N): ").strip().lower()
                disponible = disponible_input != 'n'

                # Creación del objeto usando el constructor tradicional de Producto
                nuevo_producto = Producto(nombre, categoria, precio, disponible)
                servicio_restaurante.registrar_producto(nuevo_producto)
                print("¡Producto registrado con éxito!")
            except ValueError as e:
                print(f"Error de validación: {e}. Intente de nuevo.")
            except Exception as e:
                print(f"Ocurrió un error inesperado: {e}")

        elif opcion == "2":
            # Mostrar todos los productos registrados
            print("\n--- Lista de Productos ---")
            productos = servicio_restaurante.listar_productos()
            if not productos:
                print("No hay productos registrados en el sistema.")
            else:
                for prod in productos:
                    print(prod.mostrar_informacion())

        elif opcion == "3":
            # Buscar un producto por su nombre
            print("\n--- Buscar Producto ---")
            nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
            producto = servicio_restaurante.buscar_producto(nombre_buscar)
            if producto:
                print("\nProducto Encontrado:")
                print(producto.mostrar_informacion())
            else:
                print("El producto solicitado no existe.")

        elif opcion == "4":
            # Registrar un nuevo cliente.py
            print("\n--- Registrar Nuevo Cliente ---")
            id_cliente = input("Identificador único (Cédula/ID): ").strip()
            if not id_cliente:
                print("El ID del cliente.py no puede estar vacío.")
                continue

            nombre = input("Nombre del cliente.py: ")
            # Validación para evitar nombres vacíos
            if not nombre.strip():
                print("El nombre no puede estar vacío.")
                continue

            correo = input("Correo electrónico: ")
            # Validación para evitar correos vacíos
            if not correo.strip():
                print("El correo no puede estar vacío.")
                continue

            # Creación del objeto Cliente usando el decorador @dataclass
            nuevo_cliente = Cliente(nombre, correo, id_cliente)
            servicio_restaurante.registrar_cliente(nuevo_cliente)
            print("¡Cliente registrado con éxito!")

        elif opcion == "5":
            # Mostrar todos los clientes registrados
            print("\n--- Lista de Clientes ---")
            clientes = servicio_restaurante.listar_clientes()
            if not clientes:
                print("No hay clientes registrados en el sistema.")
            else:
                for cli in clientes:
                    print(cli.mostrar_informacion())

        elif opcion == "6":
            # Buscar cliente.py por ID
            print("\n--- Buscar Cliente ---")
            id_buscar = input("Ingrese el ID del cliente.py a buscar: ")
            cliente = servicio_restaurante.buscar_cliente(id_buscar)
            if cliente:
                print("\nCliente Encontrado:")
                print(cliente.mostrar_informacion())
            else:
                print("El cliente.py solicitado no se encuentra registrado.")

        elif opcion == "7":
            print("\n¡Gracias por utilizar el Sistema de Restaurante! Saliendo...")
            break
        else:
            print("\nOpción no válida. Por favor, seleccione un número del 1 al 7.")


if __name__ == "__main__":
    ejecutar_sistema()