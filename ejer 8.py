from collections import Counter
from heapq import heappush, heappop

simbolos=["A","F","1","3","0","M","T"]
frecuencias=[0.2,0.17,0.13,0.21,0.05,0.09,0.15]

def AH (simbolos, frecuencias):
    frecuencias= list(zip(simbolos,frecuencias))
    lista_nodos= []
    for simbolos, frecuencia in lista_frecuencias:
        heappush(lista_nodos,(frecuencia,len(lista_nodos),simbolos))
        