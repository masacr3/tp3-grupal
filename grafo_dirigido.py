import random

class GrafoDirido:
    def __init__(self):
        self.vertices = {}
        self.cantidad = 0

    def agregar_vertice(self, vertice):
        self.vertices[vertice] = {}
        self.cantidad +=1

    def agregar_arista(self, origen, destino, peso = 1):

        if origen not in self.vertices: return False

        adyacentes_origen = self.vertices[origen]
        adyacentes_origen[destino] = peso
        return True

    def borrar_vertice(self, vertice):

        if vertice not in self.vertices: return None

        for vertices in self.verices:
            adyacetes = self.vertices[vertices]

            if vertice in adyacetes:
                adyacetes.pop(vertice)
                break

        self.cantidad -= 1
        return self.vertices.pop(vertice)

    def borrar_arista(self, origen, destino):

        if origen not in self.vertices: return None

        adyacentes_origen = self.vertices[origen]

        if destino not in adyacentes_origen: return None

        peso = adyacentes_origen.pop(destino)
        return (origen, destino, peso)

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

        if adyacente not in adyacentes_vertice: return -1

        return adyacentes_vertice[adyacente]

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
