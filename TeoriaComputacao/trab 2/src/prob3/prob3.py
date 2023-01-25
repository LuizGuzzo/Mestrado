"""
exemplos de grafos: 

8 
0 1
0 2
0 3
1 3
2 3
3 4
4 6
5 6

8
2 0
2 3
2 5
2 4
3 1
3 4
3 5
4 5
4 6
5 7

9
1 0
1 2
1 3
6 4
6 5
6 7
6 8
0 2
0 3
0 7
0 8
2 5
2 7
3 4
3 8
4 5
4 7
5 8

"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f','--arq', type=str)
args = parser.parse_args()
vertices = int(input())
grafo = [[] for _ in range(vertices)]

while True:
    try: # não tem condição de parada no trabalho
        AB = input().split()
        grafo[int(AB[0])].append(int(AB[1]))
        grafo[int(AB[1])].append(int(AB[0]))

    except:
        break   

# print("grafo inserido: ",grafo) # grafo bidirecional

# grafo = [[1, 2, 3], [0, 3], [0, 3], [0, 1, 2, 4], [3, 6], [6], [4,  5], []]

conexo = False
for node in grafo:
    if len(node)>0:
        # isso inclui se ele ligar com ele mesmo é conexo
        conexo = True
        break

# basicamente seria só necessario verificar se ele era conexo..
if conexo:
    """
    referencia: https://www.youtube.com/watch?v=HueFKEg7QZ8
    1) converte o grafo original G em um grafo bipartido H:
        1.a) se faz 2 conjuntos A e B como cópia dos vértices do grafo G.
        1.b) coloca-se uma aresta entre cada vértice de A para B se eles forem adjacentes a G
        1.c) coloca-se também uma aresta ligando o vertice de A entre o correspondente em B
    2) Calcula o grau de todos os vértices de A
    3) 
        3.a) Seleciona o vértices de A com o maior grau e adiciona o vértice V ao um conjunto D
        3.b) Remova todos os vértices no conjunto B que estão cobertos pelo vértice eleito V, inclusive ele mesmo
        3.c) remova o vértice V de A
    4) repete o passo 2 depois o 3 até que não haja mais vértices no conjunto B, os vértices contidos no conjunto D é o conjunto dominante

    """

    bigraph = {i:grafo[i] for i in range(len(grafo))}
    # print(bigraph)
    for key in bigraph:
        bigraph[key].append(key)

    A = bigraph.copy()
    B = bigraph.copy()
    D = []
    # print("ini A: ",A)
    # print("ini B: ",A)
    # print("ini D: ",A)

    while len(B) > 0:
        V = max(A,key=lambda x: len(A[x])) # vertice (V) de A com maior grau de arestas (é um index)
        # print("V: ",V)
        D.append(V) # adiciona o vertice (V) de maior grau no conjunto D

        rem_list = A[V] # lista dos nós a serem removidos de B e das arestas de A
        # rem_list.append(V)
        B = {key: B[key] for key in B if key not in rem_list} # removendo os nós de B

        for key in A: # removendo as arestas
            A[key] = [vertice for vertice in A[key] if vertice not in rem_list]

        del A[V] # deletando o nó eleito

        # print("index eleito: ",V)
        # print("A: ",A)
        # print("B: ",B)
        # print("D: ",D)

    # a redução de Vertex Cover para Dominating set foi feita
    # print("Conjunto de dominação do grafo: ")
    # print(D)
    for item in D:
        print(item,end=" ")

    # a redução do Dominating set para a versão simplificada, é basicamente
    # verificar se o Dominating set é maior que zero, se sim ele existe.

    # Basicamente verificaria se o grafo é conexo
    # print("sim")

else:
    print("NIL")
    


