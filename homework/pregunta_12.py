"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    file = "files/input/data.csv" 
    pairs_sequence = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            columns = line.strip().split()

            word = columns[0]

            parte_diccionario = columns[4].split(",")

            for clave_valor in parte_diccionario:

                columna_clave_valor = clave_valor.split(":")

                valor = int(columna_clave_valor[1])

                if valor:
                    pairs_sequence.append((word, valor))
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
print(pregunta_12())                
