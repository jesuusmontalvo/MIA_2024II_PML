def calcular_serie(x, n):
    suma = 0
    for exp, k in enumerate(range(2*n+1, -1, -2)):
        factor = 1
        for i in range(2, 2*exp + 4):
            factor = 1/i * factor    
        suma += (x**k) * factor * (-1)**exp
    return suma


print(calcular_serie(1, 2))

