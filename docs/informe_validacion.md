# Informe de Validacion - Proyecto Modulo 3

## 1. Entorno de desarrollo
- SO: Windows
- IDE: Visual Studio Code
- Version Git: 2.52.0.windows.1
- Lenguaje: Python 3.x

## 2. Evidencia de estructura modular
![alt text](image.png)

## 3. Evidencia de ejecucion
### 3.1 Menu principal
![alt text](image-1.png)

### 3.2 Validaciones de entrada
- Caso: ingreso de texto cuando se espera entero (leer_entero)
![alt text](image-2.png)
- Caso: RUT invalido y reintento (leer_rut)
![alt text](image-3.png)

### 3.3 Flujo de inventario
- Agregar producto
![alt text](image-4.png)
- Listar productos
![alt text](image-5.png)
- Eliminar producto
![alt text](image-6.png)


### 3.4 Flujo de ventas
- Venta con stock suficiente (rebaja correcta)
![alt text](image-7.png)
- Venta con stock insuficiente (bloqueo)
![alt text](image-8.png)

### 3.5 Reporte / recursividad
- Resumen inventario (stock total recursivo)
![alt text](image-9.png)

## 4. Analisis de desafios y soluciones
- Importaciones de modulos: solucion mediante ejecucion desde carpeta raiz y estructura correcta.
- Validacion de datos: funciones reutilizables en utils.py con try/except.
- Control de stock: validacion previa antes de rebajar y registro en historial.
- RUT: modulo independiente rut_utils.py con algoritmo modulo 11.

## 5. Conclusiones
El sistema cumple los requerimientos del modulo: control de flujo, modularizacion, estructuras de datos, validaciones y recursividad.
