from grafos import Grafo, exibirGrafo


def main():
    # https://algoritmosempython.com.br/cursos/algoritmos-python/algoritmos-grafos/representacao-grafos/
    """
        arestas = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'B'), ('C', 'E'), ('D', 'A'), ('E', 'B')]
        # Cria e imprime o grafo.
        grafo = Grafo(arestas, direcionado=True)
        print('Grafo: ', grafo.adj)
        print('Vértices: ', grafo.get_vertices())
        print('Arestas: ', grafo.get_arestas())
        print('Existe aresta - A, B: ', grafo.existe_aresta('A', 'B'), '\n \t \t \t \t E, C: ', grafo.existe_aresta('E', 'C'))
        # fim da implementação da classe gerada por algoritmosempython
        caminhoAdfs = grafo.dfs('A')
        print('Passeio completo a partir de A utilizando o método dfs: ', caminhoAdfs, '\n --------------------')
        # caminhoAbfs = grafo.bfs('A')
        # print('Passeio completo a partir de A utilizando o método bfs: ', caminhoAbfs, '\n ---------------------')
        grafo.exibirGrafo()
    """

    # arestas = [(0, 1), (1, 3), (3, 0), (1, 2), (2, 1), (2, 4), (4, 1), (5, 0)]  # define as arestas
    # arestas = [(1, 2), (2, 3), (2, 4), (2, 5), (2, 1), (5, 2), (3, 2), (4, 2)]  # define as arestas
    arestas = [(0, 1, 2), (1, 2, 3), (1, 3, 1), (3, 0, 4), (2, 1, 5), (2, 4, 2), (4, 1, 3), (5, 0, 1), (6, 3, 1), (3, 6, 2), (6, 1, 2), (1,6,1)]  # Define restas com peso
    grafo = Grafo(arestas, direcionado=True)  # cria o grafo e informa se é direcionado ou não
    print('Grafo: ', grafo.adj)  # exibe o grafo em forma de lista de adjacências
    # print('Arestas: (Vértice 1, Vértice 2, Peso)', grafo.get_arestas())  # Exibe arestas do grafo
    '''
    # verifica o caminho para percorrer o grafo (Passeio) através do algorítmo depth-first search
    caminho0dfs = grafo.dfs(0)
    print('Passeio completo a partir de A utilizando o método dfs: ', caminho0dfs, '\n --------------------')
    # caminho0bfs = grafo.bfs(0)  # verifica o caminho para percorrer o grafo (Passeio) através do algorítmo
    #                             # breadth-first search
    # print('Passeio completo a partir de A utilizando o método bfs: ', caminho0bfs, '\n ---------------------')
    grafo.imprimirMatriz(grafo.gerarMatrizAdjacencia(), 'gerarMatrizAdjacencia')  # imprime a matriz de adjacência
    print('\n --------------------')

    # retorna a matriz de alcançabilidade
    grafo.imprimirMatriz(grafo.gerarMatrizAlcancabilidade(3), 'gerarMatrizAlcancabilidade')

    # verifica a alcançabilidade entre dois vértices
    v1, v2 = 1, 4
    print(f'Verificar alcançabilidade de {v1} para {v2}: ', grafo.verificarAlcancabilidade(v1, v2))
    print(f'verifica caminho - dfs_caminho entre {v1} e {v2}: ', grafo.dfs_caminho_sem_repeticao(v1, v2))
    print(f'Verifica menor caminho - entre {v1} e {v2}', grafo.menorCaminho(v1, v2))
    '''
    arvore = grafo.getKruskal()
    # exibirGrafo(arvore)
    grafo.exibirGrafo()
    print('maximal: ', grafo.maximal())

    # print('menorCaminho(): ', grafo.menorCaminho(5, 2))


if __name__ == '__main__':
    main()
