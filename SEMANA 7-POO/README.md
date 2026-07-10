# Sistema de Gestión de Restaurante (restaurante_app)

**Estudiante:** Jessica Lisbeth Kukush Shiguango  
**Asignatura:** Programación Orientada a Objetos - Semana 7  

## Descripción del Sistema
Este proyecto es una aplicación modular de consola desarrollada en Python que simula la administración interna de un restaurante. Permite gestionar dinámicamente dos entidades esenciales: **Productos** y **Clientes**, procesando datos del mundo real ingresados por teclado para transformarlos de forma transparente en objetos de software estructurados y validados.

---

## Estructura del Proyecto y Capas
El código sigue un patrón de arquitectura limpia dividida por responsabilidades:

- **`modelos/`**: Capa de entidades de datos puras (`Producto` y `Cliente`).
- **`servicios/`**: Capa lógica encargada del negocio (`Restaurante`), donde se administran y centralizan los datos.
- **`main.py`**: Interfaz de usuario (Consola) y orquestador del flujo del programa.

---

## Conceptos POO Aplicados

### 1. Constructor Tradicional `__init__`
Implementado en la clase `Producto`. Se encarga de instanciar y asignar los estados iniciales del objeto de forma controlada a través de parámetros explícitos, garantizando que todo objeto empiece con un estado válido.

### 2. Control de Atributos mediante `@property` y `@setter`
Utilizados en `Producto` para cumplir con el principio de encapsulación. Los modificadores `@setter` actúan como compuertas lógicas impidiendo el registro de datos corruptos o incongruentes, tales como nombres o categorías vacías, o precios menores/iguales a 0.

### 3. Clases de Datos con `@dataclass`
Implementado en la clase `Cliente`. Se aprovechan las bondades nativas de Python para declarar componentes de datos puros de forma ágil, autogenerando métodos implícitos útiles como el constructor inicial de manera limpia y legible.

### 4. Menú Interactivo de Consola
Permite una simulación en tiempo real. Captura el flujo ordenado:  
`Ingreso por input() ➔ Constructor ➔ Creación del Objeto ➔ Guardado en Servicio ➔ Consulta`.

---

## Reflexión sobre la Creación de Objetos Dinámicos
La creación de objetos mediante datos ingresados por el usuario permite que el sistema sea más flexible y dinámico. En lugar de trabajar con información fija dentro del código, el programa puede adaptarse a diferentes situaciones, facilitando el registro, consulta y administración de productos y clientes, además de fortalecer la comprensión de los principios de la Programación Orientada a Objetos.