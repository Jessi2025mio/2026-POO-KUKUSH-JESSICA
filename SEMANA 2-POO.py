# Programa que representa un objeto del mundo real usando POO
# Clase Alumno - Ejemplo práctico

class Alumno:
    def __init__(self, nom, car, nota):
        # las variables que nos pidieron
        self.nombre = nom
        self.carrera = car
        self.promedio = nota

    # método para ver los datos en la pantalla
    def ver(self):
        print("--- FICHA ---")
        print("Estudiante:", self.nombre)
        print("Carrera:", self.carrera)
        print("Nota:", self.promedio)

    # método para cambiar la nota
    def subir_nota(self, nuevo_promedio):
        self.promedio = nuevo_promedio
        print("Se actualizó la nota de", self.nombre, "a", self.promedio)


# --- PROBANDO EL PROGRAMA ---

# creamos al primer alumno
a1 = Alumno("Carlos Vega", "Ingeniería Ambiental", 7.8)
# creamos al segundo alumno
a2 = Alumno("Ana Chimbo", "Licenciatura en Turismo", 8.9)

# ejecutar las funciones
print("Revisando alumno 1:")
a1.ver()
a1.subir_nota(8.5)

print("\nRevisando alumno 2:")
a2.ver()
a2.subir_nota(9.0)