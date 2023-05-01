from collections import defaultdict, deque
import networkx as nx
import matplotlib.pyplot as plt
import pprint as pp
import numpy as np


# https://algoritmosempython.com.br/cursos/algoritmos-python/algoritmos-grafos/representacao-grafos/
class Grafo(object):
    """ Implementação básica de um grafo. """

    def __init__(self, arestas, direcionado=False):
        """Inicializa as estruturas base do grafo."""
        self.adj = defaultdict(set)
        self.direcionado = direcionado
        self.adiciona_arestas(arestas)

    def get_vertices(self):
        """ Retorna a lista de vértices do grafo. """
        return list(self.adj.keys())

    def get_arestas(self):
        """ Retorna a lista de arestas do grafo. """
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]

    def adiciona_arestas(self, arestas):
        """ Adiciona arestas ao grafo. """
        for u, v in arestas:
            self.adiciona_arco(u, v)

    def adiciona_arco(self, u, v):
        """ Adiciona uma ligação (arco) entre os nodos 'u' e 'v'. """
        self.adj[u].add(v)
        # Se o grafo é não-direcionado, precisamos adicionar arcos nos dois sentidos.
        if not self.direcionado:
            self.adj[v].add(u)

    def existe_aresta(self, u, v):
        """ Existe uma aresta entre os vértices 'u' e 'v'? """
        return u in self.adj and v in self.adj[u]

    def __len__(self):
        return len(self.adj)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))

    def __getitem__(self, v):
        return self.adj[v]

    # fim da implementação da classe gerada por algoritmosempython
    def exibirGrafo(self):
        # https://networkx.org/documentation/stable/reference/generated/networkx.drawing.layout.spring_layout.html#spring-layout
        # Este método utiliza as bibliotecas networkx e matplotlib para plotar o grafo.
        G = nx.DiGraph(self.adj)
        pos = nx.spring_layout(G)  # Fruchterman-Reingold.
        nx.draw(G, pos, with_labels=True)
        plt.show()

    def posicao_vertice(self, vertice):
        for i, v in enumerate(self.adj.keys()):
            if v == vertice:
                return i
        return None

    def checaExistenciaVertices(self, v):
        if v in self.adj:
            return True
        else:
            return False

    def dfs(self, inicio, visitados=None, caminho=None):
        # depth-first search
        if visitados is None:
            visitados = []
        if caminho is None:
            caminho = []
        visitados.append(inicio)  # adiciona o vértice inicial aos visitado.
        caminho.append(inicio)  # adiciona o vértice inicial ao caminho.
        print('Método: dfs - visitados: ', visitados)
        print('Método: dfs - caminho: ', caminho)
        # print('Inicio: ', inicio, self.adj[inicio])
        for vizinho in self.adj[inicio]:
            if vizinho not in visitados:
                self.dfs(vizinho, visitados, caminho)
        return caminho

    def bfs(self, inicio):
        # breadth-first search
        visitados = set()
        fila = deque([inicio])  # começa pela raiz
        caminho = []

        while fila:
            vertice = fila.popleft()  # pega o primeiro da fila
            if vertice not in visitados:
                visitados.add(vertice)
                caminho.append(vertice)
                for vizinho in self.adj[vertice]:
                    if vizinho not in visitados:
                        fila.append(vizinho)
        return caminho

    def imprimirMatriz(self, matriz, methodName):
        n = len(self.adj)
        if isinstance(matriz, list):
            m2 = matriz
        else:
            m2 = matriz.tolist()
        col = self.get_vertices()
        m2.insert(0, col)
        for i in range(0, n + 1):
            if i == 0:
                m2[0].insert(0, '')
            else:
                m2[i].insert(0, col[i])
        print(f'Método: {methodName} - ')
        pp.pprint(m2)

    def gerarMatrizAdjacencia(self):
        n = len(self.adj)
        matriz = [[0 for j in range(n)] for i in range(n)]
        for i in self.adj:
            for j in self.adj[i]:
                matriz[i][j] = 1
        return matriz

    # Este método vai retornar a multiplicação da matriz de adjacência, sendo esta a matriz de alcançabilidade
    # que verifica se os vértices são alcançáveis com tamanho dist
    # ref: https://www.youtube.com/watch?v=5cznReL-jms&ab_channel=EdmilsonMarmoMoreira
    def gerarMatrizAlcancabilidade(self, dist):
        matrizAdj = self.gerarMatrizAdjacencia()
        matrizAlc = np.linalg.matrix_power(matrizAdj, dist)
        return matrizAlc

    def verificarAlcancabilidade(self, a, b):
        tamanho = len(self.get_vertices())
        if not self.checaExistenciaVertices(a) or not self.checaExistenciaVertices(b):
            return False, 'Os vértices não existem'
        if tamanho <= 2:
            return False
        else:
            dist = 2
            posA = self.posicao_vertice(a)
            posB = self.posicao_vertice(b)
            while True:
                MA = self.gerarMatrizAlcancabilidade(dist)
                if MA[posA][posB] == 1:
                    return dist, True
                elif dist >= tamanho:
                    return 0, 'O vértice não é alcançável'
                dist += 1
