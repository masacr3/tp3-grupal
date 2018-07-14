from camino_minimo import *
from orden_topologico import *
from tendido_minimo import *
from viajante import *
from constantes import *

def consola(linea, grafo_ciudades, diccionario_coordenadas):
    comando = linea.rstrip('\n')
    lista_comandos = comando.split()

    if lista_comandos[0] in TUPLA_IR_VIAJE:

        if lista_comandos[0] == IR:
            ciudad = lista_comandos[1]
            ciudad = ciudad[ : len(ciudad) - 1]
            lista_comandos[1] = ciudad

        else:
            tipo_viaje = lista_comandos[1]
            tipo_viaje = tipo_viaje[ : len(tipo_viaje) - 1]
            lista_comandos[1] = tipo_viaje

    if not es_valida(lista_comandos): return

    if lista_comandos[0] == IR: ir(grafo_ciudades, lista_comandos[1], lista_comandos[2])

    if lista_comandos[0] == VIAJE: ejecutar_viaje(lista_comandos[1])(grafo_ciudades, lista_comandos[2])

    if lista_comandos[0] == ITINERARIO: itinerario(grafo_ciudades, lista_comandos[1])

    else: reducir_caminos(grafo_ciudades, lista_comandos[1], diccionario_coordenadas)


def ejecutar_viaje(tipo_viaje):
    funciones = { OPTIMO : viaje_optimo,
                  APROXIMADO : viaje_aproximado
                  }

    return funciones[tipo_viaje]

def es_valida(lista_comandos):
    comando = lista_comandos[0]
    largo = len(lista_comandos)

    if comando == "ir" and largo != 3: return False

    if comando == "viaje" and largo != 3: return False

    if comando == "itinerario" and largo != 2: return False

    if comando == "reducir_caminos" and largo != 2: return False

    return True
