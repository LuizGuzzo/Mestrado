import random
from copy import deepcopy

# um loop para cada membro apenas para transformar em uma lista de Index igual o exercicio pede
def equipe_to_index(L,equipe):
    index_equipe = []
    for e in equipe:
        index_equipe.append(L.index(e))
    return index_equipe

def EMP(L, m, k):
    selecionados, pendentes = L[:k] , L[k:]    
    # limite = 0
    # Verifique se todas as competências foram cobertas
    competenciasAtendidas = competencias_cobertas(selecionados)
    # Caso alguma competência ainda não tenha sido coberta, realize trocas entre os elementos da lista de selecionados
    for _ in range(len(L)): # roda L vezes, pegando todos os membros
            
        if competenciasAtendidas >= m:
            selecionados = equipe_to_index(L,selecionados)
            return selecionados

        # Escolha um candidato da lista de selecionados
        bestMember = False
        for novo_candidato in pendentes: # roda len(L)-k vezes

            badMember = False
            # pegar um candidato que adicione competencias a equipe
            for membro in selecionados: # roda K vezes
                novoTime = deepcopy(selecionados)
                novoTime.remove(membro)
                novoTime.append(novo_candidato)
                novas_competenciasAtendidas = competencias_cobertas(novoTime) # roda + k vezes
                # novo candidato substituindo o membro melhora a equipe?
                if novas_competenciasAtendidas > competenciasAtendidas:
                    # sim, é eleito o melhor e pior membro para troca
                    badMember = membro
                    bestMember = novo_candidato
                    break
            if bestMember != False:
                break


        if badMember == False:
            # se nenhum membro for eleito pega o primeiro
            badMember = selecionados[0]
            bestMember = L[0]

        # faz a troca pelo novo candidato
        # e adiciona o removido no pendentes denovo
        # verifica se bateu as competencias
        # caso não, roda pra pegar um novo candidato

        selecionados.remove(badMember)
        pendentes.remove(bestMember)

        selecionados.append(bestMember)
        pendentes.append(badMember)

        competenciasAtendidas = competencias_cobertas(selecionados) # roda k vezes
        # limite += 1
    
    return "NIL"

def competencias_cobertas(equipe):
    competencias = set()
    for membro in equipe:
        competencias.update(membro)

    return len(competencias)

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
