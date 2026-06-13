# programacion_poo/main.py

# Importamos la clase Mascota desde el archivo modular mascota.py
from mascota import Mascota

if __name__ == "__main__":
    print("--- SISTEMA DE GESTIÓN DE MASCOTAS (ENFOQUE POO) ---\n")

    # Cumpliendo el requisito: Creamos (instanciamos) al menos dos objetos de la clase Mascota
    mascota1 = Mascota("Max", "Perro", 4)
    mascota2 = Mascota("Luna", "Gato", 2)

    # Ejecutamos los métodos definidos para el primer objeto
    print("Datos e interacción de la primera mascota:")
    mascota1.mostrar_informacion()
    mascota1.hacer_sonido()
    print("-" * 60)

    # Ejecutamos los métodos definidos para el segundo objeto
    print("Datos e interacción de la segunda mascota:")
    mascota2.mostrar_informacion()
    mascota2.hacer_sonido()