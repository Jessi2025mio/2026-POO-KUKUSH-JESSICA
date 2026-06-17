# Taller Práctico: Organización Modular - Semana 4

* **Estudiante:** Jessica Kukush
* **Asignatura:** Programación Orientada a Objetos
* **Institución:** Universidad Estatal Amazónica (UEA)
* **Semana:** Semana 4

## Descripción del Sistema
Este proyecto es un sistema básico para gestionar un restaurante usando Programación Orientada a Objetos en Python. El objetivo principal de la tarea es organizar el código en diferentes carpetas y archivos para separar los datos de la lógica del programa, logrando que los archivos se comuniquen correctamente mediante importaciones.

El sistema maneja tres clases principales:
1. **Producto:** Guarda los datos de los platos y bebidas (nombre, precio y categoría).
2. **Cliente:** Guarda la información de las personas que van al local (nombre, cédula y número de mesa).
3. **Restaurante:** Funciona como el servicio central que guarda las listas de productos y clientes en la memoria para poder mostrarlos ordenados.

## Estructura del Proyecto
El código está organizado de la siguiente manera:

```text
restaurante_app/
├── modelos/
│   ├── producto.py      # Contiene la clase Producto y sus atributos.
│   └── cliente.py       # Contiene la clase Cliente y sus datos.
├── servicios/
│   └── restaurante.py   # Contiene la lógica para registrar y listar todo.
└── main.py              # Archivo principal para correr el programa.