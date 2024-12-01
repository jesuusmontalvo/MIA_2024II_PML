def sumas_de_subconjuntos(lista_numeros):
    n = len(lista_numeros)
    binarios = [[(i >> bit) & 1 for bit in range(n - 1, -1, -1)] for i in range(2**n)] #Lista de todas los vectores binarios de n coordenadas
    sumas = []
    for binario in binarios[1:]:
        suma = 0
        for k in range(0,n):
            suma += binario[k]*numeros[k]
        sumas.append(suma)
    return set(sumas)

numeros = [6, 2, 3, 1]
print(sumas_de_subconjuntos(numeros))