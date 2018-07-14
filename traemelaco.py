import sys
from grafo import *
from consola import *

def main():
    
    if len(sys.argv) != 3: sys.exit(0)

    grafo_ciudades = Grafo(False)
    diccionario_coordenadas = {}
    cargar_datos(grafo_ciudades, sys.argv[1], diccionario_coordenadas)

    for linea in sys.stdin:
        consola(linea, grafo_ciudades, diccionario_coordenadas)

def cargar_datos(grafo_ciudades, archivo, diccionario_coordenadas):
    division_archivo = 0

    with open(archivo) as archivo_entrada:

        for linea in archivo_entrada:
            lista_linea = linea.rstrip('\n').split(',')

            if len(lista_linea) == 1 and division_archivo == 0:
                diccionario_coordenadas["ciudades"] = int( lista_linea[0] )
                division_archivo += 1
                continue

            if len(lista_linea) == 1 and division_archivo == 1:
                division_archivo += 1
                continue

            if division_archivo == 1:
                ciudad, latitud, longitud = lista_linea
                lista_coordenadas = []
                lista_coordenadas.append( float(latitud) )
                lista_coordenadas.append( float(longitud) )
                diccionario_coordenadas[ciudad] = lista_coordenadas
                grafo_ciudades.agregar_vertice(ciudad)
                continue

            origen, destino, tiempo = lista_linea
            grafo.agregar_arista(origen, destino, int(tiempo) )
