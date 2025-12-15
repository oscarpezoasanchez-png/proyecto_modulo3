# rut_utils.py
"""
Modulo para trabajar con RUT chileno:
- Limpiar RUT (quitar puntos y guiones)
- Validar RUT (es_rut_valido)
- Normalizar RUT (cuerpo-DV)
"""

def limpiar_rut(rut: str) -> str:
    """Elimina puntos y guion, y deja el RUT en mayusculas sin espacios."""
    return rut.replace(".", "").replace("-", "").strip().upper()


def es_rut_valido(rut: str) -> bool:
    """Valida el RUT chileno usando el algoritmo del modulo 11."""
    rut_limpio = limpiar_rut(rut)

    # Debe tener al menos 2 caracteres: cuerpo + DV
    if len(rut_limpio) < 2:
        return False

    cuerpo = rut_limpio[:-1]
    dv_ingresado = rut_limpio[-1]

    # El cuerpo deben ser solo digitos
    if not cuerpo.isdigit():
        return False

    # Calculo del DV
    reverso = map(int, reversed(cuerpo))
    factores = [2, 3, 4, 5, 6, 7]
    suma = 0
    i = 0

    for d in reverso:
        suma += d * factores[i % len(factores)]
        i += 1

    resto = suma % 11
    dv_calculado_num = 11 - resto

    if dv_calculado_num == 11:
        dv_calculado = "0"
    elif dv_calculado_num == 10:
        dv_calculado = "K"
    else:
        dv_calculado = str(dv_calculado_num)

    return dv_ingresado == dv_calculado


def normalizar_rut(rut: str) -> str:
    """
    Deja el RUT en formato estandar: cuerpo-DV (sin puntos).
    Ejemplo: '12.345.678-5' -> '12345678-5'
    """
    rut_limpio = limpiar_rut(rut)
    cuerpo = rut_limpio[:-1]
    dv = rut_limpio[-1]
    return f"{cuerpo}-{dv}"
