def polinomio_secreto(texto):
    texto_vector = list(texto)
    raices = []
    for i in range(len(texto_vector)-1):
        s0 = texto_vector[i]
        s1 = texto_vector[i + 1]
        if s0 != s1:
            r = (2*i + 3)
            raices.append(r)
    
    coeficientes = [1] 
    for r in raices:
        coeficientes = [c - r * coef for c, coef in zip([0] + coeficientes, coeficientes + [0])]

    indice = texto_vector.index("H")
    x = 2*(indice + 1)
    if evaluar_polinomio(coeficientes[::-1], x) < 0:
        coeficientes = [-x for x in coeficientes]
        return coeficientes[::-1]
    return coeficientes[::-1]

def evaluar_polinomio(coeficientes, x):
    resultado = 0
    grado = len(coeficientes) - 1
    for coef in coeficientes:
        resultado += coef * (x ** grado)
        grado -= 1
    return resultado

print(polinomio_secreto("AHHHA"))