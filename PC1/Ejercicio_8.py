def es_babushka_generalizada(bg):
    bg_vector = bg.split()
    while bg_vector:
        len_vector = len(bg_vector)
        if bg_vector[0] == f'-{bg_vector[-1]}' and len_vector % 2 == 0:
            """bg_vector = [abs(x) for x in list(map(int, bg_vector))]
            print(bg_vector)"""
            inicio = bg_vector[-1]
            fin = bg_vector[-1]
            bg = bg.split(inicio)[1].split(fin)[0]
            bg_vector = bg.split()
        else:
            return print(":-( intenta de nuevo.")
    return print(":-) babushkas!")


bg = "-9 -7 -1 1 -2 2 -3 -2 -1 1 2 3 7 9"
es_babushka_generalizada(bg)