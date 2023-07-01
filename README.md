# Grafos
Repositório criado com o intuito de armazenar o conteúdo da matéria de grafos do 
curso de Ciência da Computação no IFBA Camaçari.


<hr>
<h3> Class Grafo # 
<pre>
-----------------------------------------------------------
|       Grafo      |
--------------------
| - lista: list    |
| - adj: defaultdict(set) |
| - direcionado: bool |
--------------------
| + __init__(arestas, direcionado=False) | - Inicia o objeto.
| + get_vertices(): list | - Retorna os vértices em formato de lista.
| + get_arestas(): list | - Retorna a lista de arestas do grafo. 
| + adiciona_arestas(arestas) | - Adiciona arestas no grafo.
| + adiciona_arco(u, v, peso) | - Verifica se a aresta é direcionada e adiciona-as no grafo.
| + existe_aresta(u, v): bool | - Verifica se existe arestas entre os dois vértices.
| + __len__(): int | - Retorna o grau do grafo.
| + __str__(): str | - Formata o grafo em um dicionário '{}({})'.
| + __getitem__(v) | - Retorna um vértice e suas aréstas.
| + exibirGrafo() | - Exibe o grafo usando.
| + posicao_vertice(vertice) |  - retorna a posição do vértice.
| + checaExistenciaVertices(v): bool | - Verifica se existem arestas aentre os dois vértices. 
| + dfs(inicio, visitados=None, caminho=None): list | - Depth-first search - Algoritmo de busca em profundidade.
| + dfs_caminho_sem_repeticao(inicio, fim, caminho=None) | - DFS com vértice de início e fim.
| + bfs(inicio): list | - Breadth-first search - Algoritmo de busca em largura.
| + imprimirMatriz(matriz, methodName) | - Exibe matriz de Alcançabilidade / Adjacência.
| + gerarMatrizAdjacencia(): list | - Calcula matriz de adjacência.
| + gerarMatrizAlcancabilidade(dist): list | - Gera matriz de alcançabilidade.
| + verificarAlcancabilidade(a, b): tuple | - Verifica alcanlçabilidade entre dois vértices.
| + getKruskal(): defaultdict(set) | - Algoritmo de kruskal, retorna a árvore geradora do grafo.
| + menorCaminho(a, b): list | Retorna o menor caminho entre dois vértices usando a biblioteca nxGraph.
| + vgc(): dict | Retorna os vértices ordenados por grau crescente.
| + maximal(): list | Retorna o conjunto de vértices maximal do grafo.
----------------------------------------------------------- </pre>

