# Restaurante App - Semana 12: Optimización mediante Colecciones

## Descripción del Proyecto
Evolución modular del sistema **restaurante_app** correspondiente a la Semana 12. En esta versión se incorporan estructuras de datos auxiliares (`dict` y `set`) para actuar como índices en memoria, permitiendo reducir la complejidad temporal de búsquedas y validaciones de **O(n)** a **O(1)** a medida que incrementa la cantidad de registros.

---

## Mejoras de Rendimiento Aplicadas

1. **Búsqueda Directa por Clave Única (`dict`):**
   - **Índice de Productos:** Se creó `_index_productos_codigo` para acceder a cualquier objeto `Producto` de forma inmediata mediante su código sin necesidad de recorrer la lista completa.
   - **Índice de Usuarios:** Se creó `_index_usuarios_id` para resolver búsquedas de usuarios por cédula/identificación en tiempo constante $O(1)$.

2. **Optimización de Consultas Agrupadas (`dict` con listas):**
   - **Índice de Ventas por Cliente:** Se estructuró `_index_ventas_usuario` (`{identificacion: [Venta]}`). Esto evita iterar sobre la lista global de ventas cada vez que se requiere el historial de un cliente particular.

3. **Validación de Unicidad (`set`):**
   - Se implementó `_codigos_productos_set` para comprobar la existencia previa de un código de producto durante el registro sin esccanear la lista principal.

4. **Reconstrucción y Sincronización:**
   - Los índices se reconstruyen automáticamente al consumir la persistencia en `datos/*.json` durante el arranque de la aplicación.
   - Se mantiene sincronización instantánea al insertar o actualizar ventas y productos.

---

## Estructura Modular

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