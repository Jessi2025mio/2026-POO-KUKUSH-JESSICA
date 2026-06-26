# Sistema de Gestión de Restaurante (`restaurante_app`)

**Estudiante:** Jessica Lisbeth Kukush Shiguango   
**Asignatura:** Programación Orientada a Objetos  
**Semana:** 5

---

## 📝 Descripción del Sistema
Este sistema es una solución modular básica desarrollada en Python que simula la administración interna de un restaurante. Permite registrar diferentes tipos de productos (como platos y bebidas) y almacenar la información de los clientes del establecimiento, integrando todo el flujo en una capa de servicio centralizada mediante Programación Orientada a Objetos (POO).

## 📂 Estructura del Proyecto
El diseño del software respeta rigurosamente las arquitecturas de organización de archivos modulares en Python:
- `modelos/`: Contiene los moldes o entidades de datos del negocio (`producto.py` y `cliente.py`).
- `servicios/`: Contiene la lógica operativa y almacenamiento temporal de la información (`restaurante.py`).
- `main.py`: Archivo principal encargado de arrancar el programa, instanciar objetos y simular el comportamiento en la consola.

## 📊 Tipos de Datos Utilizados
Se implementaron de forma estricta los siguientes tipos de datos según la guía académica:
1. **`str` (Texto):** Utilizado para nombres de productos, nombres completos de clientes y números de cédula.
2. **`int` (Entero):** Utilizado para el stock disponible de productos y la edad de los clientes.
3. **`float` (Decimal):** Utilizado para representar los precios financieros del menú.
4. **`bool` (Lógico/Booleano):** Utilizado para definir estados lógicos como la disponibilidad de un plato (`disponible`) o la fidelidad de un usuario (`cliente_frecuente`).
5. **`list` (Compuesto):** Implementado en la clase de servicio para almacenar las colecciones mutables y ordenadas de los objetos de tipo `Producto` y `Cliente`.

## 🧠 Reflexión Académica

La organización modular en Python, combinada con el uso de identificadores descriptivos y las convenciones de nombres como PascalCase y snake_case, facilita el desarrollo de programas claros, ordenados y fáciles de mantener.

Además, seleccionar correctamente los tipos de datos (`str`, `int`, `float` y `bool`) permite representar la información según su naturaleza, mientras que el uso de listas facilita la administración de múltiples objetos relacionados con el sistema.

Este proyecto demuestra cómo la Programación Orientada a Objetos permite organizar mejor el código, mejorar su reutilización y facilitar futuras ampliaciones del sistema.