# main.py
from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante


def ejecutar_sistema():
    print("Iniciando el sistema restaurante_app...\n")

    # 1. Crear el restaurante
    mi_restaurante = Restaurante("La Casona de la Sierra")

    # 2. Crear dos objetos de tipo Platillo
    platillo1 = Platillo("Locro de Papa con Queso", 5.25, 350)
    platillo2 = Platillo("Hornado Tradicional", 8.50, 580)

    # 3. Crear dos objetos de tipo Bebida
    bebida1 = Bebida("Canelazo Caliente", 2.50, 250)
    bebida2 = Bebida("Jugo de Tomate de Arbol", 1.80, 300)

    print("--- Registrando productos en el menú ---")
    # 4. Agregar los objetos a la lista del servicio
    mi_restaurante.agregar_producto(platillo1)
    mi_restaurante.agregar_producto(platillo2)
    mi_restaurante.agregar_producto(bebida1)
    mi_restaurante.agregar_producto(bebida2)

    # 5. Prueba de encapsulación y validación
    print("\n--- Prueba de Seguridad (Encapsulación) ---")
    print(f"Precio original de {bebida1.nombre}: ${bebida1.obtener_precio():.2f}")

    # Intento de asignación incorrecta (precio negativo)
    bebida1.cambiar_precio(-2.00)

    # Asignación correcta
    bebida1.cambiar_precio(2.25)
    print(f"Precio actualizado de {bebida1.nombre}: ${bebida1.obtener_precio():.2f}")

    # 6. Mostrar el menú final aplicando Polimorfismo
    mi_restaurante.mostrar_catalogo()


if __name__ == "__main__":
    ejecutar_sistema()
