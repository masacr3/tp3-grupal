import random

class Grafo:
    def __init__(self, es_dirigido = True):
        self.vertices = {}
        self.cantidad = 0
        self.es_dirigido = es_dirigido

    def agregar_vertice(self, vertice):
        self.vertices[vertice] = {} # en este diccionario van a ir los adyacentes a vertice con el peso de la arista
        self.cantidad +=1

    def agregar_arista(self, vertice, adyacente, peso = 1):

        if vertice not in self.vertices: return False

        if not self.es_dirigido: # si el grafo no es dirigido hago lo sig.

            if adyacente not in self.vertices: return False

            adyacentes_adyacente = self.vertices[adyacente]
            adyacentes_adyacente[vertice] = peso # agrego el conjugado

        adyacentes_vertice = self.vertices[vertice]
        adyacentes_vertice[adyacente] = peso # agrego el adyacente con su peso y se formo la arista
        return True

    def borrar_vertice(self, vertice):

        if vertice not in self.vertices: return None

        for vertices in self.verices: # itero para ver si el vertice es adyacente de algun otro vertice y lo borro
            adyacentes = self.vertices[vertices]

            if vertice in adyacentes:
                adyacentes.pop(vertice)

        self.cantidad -= 1
        return self.vertices.pop(vertice)

    def borrar_arista(self, vertice, adyacente):

        if vertice not in self.vertices: return None

        adyacentes_vertice = self.vertices[vertice]

        if adyacente not in adyacentes_vertice: return None

        if not self.es_dirigido: # si el grafo no es dirigido hago lo sig.

            if adyacente not in self.vertices: return None

            adyacentes_adyacente = self.vertices[adyacente]

            if vertice not in adyacentes_adyacente: return None

            adyacentes_adyacente.pop(vertice) # borro el conjugado

        peso = adyacentes_vertice.pop(adyacente) # borro el adyacente y devulevo el peso de la arista
        return peso

    def esta_en_grafo(self, vertice):
        return vertice in self.vertices

    def estan_conectados(self, vertice1, vertice2):

        if vertice1 not in self.vertices: return False

        adyacentes_vertice1 = self.vertices[vertice1]

        if vertice2 not in adyacentes_vertice1: return False

        return True

    def obtener_peso_arista(self, vertice, adyacente):

        if vertice not in self.vertices: return -1

        adyacentes_vertice = self.vertices[vertice]
        return adyacentes_vertice.get(adyacente, -1)

    def obtener_todos_los_vertices(self):
        vertices = self.vertices
        return list(vertices)

    def obtener_vertice_aleatorio(self):
        verices = self.vertices
        lista_vertices = list(vertices)
        return random.choice(lista_vertices)

    def obtener_adyacentes(self, vertice):

        if vertice not in self.vertices: return None

        adyacentes_vertice = self.vertices[vertice]
        return list(adyacentes_vertice)

    def obtener_cantidad_vertices(self):
        return self.cantidad

    def __iter__(self):
        return iter(self.vertices)
