import random
from copy import deepcopy

def EMP(L, m, k):
    selecionados, pendentes = L[:k] , L[k:]    
    # limite = 0
    # Verifique se todas as competências foram cobertas
    competenciasAtendidas = competencias_cobertas(selecionados)
    # Caso alguma competência ainda não tenha sido coberta, realize trocas entre os elementos da lista de selecionados
    for _ in range(len(L)): # roda L vezes, pegando todos os membros
            
        if competenciasAtendidas >= m:
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

import random
M = 15 # num total de competencias coberto pela equipe
K = 4 # numero de empregados que ira compor a equipe

habilidades = list(range(M)) # cria uma lista com as 15 habilidades possíveis

L = []
for i in range(3000): # tamanho de L
    habilidades_pessoa = random.sample(habilidades, 4) # escolhe 4 habilidades aleatórias para a pessoa
    L.append(habilidades_pessoa)

# L = [[14, 6, 1, 13], [2, 3, 9, 12], [5, 13, 8, 14], [6, 13, 8, 0], [12, 7, 8, 11], [1, 12, 6, 10], [13, 5, 8, 14], [3, 12, 6, 13], [13, 7, 4, 0], [5, 0, 10, 8], [4, 13, 9, 11], [1, 4, 5, 2], [11, 2, 14, 0], [8, 2, 3, 6], [3, 5, 2, 7], [13, 1, 8, 10], [14, 3, 7, 6], [8, 3, 9, 4], [13, 3, 4, 6], [8, 11, 13, 9], [14, 0, 2, 1], [2, 6, 1, 0], [8, 2, 7, 9], [11, 8, 13, 6], [7, 2, 10, 1], [4, 14, 9, 2], [14, 3, 8, 1], [1, 0, 14, 4], [11, 6, 12, 2], [7, 12, 8, 14]]
# print(L)
res = EMP(L,M,K)
print(res)

