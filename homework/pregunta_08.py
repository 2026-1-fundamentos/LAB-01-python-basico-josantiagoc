"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """

    file = "files/input/data.csv" 
    pairs_sequence = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            columns = line.strip().split("\t")

            word = columns[0]
            num = int(columns[1])

            if word:
                pairs_sequence.append((num, word))
                
    pairs_sequence = sorted(pairs_sequence)

    result = []
    for value, key in pairs_sequence:
        if result and result[-1][0] == value:    
                if key not in result[-1][1]:        
                    result[-1][1].append(key)
        else:
            result.append((value , [key]))       

    return result
print(pregunta_08())
