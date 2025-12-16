# Documentacion Tecnica - Proyecto Modulo 3

## Descripcion del sistema
Sistema de gestion en Python para administrar inventario de productos y registrar ventas. Permite:
- Crear, listar, actualizar y eliminar productos.
- Registrar ventas rebajando stock automaticamente.
- Validar entradas (enteros, flotantes, texto) y RUT chileno (modulo 11).
- Generar reportes de resumen (incluye recursividad).

## Estructuras de datos utilizadas
- Lista (inventario): list[dict]
  - Cada producto es un diccionario con: id, nombre, categoria, precio, stock, rut_proveedor.
- Lista (ventas): list[dict]
  - Cada venta es un diccionario con: rut_cliente, id_producto, nombre_producto, cantidad, total.
- Tupla (CATEGORIAS): tuple[str]
  - Categorias fijas e inmutables.
- Set (categorias_unicas): set[str]
  - Se usa en reportes para obtener categorias sin duplicados.

## Funcionalidades implementadas
### Inventario
- Agregar producto
- Listar productos (todos / con stock)
- Actualizar stock
- Eliminar producto

### Ventas
- Venta por ID con validacion de existencia
- Validacion de stock suficiente
- Rebaja automatica del stock
- Registro de venta con RUT del cliente (validado)

### Reportes
- Resumen general
- Suma total de stock con funcion recursiva

## Modularizacion
- app.py: menu principal y flujo del programa
- productos.py: CRUD de productos
- ventas.py: logica de ventas e historial
- reportes.py: reportes del inventario
- utils.py: validaciones generales y recursividad
- rut_utils.py: validacion y normalizacion de RUT
- carga.py: barra de carga en consola

## Como ejecutar
Desde la carpeta del proyecto:
python app.py
