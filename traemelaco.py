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
    
    with open(archivo) as f:
        cant_ciudades = int( f.readline().rstrip('\n'))
        
        for i in range(cant_ciudades):
            ciudad, lat, long = f.readline().rstrip('\n').split(',')
            diccionario_coordenadas[ciudad] = [ float(lat), float(long)]
            grafo_cuidades.agregar_vertice(ciudad)
            
        cant_conecciones = int(f.readline().rstrip('\n'))
        
        for i in range(cant_conecciones):
            origen, destino, tiempo = f.readline().rstrip('\n').split(',')
            grafo.agregar_arista(origen, destino, int(tiempo) )
        
        
