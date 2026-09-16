# Restaurante App - Semana 14 (POO)

Este proyecto corresponde a la Semana 14 de la asignatura Programación Orientada a Objetos. Evoluciona la base gráfica de restaurante_app aplicando componentes, contenedores y gestores de geometría en Tkinter/ttk, manteniendo la arquitectura modular, la separación de responsabilidades y la persistencia en archivos JSON.

---

## Estructura del Proyecto

restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md

---

## Componentes y Contenedores Utilizados

Contenedores:
- ttk.Notebook: Pestañas para separar la gestión de productos y la consulta de usuarios.
- ttk.LabelFrame: Agrupación visual del formulario, acciones e inventario.
- ttk.Frame: Organización de botones de acción y layouts.

Componentes:
- ttk.Entry / ttk.Combobox: Captura de datos en el formulario.
- ttk.Button: Vinculados mediante la propiedad command=.
- ttk.Treeview: Tabla estructurada para presentar productos y usuarios con barra de desplazamiento (ttk.Scrollbar).

---

## Operaciones de Productos Implementadas

- Registrar: Inserta un producto validando datos requeridos y precio positivo.
- Cargar/Consultar: Obtiene los datos de un producto ingresando su ID y rellena el formulario.
- Actualizar: Modifica la información del producto correspondiente al ID digitado.
- Eliminar: Remueve el producto seleccionado tras solicitar confirmación.

---

## Persistencia e Integración

Todas las validaciones y reglas de negocio son procesadas exclusivamente por RestauranteServicio. La lectura y escritura en disco de los datos se gestiona mediante ArchivoServicio hacia los archivos productos.json y usuarios.json.

---

## Instrucciones de Ejecución

1. Abrir la terminal en la raíz del proyecto.
2. Ejecutar: `python main.py`
3. Credenciales de acceso:
   - Usuario: admin
   - Contraseña: 123