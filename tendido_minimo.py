import heapq
from grafo import *

def arbol_tendido_minimo(grafo):
    inicio = grafo.obtener_vertice_aleatorio()
    visitados = set()
    visitados.add(inicio)
    heap = []

    for adyacente in grafo.obtener_adyacentes(inicio):
        heapq.heappush( heap, (inicio, adyacente, grafo.obtener_peso_arista(inicio, adyacente)) )

    arbol = Grafo(False)

    for vertice in grafo: arbol.agregar_vertice(vertice)

    while not len(heap) == 0:
        vertice, adyacente, peso = heapq.heappop(heap)

        if adyacente in visitados: continue

        arbol.agregar_arista(vertice, adyacente, grafo.obtener_peso_arista(vertice, adyacente))
        visitados.add(adyacente)

        for w in grafo.obtener_adyacentes(adyacente):
            heapq.heappush( heap, (adyacente, w, grafo.obtener_peso_arista(adyacente, w)) )

    return arbol

def reducir_caminos(grafo_ciudades, archivo, diccionario_coordenadas):
    arbol = arbol_tendido_minimo(grafo_ciudades)
    costo_total = 0
    visitados = set()

    with open(archivo, "w") as archivo_salida:
        archivo_salida.write( "{}\n".format(diccionario_coordenadas["ciudades"]) )

        for ciudad in diccionario_coordenadas:
            lista_coordenadas = diccionario_coordenadas[ciudad]
            latitud = lista_coordenadas[0]
            longitud = lista_coordenadas[1]
            archivo_salida.write( "{},{},{}\n".format(ciudad, latitud, longitud) )

        cantidad_aristas = obtener_cantidad_vertices(grafo_ciudades) - 1
        archivo_salida.write( "{}\n".format(cantidad_aristas) )

        for vertice in arbol:

            for adyacente in arbol.obtener_adyacentes(vertice):

                if adyacente not in visitados:
                    visitados.add(adyacente)
                    peso_arista = arbol.obtener_peso_arista(vertice, adyacente)
                    costo_total += peso_arista
                    archivo_salida.write( "{},{},{}\n".format(vertice, adyacente, peso_arista) )

    print( "Costo total: {}".format(costo_total) )
