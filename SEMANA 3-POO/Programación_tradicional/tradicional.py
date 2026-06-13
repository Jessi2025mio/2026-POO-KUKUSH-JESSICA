# programacion_tradicional/tradicional.py

def registrar_mascota():
    """
    Función para registrar los datos de la mascota mediante teclado.
    Sigue el enfoque tradicional: se centra en el procedimiento de captura.
    """
    print("--- REGISTRO DE MASCOTA (ENFOQUE TRADICIONAL) ---")
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie (ej. Perro, Gato, Ave): ")

    # Validación para asegurar que la edad sea un número entero válido
    while True:
        try:
            edad = int(input("Ingrese la edad de la mascota: "))
            break
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido para la edad.")

    # Retorna los datos como variables independientes
    return nombre, especie, edad


def mostrar_informacion(nombre, especie, edad):
    """
    Función procedimental que recibe los datos sueltos como parámetros
    y se encarga de imprimirlos de forma organizada.
    """
    print("\n=======================================")
    print("      INFORMACIÓN DE LA MASCOTA")
    print("=======================================")
    print(f"Nombre:  {nombre}")
    print(f"Especie: {especie}")
    print(f"Edad:    {edad} años")
    print("=======================================\n")


# Bloque principal que controla la ejecución secuencial
if __name__ == "__main__":
    # 1. Se ejecutan las funciones y se guardan los datos en variables separadas
    pet_nombre, pet_especie, pet_edad = registrar_mascota()

    # 2. Se pasan esas variables a la función encargada de mostrar la información
    mostrar_informacion(pet_nombre, pet_especie, pet_edad)