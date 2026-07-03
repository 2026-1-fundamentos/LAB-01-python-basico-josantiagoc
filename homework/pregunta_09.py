"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    file = "files/input/data.csv" 
    pairs_sequence = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            columns = line.strip().split()

            columna_diccionario = columns[4]

            particion = columna_diccionario.split(",")

            for clave_valor in particion:

                columna_clave_valor = clave_valor.split(":")

                clave = columna_clave_valor[0]

                if clave:
                    pairs_sequence.append((clave, 1))
                
    pairs_sequence = sorted(pairs_sequence)

    result = []
    for key, value in pairs_sequence:
        if result and result[-1][0] == key:

           result[-1] = (key, result[-1][1] + value)
        else:
            result.append((key, value)) 
    diccionario = {clave: valor for clave, valor in result}        

    return diccionario
print(pregunta_09())
