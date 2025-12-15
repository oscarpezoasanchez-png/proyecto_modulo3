# carga.py
import sys
import time

def barra_carga(duracion=5, longitud=30, mensaje="Cargando modulo..."):
    """
    Muestra una barra de carga en consola que dura aproximadamente 'duracion' segundos.
    - duracion: tiempo total en segundos
    - longitud: cantidad de bloques de la barra
    """
    total_pasos = longitud
    intervalo = duracion / total_pasos  # tiempo entre cada paso

    sys.stdout.write("\n" + mensaje + "\n")
    sys.stdout.flush()

    for i in range(total_pasos + 1):
        completado = "#" * i
        restante = "-" * (total_pasos - i)
        porcentaje = int((i / total_pasos) * 100)

        # \r vuelve al inicio de la linea para sobreescribirla
        sys.stdout.write(f"\r[{completado}{restante}] {porcentaje:3d}%")
        sys.stdout.flush()

        time.sleep(intervalo)

    sys.stdout.write("\n\n")
    sys.stdout.flush()
# Ejecutar la barra de carga al importar el modulo