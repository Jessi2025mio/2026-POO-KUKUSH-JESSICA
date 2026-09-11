# Restaurante App - Organización Modular con Interfaz Gráfica (Semana 13)

Este proyecto corresponde a la actividad práctica de la **Semana 13** de la asignatura **Programación Orientada a Objetos**. Representa la transición de la aplicación *restaurante_app* hacia una interfaz gráfica de usuario (GUI) construida con **Tkinter**, aplicando una arquitectura modular limpia por capas.

## 📁 Estructura del Proyecto

```text
restaurante_app/
├── datos/                  # Archivos JSON de persistencia local
│   ├── productos.json
│   └── usuarios.json
├── modelos/                # Definición de entidades POO
│   ├── producto.py
│   └── usuario.py
├── servicios/              # Lógica del sistema y lectura de datos
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/                     # Componentes de la Interfaz Gráfica (Tkinter)
│   ├── login_view.py
│   └── main_view.py
├── main.py                 # Ventana principal y control del flujo
└── README.md