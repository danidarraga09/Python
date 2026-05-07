# ==========================================
# ALGORITMOS DE TEORÍA DE GRAFOS
# Matemáticas Discretas
# ==========================================

from collections import defaultdict, deque
import copy

# CLASE GRAFO


class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)

    def agregar_arista(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)

    def vertices(self):
        return list(self.grafo.keys())

    def grado(self, v):
        return len(self.grafo[v])

    def numero_aristas(self):
        return sum(len(x) for x in self.grafo.values()) // 2

   
    # DFS
    

    def dfs(self, v, visitados):
        visitados.add(v)

        for vecino in self.grafo[v]:
            if vecino not in visitados:
                self.dfs(vecino, visitados)

    
    # VERIFICAR SI ES CONEXO

    def es_conexo(self):
        visitados = set()

        vertices = self.vertices()

        if len(vertices) == 0:
            return True

        self.dfs(vertices[0], visitados)

        return len(visitados) == len(vertices)

   
    # COMPONENTES CONEXAS
   

    def componentes_conexas(self):
        visitados = set()
        componentes = []

        for v in self.vertices():

            if v not in visitados:

                componente = []
                cola = deque([v])
                visitados.add(v)

                while cola:
                    actual = cola.popleft()
                    componente.append(actual)

                    for vecino in self.grafo[actual]:
                        if vecino not in visitados:
                            visitados.add(vecino)
                            cola.append(vecino)

                componentes.append(componente)

        return componentes

  
    # DISTANCIAS BFS
    

    def bfs_distancias(self, inicio):

        dist = {inicio: 0}

        cola = deque([inicio])

        while cola:

            actual = cola.popleft()

            for vecino in self.grafo[actual]:

                if vecino not in dist:
                    dist[vecino] = dist[actual] + 1
                    cola.append(vecino)

        return dist

  
    # DIÁMETRO
  

    def diametro(self):

        maximo = 0

        for v in self.vertices():

            dist = self.bfs_distancias(v)

            maximo = max(maximo, max(dist.values()))

        return maximo

    # EXCENTRICIDAD
   

    def excentricidad(self, v):

        dist = self.bfs_distancias(v)

        return max(dist.values())

   
    # RADIO
    

    def radio(self):

        ex = []

        for v in self.vertices():
            ex.append(self.excentricidad(v))

        return min(ex)

   
    # CENTRO DEL GRAFO
    

    def centro(self):

        r = self.radio()

        centro = []

        for v in self.vertices():

            if self.excentricidad(v) == r:
                centro.append(v)

        return centro


    # DETECTAR PUENTE
    

    def es_puente(self, u, v):

        self.grafo[u].remove(v)
        self.grafo[v].remove(u)

        conectado = self.es_conexo()

        self.grafo[u].append(v)
        self.grafo[v].append(u)

        return not conectado


    # EULERIANO
   

    def es_euleriano(self):

        if not self.es_conexo():
            return False

        for v in self.vertices():

            if self.grado(v) % 2 != 0:
                return False

        return True

   
    # SEMI-EULERIANO
   

    def es_semi_euleriano(self):

        impares = 0

        for v in self.vertices():

            if self.grado(v) % 2 != 0:
                impares += 1

        return impares == 2

    # ALGORITMO DE FLEURY
   

    def fleury(self):

        if not self.es_euleriano():
            return "El grafo no es euleriano"

        g = copy.deepcopy(self.grafo)

        actual = self.vertices()[0]

        circuito = [actual]

        while True:

            vecinos = g[actual]

            if len(vecinos) == 0:
                break

            siguiente = None

            for v in vecinos:

                if len(vecinos) == 1:
                    siguiente = v
                    break

                temp = Grafo()
                temp.grafo = copy.deepcopy(g)

                temp.grafo[actual].remove(v)
                temp.grafo[v].remove(actual)

                if temp.es_conexo():
                    siguiente = v
                    break

            g[actual].remove(siguiente)
            g[siguiente].remove(actual)

            actual = siguiente

            circuito.append(actual)

        return circuito

   
    # ALGORITMO DE HIERHOLZER
   

    def hierholzer(self):

        if not self.es_euleriano():
            return "El grafo no es euleriano"

        g = copy.deepcopy(self.grafo)

        pila = []
        circuito = []

        actual = self.vertices()[0]

        while pila or g[actual]:

            if not g[actual]:
                circuito.append(actual)
                actual = pila.pop()

            else:
                pila.append(actual)

                vecino = g[actual].pop()

                g[vecino].remove(actual)

                actual = vecino

        circuito.append(actual)

        circuito.reverse()

        return circuito

    
    # HAMILTONIANO BACKTRACKING
   
    def hamiltoniano(self):

        n = len(self.vertices())

        vertices = self.vertices()

        inicio = vertices[0]

        camino = [inicio]

        def backtracking(v):

            if len(camino) == n:

                if inicio in self.grafo[v]:
                    camino.append(inicio)
                    return True

                return False

            for vecino in self.grafo[v]:

                if vecino not in camino:

                    camino.append(vecino)

                    if backtracking(vecino):
                        return True

                    camino.pop()

            return False

        if backtracking(inicio):
            return camino

        return "No existe ciclo hamiltoniano"


# EJEMPLO DE USO


g = Grafo()

g.agregar_arista(1, 2)
g.agregar_arista(2, 3)
g.agregar_arista(3, 4)
g.agregar_arista(4, 1)
g.agregar_arista(1, 3)
g.agregar_arista(2, 4)

print("Conexo:", g.es_conexo())

print("Componentes:", g.componentes_conexas())

print("Diámetro:", g.diametro())

print("Radio:", g.radio())

print("Centro:", g.centro())

print("Euleriano:", g.es_euleriano())

print("Circuito Fleury:", g.fleury())

print("Circuito Hierholzer:", g.hierholzer())

print("Hamiltoniano:", g.hamiltoniano())