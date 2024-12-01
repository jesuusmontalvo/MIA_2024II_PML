def pintar_tablero(diccionario, n, m):
    # Crear el tablero de tamaño n x m con espacios en blanco
    tablero = [[' ' for _ in range(m)] for _ in range(n)]
    # Llenar el tablero con los valores del diccionario
    for (fila, columna), valor in diccionario.items():
        # Restar 1 porque las posiciones del diccionario empiezan desde 1
        tablero[fila-1][columna-1] = valor
    # Calcular el ancho de cada celda basado en el mayor contenido
    ancho_celda = max(len(str(valor)) for fila in tablero for valor in fila) + 2
    # Imprimir el tablero
    linea_horizontal = '-' * (ancho_celda * m + m - 1)  # Línea separadora
    print(linea_horizontal)
    for fila in tablero:
        print('|'.join(f'{x:^{ancho_celda}}' for x in fila))
        print(linea_horizontal)

def tablero_diagonal_ciclico(n):
    posiciones_lineal = [(i,i) for i in range(1, n*(n+1)+1)]
    numeros_a_ubicar = range(1,n*(n+1)+1)
    tabla = dict(zip(posiciones_lineal, numeros_a_ubicar))
    posiciones_y_valores = {}
    for r, valor in tabla.items():
        r = list(r)
        r[0] = n if r[0] % n == 0 else r[0] % n
        r[1] = n + 1 if r[1] % (n + 1) == 0 else r[1] % (n + 1)
        posiciones_y_valores[(r[0], r[1])] = valor
    return posiciones_y_valores

def tablero_cuadrado(posiciones_y_valores):
    cuadrado_posiciones_y_valores = {}
    for key, value in posiciones_y_valores.items():
        if key[0] < key[1]:
            cuadrado_posiciones_y_valores[(key[0], key[1] - 1)] = value
        elif key[0] > key[1]:
            cuadrado_posiciones_y_valores[(key[0], key[1])] = value
    return cuadrado_posiciones_y_valores

def n_diagonal (n):
    print(f"Tablero {n}-diagonal” con sus casillas rellenas con el número correspondiente al momento en que se visitan.")
    pintar_tablero(tablero_diagonal_ciclico(n), n, n + 1)
    print(f"Matriz cuadrada resultante de eliminar el menor elemento de cada fila del tablero “{n}-diagonal”.")
    pintar_tablero(tablero_cuadrado(tablero_diagonal_ciclico(n)), n, n)

n_diagonal(4)