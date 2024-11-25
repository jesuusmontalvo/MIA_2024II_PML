def pintar_tablero(diccionario, n):
    tablero = [[' ' for _ in range(n+1)] for _ in range(n)]
    for (fila, columna), valor in diccionario.items():
        tablero[fila-1][columna-1] = valor
    print('-' * (4 * (n+2)-2))
    for fila in tablero:
        print(' | '.join(f'{x:2}' for x in fila))
        print('-' * (4 * (n+2) - 2))

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


pintar_tablero(tablero_diagonal_ciclico(4), 4)