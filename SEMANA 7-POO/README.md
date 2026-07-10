# Sistema de Gestión de Restaurante (restaurante_app)

**Estudiante:** Jessica Lisbeth Kukush Shiguango  
**Asignatura:** Programación Orientada a Objetos - Semana 7  

## Descripción del Sistema
Este proyecto consiste en una aplicación modular de consola desarrollada en Python que simula el control interno de un restaurante. Su objetivo principal es gestionar de manera dinámica las entidades de **Productos** y **Clientes**, procesando datos reales ingresados por el usuario desde el teclado para transformarlos en objetos de software estructurados, validados y encapsulados.

---

## Estructura del Proyecto y Capas
El proyecto se encuentra organizado siguiendo una arquitectura limpia dividida estrictamente por responsabilidades:

- **`modelos/`**: Aloja las entidades de datos puras del negocio (`Producto` y `Cliente`).
- **`servicios/`**: Contiene la capa de lógica empresarial (`Restaurante`), encargada de centralizar las listas y operaciones de búsqueda o registro.
- **`main.py`**: Funciona como la interfaz de usuario en consola y orquestador del flujo total del programa.

---

## Conceptos de POO Aplicados

### 1. Constructor Tradicional `__init__`
Implementado en la clase `Producto`. Se utiliza para instanciar los objetos y definir sus estados iniciales de forma explícita mediante parámetros, garantizando que cada producto nazca con la estructura requerida.

### 2. Encapsulación mediante `@property` y `@setter`
Aplicado detalladamente en la clase `Producto`. Los métodos modificadores (`@setter`) actúan como filtros de validación obligatorios que impiden la corrupción de datos, bloqueando el registro de nombres o categorías vacías, o precios menores o iguales a cero.

### 3. Clases de Datos con `@dataclass`
Implementado en la clase `Cliente`. Se aprovechan las bondades nativas de Python para generar de forma limpia estructuras de datos compactas, reduciendo el código repetitivo y autogenerando constructores legibles de forma automática.

### 4. Menú Interactivo y Flujo Dinámico
El archivo principal maneja un ciclo continuo que interactúa con el usuario, captura los datos dinámicamente mediante `input()`, invoca los constructores de las clases para dar vida a los objetos y los transfiere a la capa de servicios para su almacenamiento en memoria.

---

## Reflexión sobre la Creación de Objetos Dinámicos
La creación de objetos mediante datos ingresados por el usuario permite que el sistema sea más flexible y dinámico. En lugar de trabajar con información fija dentro del código, el programa puede adaptarse a diferentes situaciones, facilitando el registro, consulta y administración de productos y clientes, además de fortalecer la comprensión de los principios de la Programación Orientada a Objetos.