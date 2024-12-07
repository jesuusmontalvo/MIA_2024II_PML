import numpy as np
def crear_matriz(texto):
    filas = [list(map(int, linea.split())) for linea in texto.strip().split("\n")]
    numero_columnas = max(len(fila) for fila in filas)
    filas_completadas = [fila + [0] * (numero_columnas - len(fila)) for fila in filas]
    matriz = np.array(filas_completadas)
    return matriz

def recorrer_matriz(matriz, fila, correos_electronicos):
    direcciones_recorrer = []
    cantidad_correos_enviados = 0
    correos_unicos = set()
    for entrada in matriz[fila, :]:
        if entrada == 0:
            break
        elif entrada not in correos_electronicos:
            entrada -= 1
            direcciones_recorrer.append(entrada)
        else:
            cantidad_correos_enviados += 1
            correos_unicos.add(entrada)
    return direcciones_recorrer, cantidad_correos_enviados, correos_unicos

def mejorando_spam(texto):
    lineas = texto.splitlines()
    numero_direcciones = list(map(int, lineas[0].split()))
    num_dir_sistema = numero_direcciones[0]
    num_dir_lista = numero_direcciones[1]
    correos_electronicos = range(num_dir_lista + 1, num_dir_sistema + 1)

    matriz_direcciones = crear_matriz(texto)
    matriz_direcciones = matriz_direcciones[1:,1:]
    direcciones_recorrer = [0]
    cantidad_correos_enviados = 0
    correos_unicos = set()
    while direcciones_recorrer:
        direcciones_faltantes = []
        for k in direcciones_recorrer:
            tupla = recorrer_matriz(matriz_direcciones, k, correos_electronicos)
            direcciones_faltantes += tupla[0]
            cantidad_correos_enviados += tupla[1]
            correos_unicos |= tupla[2]
        direcciones_recorrer = direcciones_faltantes
    return cantidad_correos_enviados, len(correos_unicos)

texto = """5 3
3 2 3 5
2 4 5
2 4 2"""
resultados = mejorando_spam(texto)
print(resultados[0], resultados[1])
