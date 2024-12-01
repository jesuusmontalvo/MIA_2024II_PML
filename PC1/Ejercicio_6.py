import numpy as np

def posibles_valores_sudoku(texto):
    # Convertir el texto a una matriz NumPy
    matriz = np.array([[int(digito) for digito in linea] for linea in texto.splitlines()])
    #Encontrar donde están todos los ceros
    posicion_ceros = np.where(matriz == 0)
    posicion_ceros = list(zip(posicion_ceros[0], posicion_ceros[1]))

    for posicion in posicion_ceros:
        valores_posibles = set(range(1,10))
        if posicion[0] in range(3):
            if posicion[1] in range(3):
                valores_posibles = valores_posibles.difference(set(matriz[:3, :3].flatten()))
            elif posicion[1] in range(3,6):
                valores_posibles = valores_posibles.difference(set(matriz[:3, 3:6].flatten()))
            elif posicion[1] in range(6,9):
                valores_posibles = valores_posibles.difference(set(matriz[:3, 6:9].flatten()))

            valores_posibles = valores_posibles.difference(set(matriz[posicion[0], :].flatten()))
            valores_posibles = valores_posibles.difference(set(matriz[:, posicion[1]].flatten()))
            print(f"Casillero {(posicion[0] + 1, posicion[1] + 1)} valores posibles: ", valores_posibles)
        elif posicion[0] in range(3,6):
            if posicion[1] in range(3):
                valores_posibles = valores_posibles.difference(set(matriz[3:6, :3].flatten()))
            elif posicion[1] in range(3,6):
                valores_posibles = valores_posibles.difference(set(matriz[3:6, 3:6].flatten()))
            elif posicion[1] in range(6,9):
                valores_posibles = valores_posibles.difference(set(matriz[3:6, 6:9].flatten()))
            
            valores_posibles = valores_posibles.difference(set(matriz[posicion[0], :].flatten()))
            valores_posibles = valores_posibles.difference(set(matriz[:, posicion[1]].flatten()))
            print(f"Casillero {(posicion[0] + 1, posicion[1] + 1)} valores posibles: ", valores_posibles)
        elif posicion[0] in range(6,9):
            if posicion[1] in range(3):
                valores_posibles = valores_posibles.difference(set(matriz[6:9, :3].flatten()))
            elif posicion[1] in range(3,6):
                valores_posibles = valores_posibles.difference(set(matriz[6:9, 3:6].flatten()))
            elif posicion[1] in range(6,9):
                valores_posibles = valores_posibles.difference(set(matriz[6:9, 6:9].flatten()))

            valores_posibles = valores_posibles.difference(set(matriz[posicion[0], :].flatten()))
            valores_posibles = valores_posibles.difference(set(matriz[:, posicion[1]].flatten()))
            print(f"Casillero {(posicion[0] + 1, posicion[1] + 1)} valores posibles: ", valores_posibles)

texto = """530070001
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079"""

posibles_valores_sudoku(texto)
