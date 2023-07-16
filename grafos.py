from collections import defaultdict, deque, Counter, OrderedDict
import random

import networkx as nx
import matplotlib.pyplot as plt
import pprint as pp
import numpy as np


# https://algoritmosempython.com.br/cursos/algoritmos-python/algoritmos-grafos/representacao-grafos/

def bubblesortListaComPeso(lista):
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(0, tam - i - 1):
            if lista[j][2] > lista[j + 1][2]:  # Compara se o próx. vértice tem peso maior
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # Troca o próximo elemento com o atual
    return lista


def chavesDuplicadas(dicionario):
    contador = Counter([frozenset(chave) for chave in dicionario.keys()])
    return [list(chave) for chave, count in contador.items() if count > 1]


# Função para modificar os valores das chaves duplicadas
def modificarValoresDuplicados(dicionario):
    duplicados = chavesDuplicadas(dicionario)
    for dup in duplicados:
        valores_duplicados = [dicionario[chave] for chave in dicionario if set(chave) == set(dup)]
        for chave in dicionario:
            if set(chave) == set(dup):
                dicionario[chave] = valores_duplicados
    return dicionario


# Exibir grafo recebendo uma lista externa:
def exibirGrafo(grafo):
    G = nx.DiGraph()
    for u, vizinhos in grafo.items():
        for v, peso in vizinhos:
            G.add_edge(u, v, weight=peso)

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')

    nx.draw(G, pos, with_labels=True, arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()


class Grafo(object):
    """ Implementação básica de um grafo. """

    def __init__(self, arestas, direcionado=False):
        """Inicializa as estruturas base do grafo."""
        self.lista = arestas
        self.adj = defaultdict(set)
        self.direcionado = direcionado
        self.adiciona_arestas(arestas)
        self.lista_de_cores = ['aqua', 'red', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'gray', 'cyan',
                               'magenta', 'lime', 'teal', 'olive', 'navy', 'maroon', 'indigo', 'silver', 'gold',
                               'coral', 'orchid', 'turquoise', 'salmon', 'sienna', 'thistle', 'violet', 'wheat', 'plum',
                               'steelblue'
                               ]

    def get_vertices(self):
        """ Retorna a lista de vértices do grafo. """
        return list(self.adj.keys())

    def get_arestas(self):
        """ Retorna a lista de arestas do grafo. (Vertice1, Vertice2, Peso)"""
        arestas = []
        for vertice1, vizinhos in self.adj.items():
            for vertice2, peso in vizinhos:
                arestas.append((vertice1, vertice2, peso))
        return arestas

    def get_peso(self, vertice_origem, vertice_destino):
        for vizinho, peso in self.adj[vertice_origem]:
            if vizinho == vertice_destino:
                return peso
        return None

    def adiciona_arestas(self, arestas):
        """ Adiciona arestas ao grafo. """
        for u, v, peso in arestas:
            self.adiciona_arco(u, v, peso)

    def adiciona_arco(self, u, v, peso):
        """ Adiciona uma ligação (arco) entre os nodos 'u' e 'v' com um peso especificado. """
        self.adj[u].add((v, peso))
        # Se o grafo é não-direcionado, precisamos adicionar arcos nos dois sentidos.
        if not self.direcionado:
            self.adj[v].add((u, peso))

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
        G = nx.DiGraph()
        for u, vizinhos in self.adj.items():
            for v, peso in vizinhos:
                G.add_edge(u, v, weight=peso)

        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')  # Obtém os pesos das arestas
        labels = modificarValoresDuplicados(labels)

        nx.draw(G, pos, with_labels=True)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)  # Adiciona os pesos nas arestas
        plt.show()

    # fim da implementação da classe gerada por algoritmosempython
    def exibirGrafo(self, cores):
        G = nx.DiGraph()
        for u, vizinhos in self.adj.items():
            for v, peso in vizinhos:
                G.add_edge(u, v, weight=peso)

        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')  # Obtém os pesos das arestas
        labels = modificarValoresDuplicados(labels)
        node_colors = [cores[vertice] for vertice in G.nodes()]  # Obtém as cores dos vértices

        nx.draw(G, pos, with_labels=True, node_color=node_colors)  # Usa as cores dos vértices
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)  # Adiciona os pesos nas arestas
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
        # inicializa as listas visitados e caminho
        if visitados is None:
            visitados = []
        if caminho is None:
            caminho = []
        visitados.append(inicio)  # adiciona o vértice aos visitado.
        caminho.append(inicio)  # adiciona o vértice ao caminho.
        print('Método: dfs - visitados: ', visitados)
        print('Método: dfs - caminho: ', caminho)
        # print('Inicio: ', inicio, self.adj[inicio])
        for vizinhog in self.adj[inicio]:
            vizinho = vizinhog[0]  # Necessário para desconsiderar o peso.
            if vizinho not in visitados:
                self.dfs(vizinho, visitados, caminho)
        return caminho

    def dfs_caminho_sem_repeticao(self, inicio, fim, caminho=None):
        if caminho is None:
            caminho = []
        caminho = caminho + [inicio]
        if inicio == fim:
            return caminho
        if inicio not in self.adj:
            return None
        for verticeg in self.adj[inicio]:
            vertice = verticeg[0]  # Necessário para desconsiderar o peso.
            if vertice not in caminho:
                novo_caminho = self.dfs_caminho_sem_repeticao(vertice, fim, caminho)
                if novo_caminho:
                    return novo_caminho
        return None

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
                matriz[i][j[0]] = 1
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
            dist = 1
            posA = self.posicao_vertice(a)
            posB = self.posicao_vertice(b)
            while True:
                MA = self.gerarMatrizAlcancabilidade(dist)
                if MA[posA][posB] == 1:
                    return dist, True
                elif dist >= tamanho:
                    return 0, 'O vértice não é alcançável'
                dist += 1

    # Utilizando o algoritmo bubble sort para ordenar a lista e retornando árvore geradora ascendente
    def getKruskal(self):
        listaOrdenada = bubblesortListaComPeso(self.lista)
        print(listaOrdenada)
        visitados = []
        # print('visitados: ', visitados)
        arvore = defaultdict(set)
        qVertices = len(self.get_vertices())
        count = 0
        for i in listaOrdenada:
            if i[1] in visitados or count > qVertices:
                pass
            else:
                visitados.append(i[1])
                print(visitados)
                arvore[i[0]].add((i[1], i[2]))
            count += 1

        return arvore

    # Verifica o menor caminho usando a biblioteca networkx
    def menorCaminho(self, a, b):
        G = nx.DiGraph()
        # Declarando o grafo utilizando a biblioteca networkx
        for v1, vizinhos in self.adj.items():
            for v2, peso in vizinhos:
                G.add_edge(v1, v2, weight=peso)  # A biblioteca recebe o peso da aresta com o atributo "weight"
        return nx.shortest_path(G, a, b)

    def vgc(self):  # Retorna os vértices ordenados por grau crescente.
        graus = {}  # Dicionário para armazenar o grau de cada vértice

        # Calcular o grau de cada vértice
        for v in self.adj:
            grau = sum(len(adjacencias) for adjacencias in self.adj[v])
            graus[v] = grau

        # Ordenar os vértices com base em seus graus
        vertices_ordenados = OrderedDict(sorted(graus.items(), key=lambda x: x[1]))

        # Criar um defaultdict ordenado com o mesmo conteúdo do grafo original
        grafo_ordenado = defaultdict(set)
        for v in vertices_ordenados:
            grafo_ordenado[v] = self.adj[v]

        return grafo_ordenado

    # Retorna o conjunto maximal do grafo
    def maximal(self):
        verticesMaximais = set()
        for vertice in self.vgc():  # para cada vértice no grafo, partindo do primeiro vértice de self.adj.
            isMaximal = True
            for v in verticesMaximais:
                vizinhos_v = {vizinho for vizinho, _ in self.adj[v]}  # verifica todos os vizinhos do vertice
                print(vizinhos_v, v)
                if vertice in vizinhos_v:  # Se o vértice está entre os vizinhos, não é maximal
                    isMaximal = False
                    break
            if isMaximal:
                verticesMaximais.add(vertice)
        aux = []
        # Em casos de grafos direcionados, é necessário varrer o resultado e
        # remover os vértices que tem arestas em comum porém não foram verificados anteriormente.
        for i in tuple(verticesMaximais):
            for j in self.adj[i]:
                aux.append(j[0])
                for k in aux:
                    if k in verticesMaximais:
                        verticesMaximais.remove(k)
        return verticesMaximais

    def checarCores(self):
        cores = {}  # Dicionário para armazenar as cores atribuídas a cada vértice
        cores_disponiveis = self.lista_de_cores  # Lista de cores disponíveis

        for vertice in self.adj:  # para cada vértice no grafo
            vizinhos_cores = set()  # Conjunto de cores dos vizinhos
            print('vértice> ', vertice)
            for vizinho in self.adj[vertice]:
                if vizinho[0] in cores:  # Verifica se o vizinho já possui uma cor atribuída
                    vizinhos_cores.add(cores[vizinho[0]])
                    print('vizinho: ', vizinho[0], '\tvizinho_cores: ', vizinhos_cores, '\tcores[vizinho[0]]: '
                          , cores[vizinho[0]])

            for cor in cores_disponiveis:
                '''
                    Se a cor não está presente nos vizinhos, atribui ao vértice
                    Caso a cor não esteja nos vizinhos significa que posso adicioná-la no vértice
                '''
                if cor not in vizinhos_cores:
                    cores[vertice] = cor
                    print('cores: ', cores)
                    break

        return cores
