import heapq
from grafo import *

def dijkstra(grafo, origen):
    distancia = {}
    padre = {}

    for vertice in grafo:
        distancia[vertice] = 1000000 # Pongo una distancia muy grande para simular infinito

    distancia [origen] = 0
    padre[origen] = None
    heap = []
    heapq.heappush( heap, (origen, distancia[origen]) )

    while not len(heap) == 0:
        vertice, dist = heapq.heappop(heap) # Desempaqueto la tupla

        for adyacente in grafo.obtener_adyacentes(vertice):
            distancia_actual = distancia[vertice] + grafo.obtener_peso_arista(vertice, adyacente)

            if distancia_actual < distancia[adyacente]:
                padre[adyacente] = vertice
                distancia[adyacente] = distancia_actual
                heapq.heappush( heap, (w, distancia[adyacente]) )

    return padre, distancia


def camino_minimo(grafo, desde, hasta):
    padre, distancia = dijkstra(grafo, desde) # Desempaqueto la tupla
    resultado = []
    actual = hasta

    while actual != None:
        resultado.append(actual)
        actual = padre[actual]

    resultado.reverse()
    return resultado

def ir(grafo_ciudades, desde, hasta):
    camino = camino_minimo(grafo_ciudades, desde, hasta)
    largo = len(camino)

    for i in range(largo):

        if i == 0: print( "{}".format(camino[i]), end = " " )

        elif i == (largo - 1): print( "-> {}".format(camino[i]) )

        else: print( "-> {}".format(camino[i]), end = " " )

    costo_total = 0

    for i in range(largo - 1):
        costo_total += grafo.obtener_peso_arista(camino[i], camino[i + 1])

    print( "Costo total: {}".format(costo_total) )
