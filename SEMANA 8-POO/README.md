# Sistema de Gestión de Restaurante - `restaurante_app`

**Estudiante:** Jessica Lisbeth Kukush Shiguango  
**Asignatura:** Programación Orientada a Objetos  
**Semana:** Semana 8 - Aplicación de Principios SOLID  
**Universidad:** Universidad Estatal Amazónica  

---

## 📝 Descripción del Sistema
`restaurante_app` es una aplicación de consola modular desarrollada en Python bajo la orientación a objetos. El sistema permite administrar de manera organizada la oferta de un restaurante (productos generales y bebidas) así como los clientes registrados, garantizando la extensibilidad, el bajo acoplamiento y el cumplimiento de principios de buen diseño de software.

---

## 📂 Estructura del Proyecto

```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
├── main.py
└── README.md
```

---

## ⚙️ Responsabilidad de cada Clase y Componente

* **`modelos/producto.py` (`Producto`)**: Clase base encargada exclusivamente de definir los atributos y comportamiento común de los productos (código, nombre, categoría, precio).
* **`modelos/bebida.py` (`Bebida`)**: Clase especializada que extiende a `Producto`, incorporando información particular de las bebidas (tamaño, tipo de envase).
* **`modelos/cliente.py` (`Cliente`)**: Encargada únicamente de representar la entidad del cliente y su información personal (identificación, nombre, correo).
* **`servicios/restaurante.py` (`Restaurante`)**: Clase de servicio que administra las colecciones internas, valida duplicados de códigos/cédulas y ejecuta operaciones de negocio (registrar, buscar y listar).
* **`main.py`**: Punto de entrada de la aplicación. Gestiona la interacción con el usuario mediante la consola (menú interactivo e `input()`), delegando toda la lógica al servicio `Restaurante`.

---

## 🔗 Relación entre Producto y Bebida

La relación entre `Producto` y `Bebida` es de **herencia ("es-un")**. Una `Bebida` **es un** `Producto` especializado que comparte los atributos esenciales de un producto del menú pero agrega propiedades específicas de su naturaleza líquida o de presentación (tamaño y envase). Sobrescribe el método `mostrar_informacion()` para extender su comportamiento sin romper la compatibilidad con la clase padre.

---

## 🎯 Principios SOLID Aplicados

### 1. **S — Responsabilidad Única (SRP)**
Cada componente del proyecto tiene un propósito claro y una única razón para cambiar:
* `Producto`, `Bebida` y `Cliente` representan datos del dominio.
* `Restaurante` administra la lógica y el almacenamiento.
* `main.py` maneja exclusivamente el flujo por consola.

### 2. **O — Abierto/Cerrado (OCP)**
El sistema está **abierto a la extensión pero cerrado a la modificación**. Se añadió la funcionalidad de bebidas agregando la subclase `Bebida` sin alterar el código de la clase base `Producto` ni modificar la lógica de gestión dentro de `Restaurante`.

### 3. **L — Sustitución de Liskov (LSP)**
Los objetos de tipo `Bebida` pueden reemplazar transparentemente a los de tipo `Producto` en cualquier parte del sistema sin afectar el comportamiento esperado. El servicio `Restaurante` almacena ambos objetos dentro de una misma lista `_productos: List[Producto]` y los recorre invocando `mostrar_informacion()` de manera **polimórfica**, sin necesidad de consultar si un objeto es de tipo `Producto` o `Bebida` mediante condicionales `if/isinstance`.

---

## 🚀 Instrucciones de Ejecución

1. Asegúrate de tener instalado Python 3.8 o superior.
2. Abre una terminal dentro del directorio raíz del proyecto `restaurante_app`.
3. Ejecuta el comando:
   ```bash
   python main.py
   ```
4. Navega por las opciones del menú de consola para registrar productos, bebidas, clientes o visualizarlos.

---

## 💡 Reflexión sobre el Diseño de Proyectos Mantenibles

Organizar un proyecto mediante una estructura clara de carpetas facilita la navegación del código, pero aplicar principios de diseño como **SOLID** garantiza su calidad interna. La separación de responsabilidades y la correcta implementación del polimorfismo permiten escalar las aplicaciones con el mínimo riesgo de errores. Cuando cada clase cumple una tarea delimitada, el mantenimiento del software se vuelve intuitivo y preparado para evolucionar en entornos de desarrollo profesional.