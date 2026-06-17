
# Módulo que representa a un cliente dentro del restaurante

class Cliente:
    def __init__(self, nombre, cedula, mesa):
        """
        Constructor para inicializar los atributos del cliente.
        """
        self.nombre = nombre    # Atributo: nombre completo
        self.cedula = cedula    # Atributo: identificación
        self.mesa = mesa        # Atributo: número de mesa asignada

    def __str__(self):
        """
        Método especial para representar al cliente como texto.
        """
        return f"Cliente: {self.nombre} | Mesa: {self.mesa}"