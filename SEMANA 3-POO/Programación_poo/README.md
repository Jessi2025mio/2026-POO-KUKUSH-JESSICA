# Tarea Semana 3: Programas en Python utilizando Programación Tradicional y Programación Orientada a Objetos
**Estudiante:** Jessica Kukush   
**Asignatura:** Programación Orientada a Objetos  
**Institución:** Universidad Estatal Amazónica (UEA)  

---

## Descripción de los Programas Desarrollados
En este repositorio se implementó un sistema básico de gestión de mascotas para registrar y visualizar su información (nombre, especie y edad), aplicando dos paradigmas distintos de programación:

1. **programacion_tradicional/tradicional.py:** Resuelve el problema mediante programación tradicional utilizando variables y funciones. Los datos de la mascota se ingresan de forma dinámica por teclado mediante interacción directa con el usuario y posteriormente se muestran de forma organizada en la terminal.
2. **programacion_poo/:** Resuelve el mismo problema utilizando Programación Orientada a Objetos de manera modular. El archivo `mascota.py` contiene la estructura y definición de la clase `Mascota` con sus respectivos atributos y métodos, mientras que el archivo `main.py` se encarga de instanciar de forma explícita dos objetos independientes de dicha clase y ejecutar sus acciones correspondientes en el sistema.

---

## Reflexión: Diferencias entre la Programación Tradicional y la POO
Durante el desarrollo de esta actividad fue posible observar que ambos enfoques permiten resolver el mismo problema técnico, pero organizan el diseño estructural del código y el flujo de control de maneras completamente diferentes:

* **Enfoque del diseño:** La programación tradicional se centra en las acciones y procedimientos mediante el uso de funciones que manipulan datos almacenados en variables independientes. Este enfoque resulta adecuado para programas pequeños y sencillos, aunque puede volverse más complejo a medida que aumenta el tamaño del sistema debido al entrelazado de procedimientos.
* **Organización de la información:** La Programación Orientada a Objetos se basa en la creación de clases y objetos que representan elementos del mundo real. En este paradigma, los datos (atributos) y los comportamientos (métodos) se encuentran agrupados y encapsulados dentro de una misma estructura autónoma, lo que favorece el orden y protege la integridad de las variables internas contra modificaciones accidentales externas.
* **Mantenimiento y crecimiento:** La POO facilita la reutilización del código, el mantenimiento preventivo y la incorporación ágil de nuevas funcionalidades. Gracias a su estructura modular y el aislamiento de sus componentes, es posible ampliar o modificar el sistema sin afectar significativamente las partes del software que ya fueron desarrolladas.

---

## Conclusión
En conclusión, ambos paradigmas permiten resolver problemas informáticos de manera eficiente; sin embargo, la Programación Orientada a Objetos ofrece una mejor organización del código, reduce las dependencias complejas entre funciones, facilita el mantenimiento y favorece el crecimiento estructurado del software. Por esta razón, es uno de los enfoques más utilizados y vigentes en el desarrollo de aplicaciones modernas y sistemas de alta complejidad.