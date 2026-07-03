"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    file = "files\input\data.csv"
    pairs_sequence = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            columns = line.strip().split("\t")

            word = columns[0]
            num = int(columns[1])

            if word:
                pairs_sequence.append((word, num, num))
                
    pairs_sequence = sorted(pairs_sequence)

    result = []
    for key, valueMax, valueMin in pairs_sequence:
        if result and result[-1][0] == key:

            ultimoMax = result[-1][1]
            ultimoMin = result[-1][2]

            if valueMax > ultimoMax:
                max_num = valueMax
            else:
                max_num = ultimoMax

            if valueMin < ultimoMin:
                min_num = valueMin    
            else:
                min_num = ultimoMin
                
            result[-1] = (key, max_num, min_num)
        else:
            result.append((key, valueMax, valueMin)) 

    return result

print(pregunta_05())
