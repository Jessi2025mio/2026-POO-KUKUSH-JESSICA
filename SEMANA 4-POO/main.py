# ==========================================
# PUNTO DE ARRANQUE PRINCIPAL DEL PROGRAMA
# ==========================================

# 1. IMPORTACIONES: Usamos rutas del paquete para evitar ModuleNotFoundError
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def ejecutar_sistema():
    print("==================================================")
    print("   SISTEMA DE GESTIÓN DE RESTAURANTE (SEMANA 4)   ")
    print("==================================================")

    # 2. CREACIÓN DE OBJETOS
    platillo1 = Producto("Maito de Pescado", 8.50, "Plato Fuerte")
    platillo2 = Producto("Chicha de Chonta", 2.00, "Bebida")
    platillo3 = Producto("Volquetero Amazónico", 6.00, "Plato Fuerte")

    cliente1 = Cliente("Carlos Andrade", "1600123456", 4)
    cliente2 = Cliente("María Guamán", "1700987654", 2)

    # 3. INSTANCIACIÓN DEL SERVICIO PRINCIPAL
    mi_restaurante = Restaurante("Rincón Amazónico")

    print("\n--- Registrando Información en el Sistema ---")

    # 4. AGREGAR OBJETOS AL SERVICIO
    mi_restaurante.registrar_producto(platillo1)
    mi_restaurante.registrar_producto(platillo2)
    mi_restaurante.registrar_producto(platillo3)

    print("")  # Salto de línea estético

    mi_restaurante.registrar_cliente(cliente1)
    mi_restaurante.registrar_cliente(cliente2)

    # 5. MOSTRAR LA INFORMACIÓN EN CONSOLA
    mi_restaurante.mostrar_menu()
    mi_restaurante.mostrar_clientes_activos()

    print("\n==================================================")
    print("        EJECUCIÓN FINALIZADA CON ÉXITO            ")
    print("==================================================")

if __name__ == "__main__":
    ejecutar_sistema()