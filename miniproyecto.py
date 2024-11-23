import matplotlib.pyplot as plt
import networkx as nx

# Función para verificar si la relación es reflexiva
def es_reflexiva(matriz):
    for i in range(len(matriz)):
        if matriz[i][i] != 1:
            return False
    return True

# Función para verificar si la relación es simétrica
def es_simetrica(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

# Función para verificar si la relación es antisimétrica
def es_antisimetrica(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if i != j and matriz[i][j] == 1 and matriz[j][i] == 1:
                return False
    return True

# Función para verificar si la relación es transitiva
def es_transitiva(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] == 1:
                for k in range(n):
                    if matriz[j][k] == 1 and matriz[i][k] != 1:
                        return False
    return True

# Función para verificar si la relación es de equivalencia
def es_equivalencia(matriz):
    return es_reflexiva(matriz) and es_simetrica(matriz) and es_transitiva(matriz)

# Función para verificar si la relación es de orden parcial
def es_orden_parcial(matriz):
    return es_reflexiva(matriz) and es_antisimetrica(matriz) and es_transitiva(matriz)

# Función para visualizar la matriz como un grafo
def representar_grafo(matriz):
    G = nx.DiGraph()
    n = len(matriz)
    
    # Añadir los nodos al grafo
    for i in range(n):
        G.add_node(i)
    
    # Añadir las aristas
    for i in range(n):
        for j in range(n):
            if matriz[i][j] == 1:
                G.add_edge(i, j)
    
    # Dibujo del grafo
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_color='skyblue', font_weight='bold', font_size=12, node_size=3000, edge_color='gray')
    plt.title("Representación de la relación como un grafo", fontsize=14)
    plt.show()

# Función para que el usuario ingrese los datos de la matriz
def ingresar_matriz():
    n = int(input("Ingrese el tamaño de la matriz cuadrada (n): "))
    matriz = []
    
    print("Ingrese los elementos de la matriz fila por fila (0 o 1):")
    for i in range(n):
        fila = []
        for j in range(n):
            while True:
                try:
                    valor = int(input(f"Ingrese el valor para la posición [{i+1},{j+1}] (0 o 1): "))
                    if valor not in [0, 1]:
                        print("Solo se permiten valores 0 o 1. Intente de nuevo.")
                    else:
                        fila.append(valor)
                        break
                except ValueError:
                    print("Por favor ingrese un número entero válido.")
        matriz.append(fila)
    
    return matriz

# Función principal
def main():
    # Ingresar la matriz desde el usuario
    matriz = ingresar_matriz()

    # Evaluar las propiedades de la relación
    print("\nEvaluando la relación representada por la matriz:")
    
    print(f"Reflexiva: {es_reflexiva(matriz)}")
    print(f"Simétrica: {es_simetrica(matriz)}")
    print(f"Antisimétrica: {es_antisimetrica(matriz)}")
    print(f"Transitiva: {es_transitiva(matriz)}")
    print(f"De Equivalencia: {es_equivalencia(matriz)}")
    print(f"De Orden Parcial: {es_orden_parcial(matriz)}")

    # Mostrar la representación gráfica de la relación
    representar_grafo(matriz)

# Ejecutar el programa
if __name__ == "__main__":
    main()
