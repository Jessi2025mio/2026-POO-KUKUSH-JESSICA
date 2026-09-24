# Restaurante App - Semana 15: Conceptos Fundamentales de Manejo de Eventos

## Propósito
Este proyecto corresponde a la **Semana 15** de la asignatura *Programación Orientada a Objetos*. Su propósito principal es implementar y comprender los conceptos fundamentales del manejo de eventos en interfaces gráficas utilizando **Tkinter** y **Python**.

A través de la sección de **Ventas**, se demuestra cómo una acción directa del usuario sobre la interfaz invoca un callback por medio del parámetro `command=`, coordinando la operación con la capa de servicios sin vulnerar la separación de responsabilidades ni acceder directamente a los archivos de persistencia JSON desde la interfaz gráfica.

---

## Evolución del Proyecto
Respecto a las semanas anteriores, se han añadido e integrado las siguientes capacidades:
1. **Modelo de Ventas (`venta.py`):** Estructura que vincula la información de un usuario, un producto, el valor gastado y la marca de tiempo de la transacción.
2. **Persistencia JSON (`ventas.json`):** Almacenamiento persistente delegando las operaciones de lectura/escritura a `ArchivoServicio`.
3. **Módulo de Ventas en la Interfaz (`MainView`):** Integración de componentes `ttk.Combobox`, `ttk.Button` y `ttk.Treeview` para el control visual de transacciones.
4. **Manejo de Recursos Visuales (`/assets`):** Integración obligatoria de íconos y logotipos organizados para la identidad corporativa de la aplicación.

---

## Flujo de Eventos Implementado

El sistema evidencia la secuencia fundamental de manejo de eventos:
1. **Usuario:** Selecciona un usuario y producto en la interfaz, luego presiona el botón "Registrar Venta".
2. **Botón / Componente:** Captura la acción del usuario mediante el parámetro `command=`.
3. **Callback (`callback_registrar_venta`):** Extrae las selecciones de los componentes `Combobox` y transfiere la información al servicio.
4. **Restaurante Servicio (`RestauranteServicio`):** Ejecuta la lógica de negocio, realiza las validaciones correspondientes y crea el registro.
5. **Persistencia (`ventas.json`):** Almacena de forma permanente la nueva venta en el archivo JSON mediante `ArchivoServicio`.
6. **Respuesta en Interfaz:** Muestra un mensaje emergente de éxito y actualiza automáticamente la tabla `Treeview` de ventas.

---

## Estructura del Proyecto

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
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── assets/
│   └── logo.png
├── main.py
└── README.md

---

## Instrucciones de Ejecución

1. Abra la terminal en la carpeta principal del proyecto.
2. Ejecute el archivo principal con el comando:
   python main.py
3. Inicie sesión en la pantalla de login.
4. Diríjase a la pestaña **Módulo Ventas**, elija un usuario, un producto y presione **Registrar Venta**.