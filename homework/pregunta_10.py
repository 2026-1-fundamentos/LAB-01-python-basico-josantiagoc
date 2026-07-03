"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

    file = "files/input/data.csv" 
    pairs_sequence = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            columns = line.strip().split()

            word = columns[0]

            parte_letras = len(columns[3].split(","))

            parte_diccionario = len(columns[4].split(","))

            if word:
                pairs_sequence.append((word, parte_letras, parte_diccionario))
            
    return pairs_sequence

print(pregunta_10())
