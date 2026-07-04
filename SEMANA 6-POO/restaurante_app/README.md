# Tarea Semana 6 - Aplicación Modular Restaurante App

**Estudiante:** Jessica Lisbeth Kukush Shiguango  
**Asignatura:** Programación Orientada a Objetos  

## Descripción del Sistema
Este proyecto consiste en una aplicación modular de consola en Python para gestionar el catálogo de productos de un restaurante ("La Casona de la Sierra"). El sistema organiza el menú dividiendo las comidas y las bebidas mediante clases especializadas, aplicando los principios clave de la programación orientada a objetos.

## Estructura del Proyecto
El código se organizó en diferentes carpetas separando las responsabilidades del programa:
- **`modelos/`**: Contiene las clases que definen los datos del sistema (`Producto`, `Platillo` y `Bebida`).
- **`servicios/`**: Contiene la clase `Restaurante` que se encarga de guardar los productos en una lista y controlar el menú.
- **`main.py`**: Es el archivo principal que sirve como punto de arranque para probar todo el funcionamiento del sistema.

## Aplicación de Principios de POO

### 1. Herencia
Se creó la clase padre `Producto` para agrupar los atributos que tienen en común todos los artículos del restaurante (nombre, precio y disponibilidad). Las clases hijas `Platillo` y `Bebida` heredan de ella. Para reutilizar el código del padre, se utilizó la función `super().__init__()` dentro de los constructores de las clases hijas.

### 2. Encapsulación
Para proteger el atributo del precio y evitar que se altere de forma incorrecta desde fuera de la clase, se configuró como privado usando doble guion bajo (`__precio`). Su acceso se controla mediante el método de lectura `obtener_precio()` y su modificación pasa por `cambiar_precio()`, el cual valida que el nuevo valor sea estrictamente mayor a cero.

### 3. Polimorfismo
El polimorfismo se aplica al sobrescribir el método `mostrar_informacion()` en las clases hijas. La clase padre muestra los datos básicos, pero cada clase hija añade sus propios detalles (calorías en los platos y mililitros en las bebidas). Cuando el servicio recorre la lista general de productos con un bucle `for`, ejecuta el mismo método para todos, pero cada objeto se muestra de forma diferente según su tipo.

## Reflexión sobre la Modularidad en Python
Organizar el código de forma modular dividiéndolo en carpetas y archivos independientes ayuda a que el proyecto sea mucho más ordenado y fácil de mantener. Si en el futuro el restaurante necesita agregar nuevos tipos de productos (como postres o combos), solo se debe crear un archivo nuevo que herede de la clase padre sin necesidad de modificar o arriesgar el código que ya funciona correctamente.