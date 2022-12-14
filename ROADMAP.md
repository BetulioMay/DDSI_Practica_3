# ROADMAP

### Conexion

- Conexión con base de datos: <strong>HECHO</strong>
  - `src/connection.py:connect()`.

### Funcionalidad

- Creación de nueva tabla STOCK con 10 tuplas predefinidas en el código: <strong>HECHO</strong>
- Borrar tabla STOCK: <strong>HECHO</strong>
- Dar de alta nuevo pedido: <strong>HECHO</strong>
  - `src/transactions/register_order.py`
- Mostrar el contenido de las tablas de la BD. <strong>HECHO</strong>
  - `src/transactions/show_tables.py`
- Salir del programa y cerrar conexión con la BD: <strong>HECHO</strong>
  - Implementado el cierre de conexión: `src/connection.py:close_connection()`

### Interfaz

> NOTA: Todas las interfaces se encuentran en `src/interfaces`.

- Main loop: <strong>HECHO</strong>
- Dar de alta al cliente (interfaz): <strong>HECHO</strong>
  - `src/interfaces/order.py`|`src/interfaces/detail_order.py`
