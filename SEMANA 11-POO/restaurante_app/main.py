from servicios.restaurante import Restaurante


def mostrar_menu():
    print("\n--- SISTEMA RESTAURANTE APP ---")
    print("1. Registrar Usuario")
    print("2. Registrar Producto")
    print("3. Listar Usuarios")
    print("4. Listar Productos")
    print("5. Realizar Venta")
    print("6. Consultar Ventas de un Usuario")
    print("7. Salir")


def main():
    restaurante = Restaurante()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n-- Registro de Usuario --")
            id_u = input("Identificación: ").strip()
            nombre = input("Nombre: ").strip()
            if restaurante.registrar_usuario(id_u, nombre):
                print("Usuario registrado exitosamente.")
            else:
                print("Error: El usuario ya existe o los datos son inválidos.")

        elif opcion == "2":
            print("\n-- Registro de Producto --")
            codigo = input("Código: ").strip()
            nombre = input("Nombre: ").strip()
            try:
                precio = float(input("Precio: "))
                stock = int(input("Stock inicial: "))
                if restaurante.registrar_producto(codigo, nombre, precio, stock):
                    print("Producto registrado exitosamente.")
                else:
                    print("Error: El producto ya existe o los datos son inválidos.")
            except ValueError:
                print("Error: El precio y el stock deben ser valores numéricos válidos.")

        elif opcion == "3":
            print("\n-- Lista de Usuarios --")
            usuarios = restaurante.listar_usuarios()
            if not usuarios:
                print("No hay usuarios registrados.")
            for u in usuarios:
                print(f"ID: {u.identificacion} | Nombre: {u.nombre}")

        elif opcion == "4":
            print("\n-- Lista de Productos --")
            productos = restaurante.listar_productos()
            if not productos:
                print("No hay productos registrados.")
            for p in productos:
                print(f"Código: {p.codigo} | Nombre: {p.nombre} | Precio: ${p.precio:.2f} | Stock: {p.stock}")

        elif opcion == "5":
            print("\n-- Realizar Venta --")
            id_u = input("Identificación del Usuario: ").strip()
            cod_p = input("Código del Producto: ").strip()
            try:
                cantidad = int(input("Cantidad a comprar: "))
                exito, mensaje = restaurante.vender_producto(cod_p, id_u, cantidad)
                print(f"Resultado: {mensaje}")
            except ValueError:
                print("Error: La cantidad debe ser un número entero.")

        elif opcion == "6":
            print("\n-- Consultar Ventas por Usuario --")
            id_u = input("Identificación del Usuario: ").strip()
            usuario = restaurante.buscar_usuario(id_u)
            if usuario is None:
                print("Error: El usuario no existe.")
            else:
                ventas = restaurante.obtener_ventas_usuario(id_u)
                print(f"\nVentas registradas para {usuario.nombre} ({usuario.identificacion}):")
                if not ventas:
                    print("Este usuario no tiene ventas registradas.")
                for v in ventas:
                    print(f"- Producto: {v['nombre_producto']} (Cód: {v['codigo_producto']}) | Cantidad: {v['cantidad']}")

        elif opcion == "7":
            print("\n¡Gracias por utilizar restaurante_app!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()