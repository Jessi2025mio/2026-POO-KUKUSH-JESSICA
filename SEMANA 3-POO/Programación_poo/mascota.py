# programacion_poo/mascota.py

class Mascota:
    """
    Clase Mascota: Representa la abstracción de una mascota del mundo real.
    Agrupa los datos (atributos) y los comportamientos (métodos) en una sola entidad.
    """

    def __init__(self, nombre, especie, edad):
        """
        Método Constructor: Inicializa los atributos del objeto cuando es creado.
        """
        self.nombre = nombre  # Atributo para almacenar el nombre
        self.especie = especie  # Atributo para almacenar la especie
        self.edad = edad  # Atributo para almacenar la edad

    def mostrar_informacion(self):
        """
        Método de la clase: Permite que el propio objeto imprima sus atributos internos.
        """
        print(f"Mascota: {self.nombre:<12} | Especie: {self.especie:<12} | Edad: {self.edad} años")

    def hacer_sonido(self):
        """
        Método de la clase: Define una acción/comportamiento que varía según la especie.
        """
        esp = self.especie.lower()
        if "perro" in esp:
            print(f"{self.nombre} dice: ¡Guau guau!")
        elif "gato" in esp:
            print(f"{self.nombre} dice: ¡Miau miau!")
        else:
            print(f"{self.nombre} hace un sonido característico de su especie.")