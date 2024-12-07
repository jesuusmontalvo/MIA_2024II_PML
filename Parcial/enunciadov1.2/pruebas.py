import numpy as np

# El texto de entrada
texto = """
1 6 
7 10 11 12 13 9 7 8
5 6 14 4 5 15
2 14 15
2 4 14
2 5 4
"""

# Paso 1: Dividir el texto en líneas y convertir cada línea en una lista de enteros
lineas = [list(map(int, linea.split())) for linea in texto.strip().split("\n")]

# Paso 2: Encontrar la longitud máxima de las filas
longitud_maxima = max(len(fila) for fila in lineas)

# Paso 3: Completar las filas más cortas con ceros
lineas_completadas = [fila + [0] * (longitud_maxima - len(fila)) for fila in lineas]

# Paso 4: Convertir a un array de NumPy
array_numpy = np.array(lineas_completadas)

print(array_numpy)