from itertools import combinations

# um loop para cada membro apenas para transformar em uma lista de Index igual o exercicio pede
def equipe_to_index(L,equipe):
    index_equipe = []
    for e in equipe:
        index_equipe.append(L.index(e))
    return index_equipe

def EMP(L,tot_competencias,cand_max):

    for equipe in combinations(L, cand_max): # gera todas as possibilidades dado um tamanho especifico
        competencias = set()
        for membro in equipe:
            # print("m: ",membro)
            competencias.update(membro) # apenas une as competencias, se deu o tamanho é a equipe
        if len(competencias) == tot_competencias:
            equipe = equipe_to_index(L,equipe)
            return equipe
        
    return "NIL" 
            

"""
# gerador de Candidatos
import random
M = 15 # num total de competencias coberto pela equipe
K = 4 # numero de empregados que ira compor a equipe
habilidades = list(range(M)) # cria uma lista com as 15 habilidades possíveis
L = []
for i in range(3000): # tamanho de L
    habilidades_pessoa = random.sample(habilidades, 4) # escolhe 4 habilidades aleatórias para a pessoa
    L.append(habilidades_pessoa)
res = EMP(L,M,K) #bigO O(N^k)
"""
"""
# teste de candidatos
L = [[0,2],[0,1],[2,3],[4,5,7],[4,5,6],[7,8,9]]
M = 10 # num total de competencias coberto pela equipe
K = 4 # numero de empregados que ira compor a equipe
res = EMP(L,M,K) #bigO O(N^k)
"""

# problema do exercicio
res = EMP([[0,1,2],[1,3],[4,3]],5,2)

print(res)
