from cola import *
from grafo import *

def orden_topologico(grafo):
    grados = {}

    for vertice in grafo:
        grados[vertice] = 0

    for vertice in grafo:

        for adyacente in grafo.obtener_adyacentes(vertice):
            grados[adyacente] += 1

    resultado = []
    cola = Cola()

    for vertice in grafo:

        if grados[vertice] == 0: cola.encolar(vertice)

    while not cola.esta_vacia():
        vertice = cola.desencolar()
        resultado.append(vertice)

        for adyacente in grafo.obtener_adyacentes(vertice):
            grados[adyacente] -= 1

            if grados[adyacente] == 0: cola.encolar(adyacente)

    return None if len(resultado) == 0 else resultado

def itinerario(grafo_ciudades, archivo):
    grafo = Grafo()

    for vertice in grafo_ciudades:
        grafo.agregar_vertice(vertice)

    with open(archivo) as archivo_entrada:

        for linea in archivo_entrada:
            vertice, adyacente = linea.rstrip('\n').split(',')
            grafo.agregar_arista(vertice, adyacente)

    lista_orden_topologico = orden_topologico(grafo)
    largo = len(lista_orden_topologico)

    for i in range(largo):

        if i == 0: print( "{}".format(camino[i]), end = " " )

        elif i == (largo - 1): print( "-> {}".format(camino[i]) )

        else: print( "-> {}".format(camino[i]), end = " " )

    costo_total = 0

    for i in range(largo - 1):
        costo_total += grafo.obtener_peso_arista(camino[i], camino[i + 1])

    print( "Costo total: {}".format(costo_total) )
