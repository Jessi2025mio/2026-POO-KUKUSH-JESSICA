# Restaurante App - Semana 10

**Estudiante:** Jessica Lisbeth Kukush Shiguango 
**Asignatura:** Programación Orientada a Objetos  

## Descripción del Proyecto
Esta entrega es la evolución del sistema `restaurante_app`. Implementa la persistencia de datos de productos utilizando un archivo en formato JSON (`datos/productos.json`), permitiendo conservar la información entre ejecuciones y manteniendo la arquitectura orientada a objetos.

## Estructura del Proyecto
```text
restaurante_app/
├── datos/
│   └── productos.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md