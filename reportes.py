# reportes.py
"""
Modulo para generar reportes del inventario.
Usa:
- sets para categorias unicas
- funciones
- funcion recursiva (importada desde utils)
"""

from utils import sumar_stock_recursivo


def resumen_inventario(inventario):
    """Muestra un resumen general del inventario."""
    print("\n=== Resumen de inventario ===")

    total_productos = len(inventario)
    categorias_unicas = set()  # uso de set para evitar duplicados

    for prod in inventario:
        categorias_unicas.add(prod["categoria"])

    stock_total = sumar_stock_recursivo(inventario)  # funcion RECURSIVA

    print(f"Cantidad de productos registrados: {total_productos}")
    print(f"Categorias distintas: {', '.join(categorias_unicas) if categorias_unicas else 'Ninguna'}") # Join une los elementos del set en una cadena separada por comas.
    print(f"Stock total sumado (recursivo): {stock_total}")
