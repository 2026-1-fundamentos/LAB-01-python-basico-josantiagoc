"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

    file = "files\input\data.csv"
    pairs_sequence = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            columns = line.strip().split()

            num = int(columns[1])

            parte_letras = columns[3].split(",")

            for letra in parte_letras:
                if letra:
                    pairs_sequence.append((letra, num))

    pairs_sequence = sorted(pairs_sequence)
    result = []
    for key, value in pairs_sequence:
        if result and result[-1][0] == key:
            suma = result[-1][1] + value
            result[-1] = (key, suma)
        else:
            result.append((key, value)) 
    diccionario = {clave: valor for clave, valor in result}        

    return diccionario                

print(pregunta_11())
