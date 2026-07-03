"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    file = "files/input/data.csv" 
    pairs_sequence = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            columns = line.strip().split("\t")

            columna_fecha = columns[2]

            parte_mes = columna_fecha.split("-")

            mes = parte_mes[1]

            if mes:
                pairs_sequence.append((mes, 1))
                
    pairs_sequence = sorted(pairs_sequence)

    result = []
    for key, value in pairs_sequence:
        if result and result[-1][0] == key:
            result[-1] = (key, result[-1][1] + value)
        else:
            result.append((key, value)) 

    return result
print(pregunta_04())
