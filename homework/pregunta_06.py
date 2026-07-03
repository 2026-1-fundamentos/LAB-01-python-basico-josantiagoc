"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

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
                valor = int(columna_clave_valor[1])

                if clave:
                    pairs_sequence.append((clave, valor, valor))
                
    pairs_sequence = sorted(pairs_sequence)

    result = []
    for key, valueMin, valueMax in pairs_sequence:
        if result and result[-1][0] == key:

            ultimoMin = result[-1][1]
            ultimoMax = result[-1][2]

            if valueMax > ultimoMax:
                max_num = valueMax
            else:
                max_num = ultimoMax

            if valueMin < ultimoMin:
                min_num = valueMin    
            else:
                min_num = ultimoMin
                
            result[-1] = (key, min_num, max_num)
        else:
            result.append((key, valueMin, valueMax)) 

    return result
print(pregunta_06()) 
