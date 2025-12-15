# ventas.py
"""
Modulo de ventas:
- Permite vender productos existentes en el inventario
- Rebaja stock
- Registra ventas con RUT del cliente
"""

from utils import leer_entero, leer_rut


def vender_producto(inventario, ventas):
    """
    Vende un producto por ID y rebaja su stock.
    Registra la venta con RUT del cliente.
    """
    if not inventario:
        print("\nNo hay productos en el inventario.")
        return

    print("\n=== Ventas ===")

    # RUT del cliente (VALIDADO)
    rut_cliente = leer_rut("RUT del cliente (ej: 12345678-5): ")

    producto_id = leer_entero("ID del producto a vender: ", minimo=1)

    producto = None
    for prod in inventario:
        if prod["id"] == producto_id:
            producto = prod
            break

    if producto is None:
        print("No existe un producto con ese ID.")
        return

    print(f"\nProducto: {producto['nombre']}")
    print(f"Stock actual: {producto['stock']}")

    if producto["stock"] <= 0:
        print("No se puede vender: stock agotado.")
        return

    cantidad = leer_entero("Cantidad a vender: ", minimo=1)

    if cantidad > producto["stock"]:
        print(f"No hay stock suficiente. Disponible: {producto['stock']}")
        return

    # Rebajar stock
    producto["stock"] -= cantidad

    total = cantidad * float(producto.get("precio", 0))

    # Registrar venta (diccionario)
    ventas.append({
        "rut_cliente": rut_cliente,
        "id_producto": producto["id"],
        "nombre_producto": producto["nombre"],
        "cantidad": cantidad,
        "total": total
    })

    print("\nVenta realizada con exito.")
    print(f"Cliente (RUT): {rut_cliente}")
    print(f"Stock restante: {producto['stock']}")
    print(f"Total venta: ${total:.2f}")


def listar_ventas(ventas):
    """Muestra el historial de ventas."""
    if not ventas:
        print("\nAun no hay ventas registradas.")
        return

    print("\n=== Historial de ventas ===")
    print("RUT Cliente | Producto              | Cant | Total")
    print("-" * 65)

    for v in ventas:
        print(
            f"{v['rut_cliente']:11} | "
            f"{v['nombre_producto'][:20]:20} | "
            f"{v['cantidad']:4} | "
            f"${v['total']:9.2f}"
        )
