# 🍽️ Restaurante App - Gestión de Usuarios con Manejo de Eventos (Semana 16)

## 📌 Propósito de la Entrega
La versión de la **Semana 16** evoluciona el sistema `restaurante_app` incorporando un manejo robusto de eventos aplicados a la **gestión de usuarios**. Se aplican eventos virtuales, atajos de teclado y eventos de componentes Tkinter para brindar una experiencia de usuario fluida, manteniendo la arquitectura modular y la persistencia en archivos JSON.

---

## 🏗️ Arquitectura del Proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── usuario.py
│   ├── producto.py
│   └── venta.py
├── servicios/
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── login_view.py
│   └── main_view.py
├── assets/
│   └── (recursos visuales)
├── main.py
└── README.md

# 🔑 Gestión de Usuarios y Roles

Se incorpora el atributo **rol** en el modelo `Usuario` para controlar los accesos y permisos del sistema.

### 👤 Niveles de Permiso
* **`Administrador`** — Acceso completo al CRUD de usuarios, catálogo de productos y reporte de ventas.
* **`Empleado`** — Acceso operativo (Ventas y Productos). Sin permisos de administración.
* **`Cliente`** — Acceso restringido únicamente a vistas de consulta.

> 🔒 **Seguridad de Sesión:** Validación activa que impide que el administrador en sesión pueda eliminarse a sí mismo por accidente.

---

## ⚡ Eventos Implementados

| Evento                     | Tipo           | Mecanismo      | Descripción / Callback |

| **`<<TreeviewSelect>>`**   | Evento Virtual | `bind()`       | Carga los datos del usuario seleccionado desde la tabla al formulario mediante su ID.      |
| **`<Return>`**             | Teclado        | `bind()`       | Atajo de teclado para confirmar y registrar al usuario.                                    |
| **`<Escape>`**             | Teclado        | `bind()`       | Atajo para limpiar el formulario y deseleccionar elementos en la tabla.                    |
| **`<<ComboboxSelected>>`** | Evento Virtual | `bind()`       | Detecta y responde al cambio de rol en el formulario en tiempo real.                       |
| **`Button Click`**         | Acción UI      | `command=`     | Ejecuta directamente las acciones CRUD (*Registrar*, *Actualizar*, *Eliminar*, *Limpiar*). |


## 🔄 Diferencia Técnica: `command=` vs `bind()`

🔘 **`command=`**
  Propiedad exclusiva de botones (`ttk.Button`). Se utiliza únicamente para vincular la acción del clic directo sobre el botón.

⚙️ **`bind()`**
  Método flexible de Tkinter para vincular cualquier evento del sistema (teclas, ratón, selecciones) con una función *callback*, sin depender de un botón.