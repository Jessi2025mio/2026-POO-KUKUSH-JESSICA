# Restaurante App - Semana 11

**Estudiante:** Jessica Lisbeth Kukush Shiguango 
**Asignatura:** Programación Orientada a Objetos  

## Descripción del Sistema
`restaurante_app` es una aplicación modular para la gestión de productos, usuarios y ventas en un restaurante. La versión de la Semana 11 integra la persistencia de datos mediante archivos JSON y maneja la relación entre usuarios y productos mediante transacciones de venta, manteniendo el control estricto de inventario (stock).

## Estructura del Proyecto
```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md