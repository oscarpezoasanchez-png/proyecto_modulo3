# utils.py
"""
Modulo de utilidades:
- Validacion de entradas (enteros, flotantes, texto)
- Funciones recursivas
- Lectura validada de RUT (usando rut_utils)
"""

from rut_utils import es_rut_valido, normalizar_rut


def leer_entero(mensaje, minimo=None, maximo=None):
    """Lee un entero validado desde teclado."""
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"Error: el valor debe ser >= {minimo}")
                continue
            if maximo is not None and valor > maximo:
                print(f"Error: el valor debe ser <= {maximo}")
                continue
            return valor
        except ValueError:
            print("Error: debes ingresar un numero entero valido.")


def leer_flotante(mensaje, minimo=None, maximo=None):
    """Lee un flotante validado desde teclado."""
    while True:
        try:
            valor = float(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"Error: el valor debe ser >= {minimo}")
                continue
            if maximo is not None and valor > maximo:
                print(f"Error: el valor debe ser <= {maximo}")
                continue
            return valor
        except ValueError:
            print("Error: debes ingresar un numero valido (puede tener decimales).")


def leer_texto(mensaje):
    """Lee un texto no vacio."""
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("Error: el texto no puede estar vacio.")
        else:
            return texto


def leer_rut(mensaje):
    """
    Lee un RUT desde teclado y lo valida usando el modulo rut_utils.
    Devuelve el RUT normalizado (sin puntos, con guion).
    """
    while True:
        rut = input(mensaje).strip()
        if not es_rut_valido(rut):
            print("RUT no valido. Intenta de nuevo (ejemplo: 12345678-5).")
            continue
        return normalizar_rut(rut)


# Funcion recursiva de ejemplo:
def sumar_stock_recursivo(lista_productos, indice=0):
    """
    Suma el stock total de forma RECURSIVA.
    Caso base: si el indice llega al final de la lista, retorna 0.
    Caso recursivo: stock del producto actual + llamada recursiva al siguiente.
    """
    if indice >= len(lista_productos):
        return 0
    return lista_productos[indice]["stock"] + sumar_stock_recursivo(lista_productos, indice + 1)
