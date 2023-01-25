# ciclo hamiltoniano
# problema: https://open.kattis.com/problems/paintball
# base : https://www.codespeedy.com/check-if-hamiltonian-cycle-exists-in-a-graph-using-python/

def cicloHamiltoniano(visitados,matriz,noOrigem):
    visitados.append(noOrigem)
    for noDestino in matriz[noOrigem]:
        if(noDestino not in visitados):
            if(cicloHamiltoniano(visitados,matriz,noDestino)):
                return True
    
    if(num_vertices == len(visitados)): # verifica se o ultimo valor linka com o primeiro
        if(visitados[0] in matriz[visitados[len(visitados)-1]]):
            return True 
        else:
            return False

    visitados.pop()


import sys
inputF = sys.stdin.readline

NumV_NumA = inputF().split()
num_vertices = int(NumV_NumA[0])

matriz = [[] for _ in range(num_vertices)]

num_arestas = int(NumV_NumA[1])

for _ in range(num_arestas):
    ligacao = inputF().split()
    a = int(ligacao[0])-1
    b = int(ligacao[1])-1
    matriz[a].append(b)
    matriz[b].append(a)

# matriz = [[1, 2, 5], [0, 2], [0, 1, 3, 4], [2, 4], [6, 2, 3, 5], [0, 6, 4], [5, 4]]
# num_vertices = 7
# num_arestas = 10
# print(matriz)

ciclo = False
for no in range(num_vertices):
    visitados = list()
    if (cicloHamiltoniano(visitados,matriz,no)):
        ciclo = True
        first = visitados.pop(0) +1
        for i in visitados:
            print(i+1)
        print(first)
        break
    # print("no: ",i)

if not ciclo:
    print("Impossible")
   