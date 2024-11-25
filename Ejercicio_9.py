def pasos_hexagonal(x, y, u, v):
    """
    Calcula la cantidad de pasos necesarios para ir de (x, y) a (u, v) en un panal hexagonal.
    """
    # Direcciones de movimiento en el sistema hexagonal
    movimientos = [
        (0, 1),   # Arriba
        (0, -1),  # Abajo
        (1, 1),   # Derecha y arriba
        (1, 0),   # Derecha y abajo
        (-1, 0),  # Izquierda y arriba
        (-1, -1)  # Izquierda y abajo
    ]
    
    celdas = 0
    while (x, y) != (u, v):
        mejor_movimiento = None
        menor_distancia = float('inf')
        
        # Evaluar todas las direcciones posibles
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy  # Nueva posición
            # Calcular distancia Manhattan al objetivo (u, v)
            distancia = abs(nx - u) + abs(ny - v)
            if distancia < menor_distancia:
                menor_distancia = distancia
                mejor_movimiento = (dx, dy)
        
        # Realizar el mejor movimiento
        x += mejor_movimiento[0]
        y += mejor_movimiento[1]
        celdas += 1

    return celdas + 1

# Leer los valores de entrada
x, y, u, v = map(int, input("Introduce 4 enteros (x, y, u, v) separados por espacio: ").split())
resultado = pasos_hexagonal(x, y, u, v)
print(f"Cantidad de celdas recorridas: {resultado}")