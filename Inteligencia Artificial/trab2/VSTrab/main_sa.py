## MAIN SA
from NN import *
from functions import *
from SA import *

import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from IPython import display


N_POPULACAO = 50 #50
N_INTERACAO = 2000 #2000
# np.random.seed(0)
PI = np.pi
SEARCH_SPACE = [-5,5] #espaço de operaçao
TRAINING_SPACE = [-PI,PI]

TESTE_ESCOPO = [] # escopo de entradas de teste da rede
aux = -2*PI
while aux <= 2*PI:
    TESTE_ESCOPO.append(aux)
    aux += 0.2

TREINO_ESCOPO = []
aux = TRAINING_SPACE[0]
for _ in range(32):
    TREINO_ESCOPO.append(aux)
    aux += 0.2
    
def main():
    
    # caso precise criar uma rede com varias entradas
#     entrada = [] # entrada varios valores
#     aux = -3
#     for _ in range(6):
#         entrada.append(aux)
#         aux += 1
    
    rede = []
    entrada = [3]

        
    RESP_FO = []
    for x in TREINO_ESCOPO:
        RESP_FO.append(true_regression_fn(x))
    
    
    tabelaNeural = [0]
    tabelaNeural = [2,4,8,16,32,64,128] # comenta essa linha para ativar o modo criar sua rede
    tabelaRmse = []
    
    for tn in range(len(tabelaNeural)):
        
        RMSEs = []
        inLayer = len(entrada)
        if len(tabelaNeural) == 1:
            print("Quantas camadas você deseja que a rede tenha?")
            camadas = int(input()) # quantas camadas vc quer
            for i in range(camadas):
                print("Quantos neuronios na camada",i,"voce deseja?")
                outLayer = int(input()) # quantos neuronios vc quer
                rede.append(Camada(inLayer,outLayer))
                inLayer = outLayer
        else:
            camadas = 1    
            for i in range(camadas):
                outLayer = tabelaNeural[tn]
                rede.append(Camada(inLayer,outLayer))
                inLayer = outLayer
            print("EXECUTANDO TABELA NEURAL [ INTERACAO:",tn,"NEURONIOS:",tabelaNeural[tn],"]")
        rede.append(Camada(inLayer,len(entrada)))

        
#         for layer in rede:
#             print(layer.weights)
#             print(layer.biases)

        rmse = calculaRMSE(TREINO_ESCOPO,RESP_FO,rede)

        RMSEs.append(rmse)

        print("RMSE virgem:",rmse)

        figure= plt.subplots(figsize=(10, 8))
        plt.title("RMSE", fontsize=20)
        plt.xlabel("interacoes")
        plt.ylabel("Fo")
        

        SA = SimulatedAnnealing(search_space = TRAINING_SPACE, # espaço de treino da rede
                                DESVIO_PADRAO = 0.3,
                                temperature = 100,
                                alpha = 0.995,
                                num_vizinhos = 10)

        # modificando um dado da rede para calcular o novo RMSE se ele melhora atualiza a rede, se nao vai para proxima interacao
        for p in range(N_POPULACAO*N_INTERACAO):
            # extraindo ids da rede
            layerId = np.random.randint(len(rede))
            weighId = np.random.randint(len(rede[layerId].weights))
            neuroId = np.random.randint(len(rede[layerId].weights[weighId]))

#             print("camada[{}/{}], peso[{}/{}], neuronio[{}/{}] ".format(len(rede),layerId,len(rede[layerId].weights),weighId,len(rede[layerId].weights[weighId]),neuroId))

            # extraindo peso e bias
            peso = rede[layerId].weights[weighId][neuroId]
            bias = rede[layerId].biases[neuroId]

            # filtro para mudar Peso ou Bias
            if random.uniform(0,1) <= 0.5:
                isPeso = True
                data = peso
            else:
                isPeso = False
                data = bias

            vizinhos = SA.gera_vizinhos(data)
            for data_vizinha in vizinhos:
                #cria uma rede temporaria para testar desempenho (podia criar uma flag para utiliza a mesma rede caso n fosse alterada para poupar memoria.. preguiça)
                newRede = rede.copy()

                if isPeso:
                    newRede[layerId].weights[weighId][neuroId] = data_vizinha
                else:
                    newRede[layerId].biases[neuroId] = data_vizinha

                newRMSE = calculaRMSE(TREINO_ESCOPO,RESP_FO,newRede)

                if newRMSE < rmse:
                    rmse = newRMSE # RMSE da nova  rede
                    rede = newRede # nova rede
#                     print("Ta indo")
                else:  # data_vizinha eh pior (delta >= 0)
                    prob_aceitacao = np.exp((-newRMSE) / SA.temperature)
                    if random.uniform(0, 1) < prob_aceitacao:
                        # data_vizinha eh aceito mesmo sendo pior.
                        rmse = newRMSE # RMSE da nova  rede
                        rede = newRede # nova rede
                
#                 print(rmse)
                SA.atTemperature()
                RMSEs.append(rmse)


        print("RMSE Final:", rmse)
        
        resultado_teste = []
#         print("teste rede:",TESTE_ESCOPO)
        for te in TESTE_ESCOPO:
            resultado_teste.append(processNN([te],rede)[0])
#         print("resultado teste:",resultado_teste)
        
        # adiciona o Rmse final a tabela 
        tabelaRmse.append([tabelaNeural[tn], rmse])
        
        
        # plota o conjunto de treinamento + conjunto de teste
        plt.subplot(2, 1, 1)
        plt.cla()
        plot_fn(true_regression_fn, SEARCH_SPACE)
        plt.plot(TREINO_ESCOPO, RESP_FO,'*g', markersize=7)
        plt.plot(TESTE_ESCOPO, resultado_teste,'*r', markersize=7)
        plt.title("Result (green) and predict (red)")

        plt.subplot(2, 1, 2)
        # plta o avanço do rmse 
        plt.title("RMSEs")
        plt.plot(RMSEs)
        plt.show()

        
    #printa a tabela
    print("TABELA DE RMSEs")
    print(pd.DataFrame(tabelaRmse, columns=["qntNeuronios", "rmse"]))


    
    
    
if __name__ == "__main__":
    main()