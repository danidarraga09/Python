from collections import defaultdict, deque

class Grafo:

    def __init__(self):
        self.grafo = defaultdict(list)

    def agregar_arista(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)

    def eliminar_arista(self, u, v):
        if v in self.grafo[u]:
            self.grafo[u].remove(v)
        if u in self.grafo[v]:
            self.grafo[v].remove(u)

    def vertices(self):
        return list(self.grafo.keys())

    def grado(self, v):
        return len(self.grafo[v])

    def numero_aristas(self):
        return sum(len(x) for x in self.grafo.values()) // 2

    def dfs(self, v, visitados):
        visitados.add(v)
        for vecino in self.grafo[v]:
            if vecino not in visitados:
                self.dfs(vecino, visitados)

    def es_conexo(self):
        vertices = self.vertices()
        if len(vertices) == 0:
            return True
        visitados = set()
        self.dfs(vertices[0], visitados)
        return len(visitados) == len(vertices)

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

    def diametro(self):
        maximo = 0
        for v in self.vertices():
            dist = self.bfs_distancias(v)
            maximo = max(maximo, max(dist.values()))
        return maximo

    def excentricidad(self, v):
        dist = self.bfs_distancias(v)
        return max(dist.values())

    def radio(self):
        return min(self.excentricidad(v) for v in self.vertices())

    def centro(self):
        r = self.radio()
        return [v for v in self.vertices() if self.excentricidad(v) == r]

    def es_puente(self, u, v):
        if len(self.grafo[u]) == 1:
            return False
        visitados = set()
        self.dfs(u, visitados)
        antes = len(visitados)
        self.eliminar_arista(u, v)
        visitados = set()
        self.dfs(u, visitados)
        despues = len(visitados)
        self.agregar_arista(u, v)
        return despues < antes

    def es_euleriano(self):
        if not self.es_conexo():
            return False
        for v in self.vertices():
            if self.grado(v) % 2 != 0:
                return False
        return True

    def es_semi_euleriano(self):
        impares = sum(1 for v in self.vertices() if self.grado(v) % 2 != 0)
        return impares == 2

    def fleury(self):
        if not self.es_euleriano():
            print("El grafo no es euleriano.")
            return
        copia = defaultdict(list)
        for v in self.grafo:
            copia[v] = self.grafo[v][:]
        actual = next(iter(self.grafo))
        circuito = [actual]
        while self.numero_aristas() > 0:
            vecinos = self.grafo[actual][:]
            for vecino in vecinos:
                if not self.es_puente(actual, vecino):
                    self.eliminar_arista(actual, vecino)
                    actual = vecino
                    circuito.append(actual)
                    break
        self.grafo = copia
        print("Circuito Euleriano:")
        print(" -> ".join(map(str, circuito)))

   #KAUMANN
    def kaufmann_malgrange(self):
        vertices = self.vertices()
        n = len(vertices)

        # ==========================
        # MATRIZ H¹
        # ==========================
        H = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                u = vertices[i]
                v = vertices[j]
                if v in self.grafo[u]:
                    H[i][j] = [u, v]

        print("\nMatriz H¹:")
        self.imprimir_matriz(H)

        Hr = H

        # ==========================
        # MULTIPLICACIÓN LATINA
        # ==========================
        for r in range(1, n - 1):
            nueva = [[None for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    caminos = []
                    for k in range(n):
                        if Hr[i][k] and H[k][j]:
                            for camino1 in (Hr[i][k] if isinstance(Hr[i][k][0], list) else [Hr[i][k]]):
                                for camino2 in (H[k][j] if isinstance(H[k][j][0], list) else [H[k][j]]):
                                    usados = set(camino1)
                                    valido = True
                                    for vertice in camino2[1:]:
                                        if vertice in usados:
                                            valido = False
                                            break
                                    if valido:
                                        nuevo = camino1 + camino2[1:]
                                        caminos.append(nuevo)
                    if caminos:
                        nueva[i][j] = caminos
            Hr = nueva
            print(f"\nMatriz H^{r+1}:")
            self.imprimir_matriz(Hr)

        # ==========================
        # CAMINOS HAMILTONIANOS
        # ==========================
        print("\nCaminos Hamiltonianos:")
        encontrado = False
        for i in range(n):
            for j in range(n):
                if Hr[i][j]:
                    for camino in Hr[i][j]:
                        if len(camino) == n:  # condición de Hamiltoniano
                            print(f"{vertices[i]} -> {vertices[j]} : {camino}")
                            encontrado = True
        if not encontrado:
            print("No existen caminos Hamiltonianos.")
    
    def imprimir_matriz(self, M):
        for fila in M:
            print(fila)



# ==========================================
# EJEMPLO DE USO
# ==========================================

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
print("Semi-Euleriano:", g.es_semi_euleriano())

g.kaufmann_malgrange()
g.fleury()




