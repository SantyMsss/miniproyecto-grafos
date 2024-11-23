# Verificación de Propiedades de Relaciones Representadas en Matrices

Este programa, desarrollado en Python, permite a los usuarios ingresar una matriz cuadrada de ceros y unos que representa una relación sobre un conjunto de elementos. El programa evalúa las propiedades de la relación y las representa gráficamente como un grafo.

## **Funcionalidades**

1. **Ingreso de Matriz**:
   - El usuario puede ingresar una matriz cuadrada de tamaño `n x n` (donde `n` es un número entero positivo).
   - Solo se permiten valores `0` y `1` en la matriz.

2. **Propiedades Evaluadas**:
   - **Reflexiva**: Verifica si todos los elementos de la diagonal principal son iguales a 1.
   - **Simétrica**: Comprueba si la matriz es simétrica respecto a la diagonal principal.
   - **Antisimétrica**: Evalúa si para cada par de elementos `(i, j)` y `(j, i)`, no ambos son iguales a 1.
   - **Transitiva**: Verifica si la relación cumple la propiedad transitiva.
   - **Relación de Equivalencia**: Determina si la relación es reflexiva, simétrica y transitiva simultáneamente.
   - **Relación de Orden Parcial**: Determina si la relación es reflexiva, antisimétrica y transitiva.

3. **Visualización Gráfica**:
   - Representa gráficamente la relación como un grafo dirigido utilizando las librerías `networkx` y `matplotlib`.

4. **Impresión de Resultados**:
   - Muestra la matriz ingresada y evalúa cada propiedad con un resultado booleano (`True` o `False`).
   - Incluye una línea de crédito con el autor y el código.

## **Requisitos**

### **Librerías necesarias**
El programa utiliza las siguientes librerías de Python. Si no las tienes instaladas, puedes hacerlo ejecutando:
```bash
pip install networkx matplotlib


