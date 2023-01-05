from itertools import combinations
# para cada candidatos da lista de candidatos:
    # procura o candidato com maior conjunto de competencias
    # adiciona ele na lista de candidatos cobertos
    # remove ele e as competencias que ele tem

# a cada ciclo um novo candidato é eleito e colocado nos candidatos cobertos

# repete o ciclo ate não ter mais competencias

# L é um array de candidatos que cada candidato tem suas competencias
def EMP(L,tot_competencias,cand_max):

    for equipe in combinations(L, cand_max): # gera todas as possibilidades dado um tamanho especifico

        # equipe = {i:equipe[i] for i in range(len(equipe))}
        
        # equipe = find_best_team(equipe,tot_competencias)
        competencias = set()
        for membro in equipe:
            competencias = competencias.union(membro)
        if len(competencias) == tot_competencias:
            return equipe
        
    return "NIL" 
            

        # cL organizado pelo grau de competencia
        # competencias : qnt membros que tem tal grau. # usarei para fazer as rotaçoes, 
        # competencias : [membros]
        

        # se cand_max for menor do que o encontrado
            # array de tamanho de grau, ex: para grau 3 tem x candidatos, [3:3,2:3,...]
            # rotate the biggest vertices e decrementa no array correspondente as vezes que rotacionou
            # [[0,1,2],[0,1,3],[0,2,3],[0,1],[1,2],[0,3]] vira > [[0,1,3],[0,2,3],[0,1,2],[0,1],[1,2],[0,3]]
        
        
        

    return False

def find_best_team(L_candidatos,tot_competencias):
    # interacao para achar o melhor candidato, remover as suas competencias da lista
    membros_eleitos = set()
    competencias = {i:i for i in range(tot_competencias)}
    while len(competencias)> 0 and len(L_candidatos)>0:     
        
        bigCand = max(L_candidatos,key=lambda x: len(L_candidatos[x])) # candidato com maior competencia
        membros_eleitos.add(bigCand) # lista das competencias cobertas (nao repete porque "set" evita isso)
        
        rem_list = L_candidatos[bigCand]
        
        # remove as competencias atendidas da lista de competencias
        # remove as competencias da lista de candidatos
        # remove o membro da lista de membros

        print("bigC: ",bigCand)
        print("A: ",L_candidatos)
        print("B: ",competencias)
        print("D: ",membros_eleitos)

        competencias = {key: competencias[key] for key in competencias if key not in rem_list} # removendo os nós de competencias

        for key in L_candidatos: # removendo as competencias da lista de candidatos
            L_candidatos[key] = [vertice for vertice in L_candidatos[key] if vertice not in rem_list]

        del L_candidatos[bigCand] # deletando o nó eleito

        # if len(competencias)> 0:
        #     print("achou")
        #     return membros_eleitos

    return membros_eleitos


# L = [[1,3],[4,3],[0,1,2]]# lista de candidatos representador por uma sublista e cada sublista contem numeros representando as competencias do candidato
L = [0,2],[0,1],[2,3],[4,5,7],[4,5,6],[7,8,9]
# L = [0,1],[2,3],[0,2],[4,5,6],[7,8,9],[4,5,7]
M = 10 # num total de competencias coberto pela equipe
K = 4 # numero de empregados que ira compor a equipe

res = EMP(L,M,K) # [0,2]

print(res)