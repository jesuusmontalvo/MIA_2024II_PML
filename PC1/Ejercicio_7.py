def cantidad_de_vocales_diferentes_en_palabra(palabra):
    vocales = ['a', 'e', 'i', 'o', 'u']
    nuevas_palabras = []
    for vocal in vocales:
        tabla_traduccion = str.maketrans("","", f"{vocal}")
        nuevas_palabras.append(palabra.translate(tabla_traduccion))
    return sum([1 for nueva_palabra in nuevas_palabras if len(palabra) - len(nueva_palabra) >= 1])

def cantidad_palabras_con_vocales(texto):
    texto = texto.lower() #Convertimos la string a una string con letras minusculas
    abecedario_minusculas = [chr(i) for i in range(97, 123)] #Creamos lista con las letras minusculas del abecedario
    tabla_traduccion = str.maketrans("", "", "".join(abecedario_minusculas)) # Crear la tabla de traducción
    nuevo_texto = texto.translate(tabla_traduccion).split() # Aplicar la traducción y dividir string
    numeros = list(map(int, nuevo_texto))
    n = sum(numeros) % 5 + 1
    count = 0
    for palabra in texto.split():
        if cantidad_de_vocales_diferentes_en_palabra(palabra) == n:
            count += 1
    return (count, n)

def main(texto):
    resultados = cantidad_palabras_con_vocales(texto)
    print(f"Hay {resultados[0]} palabras con {resultados[1]} vocales diferentes")


texto = "Mis primos tienen casi 40 anios yo tengo 34 y tenemos que jugar pelota con gente de 18 esta bien dificil ganar"
main(texto)
