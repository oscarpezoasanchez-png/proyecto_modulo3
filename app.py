# app.py
"""
Sistema de gestion de inventario en Python.

Demuestra:
- Entrada/salida de datos con input() y print()
- Uso de f-strings
- Validacion de entradas (incluyendo RUT en modulo aparte)
- Condicionales if / elif / else
- Bucles while / for, con break y continue
- Funciones con parametros y valores de retorno
- Estructuras de datos: list, dict, tuple, set
- Modularizacion con varios archivos .py e import
"""

from productos import (
    agregar_producto,
    listar_productos,
    actualizar_stock,
    eliminar_producto,
)
from reportes import resumen_inventario
from carga import barra_carga # Importa la funcion barra_carga del modulo carga.py
from ventas import vender_producto, listar_ventas
from carga import barra_carga  # si ya lo estás usando




def mostrar_menu():
    print("\n==========================================")
    print("   SISTEMA DE INVENTARIO TIENDA FPR EN PY   ")
    print("===========================================")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Actualizar stock")
    print("4. Eliminar producto")
    print("5. Ver resumen de inventario")
    print("6. Vender producto")
    print("7. Listar ventas")
    print("0. Salir")
    print("===========================================")


def main():
    # Lista de productos (lista de diccionario)
    inventario = []
    ventas = []

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ").strip() # Strip Elimina espacios en blanco al inicio o final.

        if opcion == "1":
            barra_carga(duracion=5, mensaje="Cargando modulo de productos...")
            agregar_producto(inventario)
        elif opcion == "2":
            barra_carga(duracion=5, mensaje="Cargando modulo de productos...")
            listar_productos(inventario)
        elif opcion == "3":
            barra_carga(duracion=5, mensaje="Cargando modulo de productos...")
            actualizar_stock(inventario)
        elif opcion == "4":
            barra_carga(duracion=5, mensaje="Cargando modulo de productos...")
            eliminar_producto(inventario)
        elif opcion == "5":
            barra_carga(duracion=5, mensaje="Cargando modulo de productos...")
            resumen_inventario(inventario)
        elif opcion == "6":
            barra_carga(duracion=5, mensaje="Cargando modulo de ventas...")
            vender_producto(inventario, ventas)
        elif opcion == "7":
            barra_carga(duracion=5, mensaje="Cargando historial de ventas...")
            listar_ventas(ventas)
        elif opcion == "0":
            print("\nSaliendo del sistema... ¡Hasta luego!")
            break
        else:
            print("Opcion no valida. Intenta de nuevo.")

# Sirve para que el archivo app.py funcione como programa principal.
if __name__ == "__main__":
    main()
