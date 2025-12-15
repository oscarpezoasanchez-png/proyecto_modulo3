# productos.py
"""
Modulo para gestionar productos del inventario.
Usa:
- listas de diccionarios
- tuplas para categorias
- bucles, condicionales, break, continue
"""

from utils import leer_entero, leer_flotante, leer_texto, leer_rut

# Tupla de categorias (inmutable, ejemplo de uso de tupla)
CATEGORIAS = ("Bloques", "Puzzles", "Llaveros", "Juegos", "Peluches", "Escritorio")


def mostrar_categorias():
    print("\nCategorias disponibles:")
    for i, categoria in enumerate(CATEGORIAS, start=1):
        print(f"{i}. {categoria}")


def seleccionar_categoria():
    """Permite elegir una categoria valida."""
    while True:
        mostrar_categorias()
        opcion = leer_entero("Selecciona una categoria: ", minimo=1, maximo=len(CATEGORIAS)) # leer_entero() valida que el usuario escriba un número entero, minimo=1 asegura que el usuario no escriba 0 o números negativos, maximo=len(CATEGORIAS) evita que escriba números fuera del rango.
        return CATEGORIAS[opcion - 1]


def agregar_producto(inventario):
    """
    Agrega un producto al inventario.
    inventario es una lista de diccionarios.
    """
    print("\n=== Agregar producto ===")
    producto_id = leer_entero("ID del producto (numero entero): ", minimo=1)

    # Validar que el ID no exista (uso de for + break)
    for prod in inventario:
        if prod["id"] == producto_id:
            print("Error: ya existe un producto con ese ID.")
            return  # salimos sin agregar

    nombre = leer_texto("Nombre del producto: ")
    categoria = seleccionar_categoria()
    precio = leer_flotante("Precio del producto: ", minimo=0)
    stock = leer_entero("Stock inicial: ", minimo=0)
    rut_proveedor = leer_rut("RUT del proveedor (ejemplo 12345678-5): ")

    producto = {
        "id": producto_id,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock,
        "rut_proveedor": rut_proveedor,
    }

    inventario.append(producto)
    print(f"\nProducto '{nombre}' agregado correctamente.")


def listar_productos(inventario):
    """
    Lista productos del inventario.
    Usa 'continue' para saltar productos sin stock si el usuario lo desea.
    """
    if not inventario:
        print("\nNo hay productos en el inventario.")
        return

    print("\n=== Listar productos ===")
    print("1. Ver todos")
    print("2. Ver solo productos con stock > 0")
    opcion = leer_entero("Elige una opcion: ", minimo=1, maximo=2)

    print("\nID | Nombre                | Categoria     | Precio     | Stock | RUT Proveedor")
    print("-" * 85) # "-" * 85 significa imprimir 85 guiones para crear un separador.

    for prod in inventario:
        if opcion == 2 and prod["stock"] <= 0:
            # Usamos 'continue' para saltar productos sin stock
            continue

        print(
            f"{prod['id']:2} | {prod['nombre'][:20]:20} | {prod['categoria'][:12]:12} | "
            f"${prod['precio']:9.2f} | {prod['stock']:5} | {prod['rut_proveedor']}"
        )


def buscar_producto_por_id(inventario):
    """
    Busca un producto por ID.
    Usa 'break' para salir del bucle cuando lo encuentra.
    """
    if not inventario:
        print("\nNo hay productos en el inventario.")
        return None

    print("\n=== Buscar producto por ID ===")
    buscar_id = leer_entero("Ingresa el ID del producto: ", minimo=1)

    encontrado = None
    for prod in inventario:
        if prod["id"] == buscar_id:
            encontrado = prod
            break  # ya lo encontramos, salimos del for

    if encontrado:
        print(f"\nProducto encontrado:")
        print(f"ID: {encontrado['id']}")
        print(f"Nombre: {encontrado['nombre']}")
        print(f"Categoria: {encontrado['categoria']}")
        print(f"Precio: ${encontrado['precio']:.2f}")
        print(f"Stock: {encontrado['stock']}")
        print(f"RUT proveedor: {encontrado['rut_proveedor']}")
    else:
        print("No se encontro ningun producto con ese ID.")

    return encontrado


def actualizar_stock(inventario):
    """Actualiza el stock de un producto."""
    print("\n=== Actualizar stock ===")
    producto = buscar_producto_por_id(inventario)
    if producto is None:
        return

    nuevo_stock = leer_entero("Nuevo stock: ", minimo=0)
    producto["stock"] = nuevo_stock
    print("Stock actualizado correctamente.")


def eliminar_producto(inventario):
    """Elimina un producto del inventario."""
    print("\n=== Eliminar producto ===")
    producto = buscar_producto_por_id(inventario)
    if producto is None:
        return

    inventario.remove(producto)
    print("Producto eliminado correctamente.")
