# main.py

# Importaciones correspondientes de los módulos externos creados
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def arrancar_programa():
    # 1. Crear el objeto del servicio principal
    mi_restaurante = Restaurante("Sabores Amazónicos")

    print("--- REGISTRANDO DATOS INICIALES ---")

    # 2. Crear al menos dos objetos de cada modelo
    producto_uno = Producto("Maito de Pescado", 12.50, 15, True)
    producto_dos = Producto("Chicha de Chonta", 2.00, 40, True)

    cliente_uno = Cliente("1500123456", "Ana María López", 28, True)
    cliente_dos = Cliente("1722987654", "Carlos Javier Torres", 19, False)

    # 3. Agregar los objetos a las listas administradas por el servicio principal
    mi_restaurante.registrar_producto(producto_uno)
    mi_restaurante.registrar_producto(producto_dos)

    mi_restaurante.registrar_cliente(cliente_uno)
    mi_restaurante.registrar_cliente(cliente_dos)

    # 4. Mostrar la información registrada de forma organizada en consola
    mi_restaurante.mostrar_informacion_general()

    # 5. Mostrar los totales consolidados (Mejora del sistema)
    mi_restaurante.mostrar_totales()


# Punto de arranque del script principal
if __name__ == "__main__":
    arrancar_programa()