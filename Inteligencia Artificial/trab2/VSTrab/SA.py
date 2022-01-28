import random
import numpy as np

## SIMULATED ANNEALING
class SimulatedAnnealing():
    
    def __init__(self,search_space, DESVIO_PADRAO, temperature, alpha, num_vizinhos):
        self.search_space = search_space
        self.DESVIO_PADRAO = DESVIO_PADRAO
        self.temperature = temperature
        self.alpha = alpha
        self.num_vizinhos = num_vizinhos

    def gera_vizinhos(self,solucao):
        vizinhos = []
        
        for _ in range(self.num_vizinhos):

            #condiçao de mutaçao
            if random.uniform(0,1) <= 0.5:
                vizinho = solucao + np.random.normal(loc=0, scale=self.DESVIO_PADRAO)
                #adiciona gaussiana no dado
                # basicamente vai pegar outro vizinho enquanto estiver fora do espaço de busca
                while vizinho < self.search_space[0] or vizinho > self.search_space[1]:
                    vizinho = solucao + np.random.normal(loc=0, scale=self.DESVIO_PADRAO)
            else:
                vizinho = random.uniform(self.search_space[0], self.search_space[1])
                #muda o dado para um valor aleatorio dentro do espaço de busca
            
            vizinhos.append(vizinho)

        return vizinhos
    
    def atTemperature(self):
        self.temperature *= self.alpha
        return self.temperature