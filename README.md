# 📦 Proyecto Módulo 3 – Sistema de Gestión en Python

## 👤 Autor
**Oscar Andrés Pezoa Sánchez**

---

## 🧩 Descripción del proyecto

Este proyecto corresponde al desarrollo de un **Sistema de Gestión en Python**, creado como parte del **Módulo 3** del curso.  
El sistema permite administrar un inventario de productos y registrar ventas, aplicando los principales conceptos aprendidos durante el módulo.

El programa funciona mediante un **menú interactivo en consola**, validando los datos ingresados por el usuario y gestionando la información de forma estructurada.

---

## 🎯 Objetivo del proyecto

Diseñar e implementar un sistema que permita:

- Gestionar productos de un inventario
- Registrar ventas y rebajar stock automáticamente
- Validar datos ingresados por el usuario
- Aplicar estructuras de control, funciones, recursividad y modularización

---

## ⚙️ Funcionalidades implementadas

### 📦 Gestión de Inventario
- Agregar productos
- Listar productos (todos o solo con stock)
- Actualizar stock
- Eliminar productos
- Clasificación por categorías

### 💰 Módulo de Ventas
- Venta de productos existentes
- Validación de stock disponible
- Rebaja automática del inventario
- Registro de ventas con RUT del cliente validado
- Historial de ventas

### 🧪 Validaciones
- Validación de números enteros y flotantes
- Validación de campos vacíos
- Validación de RUT chileno (algoritmo módulo 11)

### 🔄 Otros
- Barra de carga simulada al acceder a opciones del menú
- Función recursiva para el cálculo del stock total

---

## 🧠 Estructuras de datos utilizadas

- **Listas (`list`)**
  - `inventario`: almacena los productos
  - `ventas`: almacena el historial de ventas

- **Diccionarios (`dict`)**
  - Representación de productos
  - Representación de ventas

- **Tuplas (`tuple`)**
  - Categorías de productos (estructura inmutable)

- **Conjuntos (`set`)**
  - Obtención de categorías únicas en reportes

---

## 🧩 Modularización del proyecto

proyecto_modulo3/
│── app.py # Archivo principal (menú)
│── productos.py # Gestión de productos
│── ventas.py # Gestión de ventas
│── reportes.py # Resúmenes del sistema
│── utils.py # Validaciones generales y recursividad
│── rut_utils.py # Validación de RUT chileno
│── carga.py # Barra de carga
│── data_prueba.csv # Archivo de datos de prueba
│── output_prueba.txt # Salida de pruebas
│── README.md
│── docs/