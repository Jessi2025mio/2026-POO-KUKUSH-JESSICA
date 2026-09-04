from servicios.restaurante import RestauranteService
from modelos.producto import Producto
from modelos.usuario import Usuario


def main():
    service = RestauranteService()

    # Pre-poblado de datos de prueba si el sistema está vacío
    if not service.productos:
        service.registrar_producto(Producto("P001", "Hamburguesa Doble", 5.50, 20))
        service.registrar_producto(Producto("P002", "Papas Fritas", 2.00, 50))
        service.registrar_producto(Producto("P003", "Gaseosa 500ml", 1.50, 30))

    if not service.usuarios:
        service.registrar_usuario(Usuario("1720001122", "Carlos Pérez", "carlos@mail.com"))
        service.registrar_usuario(Usuario("0912345678", "Ana Gómez", "ana@mail.com"))

    while True:
        print("\n--- RESTAURANTE APP (SEMANA 12 - OPTIMIZADO) ---")
        print("1. Buscar Producto por Código")
        print("2. Buscar Usuario por Cédula")
        print("3. Registrar Nueva Venta")
        print("4. Consultar Ventas de un Usuario")
        print("5. Registrar Nuevo Producto")
        print("6. Listar Todo (Productos y Usuarios)")
        print("7. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            cod = input("Ingrese el código del producto: ").strip()
            prod = service.buscar_producto_por_codigo(cod)
            if prod:
                print(f"-> Encontrado: {prod.nombre} | Precio: ${prod.precio:.2f} | Stock: {prod.stock}")
            else:
                print("-> Producto no encontrado.")

        elif opcion == "2":
            ced = input("Ingrese la identificación del usuario: ").strip()
            usr = service.buscar_usuario_por_id(ced)
            if usr:
                print(f"-> Encontrado: {usr.nombre} | Email: {usr.correo}")
            else:
                print("-> Usuario no encontrado.")

        elif opcion == "3":
            id_v = input("ID único para la venta (ej. V001): ").strip()
            ced = input("Cédula/ID del cliente: ").strip()
            cod = input("Código del producto: ").strip()
            cant = int(input("Cantidad a comprar: "))

            if service.registrar_venta(id_v, ced, cod, cant):
                print("-> Venta realizada con éxito y stock actualizado.")
            else:
                print("-> Error en la venta (Usuario/Producto invalido o Stock insuficiente).")

        elif opcion == "4":
            ced = input("Ingrese cédula del cliente: ").strip()
            ventas_usr = service.consultar_ventas_por_usuario(ced)
            if ventas_usr:
                print(f"-> Historial de ventas para {ced}:")
                for v in ventas_usr:
                    print(
                        f"   Venta #{v.id_venta} - Prod: {v.codigo_producto} | Cant: {v.cantidad} | Total: ${v.total:.2f}")
            else:
                print("-> El usuario no registra ventas.")

        elif opcion == "5":
            cod = input("Código nuevo: ").strip()
            nom = input("Nombre: ").strip()
            precio = float(input("Precio: "))
            stock = int(input("Stock inicial: "))

            if service.registrar_producto(Producto(cod, nom, precio, stock)):
                print("-> Producto registrado en la lista e índices auxiliares.")
            else:
                print("-> El código ya existe (Validación O(1) con set).")

        elif opcion == "6":
            print("\n--- PRODUCTOS ---")
            for p in service.productos:
                print(f"[{p.codigo}] {p.nombre} - ${p.precio:.2f} (Stock: {p.stock})")
            print("\n--- USUARIOS ---")
            for u in service.usuarios:
                print(f"[{u.identificacion}] {u.nombre}")

        elif opcion == "7":
            print("Saliendo de la aplicación...")
            break


if __name__ == "__main__":
    main()