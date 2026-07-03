"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    ruta = "files\input\data.csv"
    suma = 0
    with open(ruta, mode="r", encoding="utf-8") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")

            suma += int(columnas[1])
    return suma

print(pregunta_01())    

