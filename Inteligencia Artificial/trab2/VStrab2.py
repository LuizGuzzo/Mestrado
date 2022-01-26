##FUNÇÕES


def my_obj_fn(x):
    return np.sin(x) + np.random.normal(loc=0.0, scale = 0.1)

def calculaRMSE(valor_fo,result):
    return np.sqrt(np.mean(np.square(valor_fo - result)))


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
            vizinho = solucao + np.random.normal(loc=0, scale=self.DESVIO_PADRAO)
            # basicamente vai pegar outro vizinho enquanto estiver fora do espaço de busca
            while vizinho < self.search_space[0] or vizinho > self.search_space[1]:
                vizinho = solucao + np.random.normal(loc=0, scale=self.DESVIO_PADRAO)
            
            vizinhos.append(vizinho)

        return vizinhos
    
    def atTemperature(self):
        self.temperature *= self.alpha
        return self.temperature

## NN

class Camada():
    def __init__(self, input_units, output_units):
        # iniciando os pesos "aleatoriamente" (matriz)
        self.weights = np.random.normal(loc=0.0, 
                                        scale = np.sqrt(2/(input_units+output_units)), 
                                        size = (input_units,output_units))
        self.biases = np.zeros(output_units)
        #print("peso:",self.weights)
        #print("bias:",self.biases)
        
    def forward(self,input):
        # multiplicando o input com os pesos depois somando a bias + calculando o tanh
        return np.tanh(np.dot(input,self.weights) + self.biases)

    
def processNN(entrada,rede):
    activations = []
    for l in rede:
        activations.append(l.forward(entrada))
        entrada = activations[-1]
    return entrada
        

    
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from IPython import display

#%matplotlib inline

## MAIN

N_POPULACAO = 1 #50
N_INTERACAO = 100 #2000
#np.random.seed(0)
SEARCH_SPACE = [-5,5]
    
def main():
    rede = []
    
    entrada = [3] # entrada varios valores
    valor_fo = my_obj_fn(entrada) # saida de varios valores desejados
    RMSEs = []
    
    print("DADO DE ENTRADA DA REDE:",entrada)
    print("RESULTADO PELA FUNCAO DA ENTRADA:", valor_fo)
    
    rede.append(Camada(len(entrada),3))
    rede.append(Camada(3,1))
    #fazer um pergunta cm quantas camadas, e cada loop perguntar qnt de neuronios
    
    result = processNN(entrada,rede)
        
    
    #calcular RMSE (precisa testar com mais dados se ele calcula o RMSE para varias entradas, array no caso)
    rmse = calculaRMSE(valor_fo, result)
    # esse rmse significa o resultado q a NN virgem deu
    
    RMSEs.append(rmse)
    
    print("RESULTADO DA NN: ",result)
    print("RMSE (resFunc-resNN): ",rmse)
    
    figure= plt.subplots(figsize=(10, 8))
    plt.title("RMSE", fontsize=20)
    plt.xlabel("interacoes")
    plt.ylabel("Fo")
    
    SA = SimulatedAnnealing(search_space = [-np.pi, np.pi],
                            DESVIO_PADRAO = 0.3,
                            temperature = 100,
                            alpha = 0.995,
                            num_vizinhos = 1)
    
    # modificando um dado da rede para calcular o novo RMSE se ele melhora atualiza a rede, se nao vai para proxima interacao
    for p in range(N_POPULACAO*N_INTERACAO):
        # extraindo ids da rede
        layerId = np.random.randint(len(rede))
        weighId = np.random.randint(len(rede[layerId].weights))
        neuroId = np.random.randint(len(rede[layerId].weights[weighId]))
        
        #print("camada[{}/{}], peso[{}/{}], neuronio[{}/{}] ".format(len(rede),layerId,len(rede[layerId].weights),weighId,len(rede[layerId].weights[weighId]),neuroId))
        
        # extraindo peso e bias
        peso = rede[layerId].weights[weighId][neuroId]
        bias = rede[layerId].biases[neuroId]

        # filtro para mudar Peso ou Bias
        if np.random.randint(100) <= 50:
            isPeso = True
            data = peso
        else:
            isPeso = False
            data = bias
        
        #condiçao de mutaçao
        if np.random.randint(100) <= 50:
            data += np.random.normal(0,1)
            #adiciona gaussiana no dado
        else:
            data = np.random.uniform(low=SEARCH_SPACE[0], high=SEARCH_SPACE[1])
            #muda o dado para um valor aleatorio dentro do espaço de busca
        
        ##############################################################
        #modificar os valores
        #com o SA e GA

        vizinhos = SA.gera_vizinhos(data)
        for data_vizinha in vizinhos:
            #cria uma rede temporaria para testar desempenho (podia criar uma flag para utiliza a mesma rede caso n fosse alterada para poupar memoria.. preguiça)
            newRede = rede.copy()

            if isPeso:
                newRede[layerId].weights[weighId][neuroId] = data_vizinha
            else:
                newRede[layerId].biases[neuroId] = data_vizinha

            newResult = processNN(entrada,newRede)
            newRMSE = calculaRMSE(valor_fo,newResult)
#             print("newRMSE:",newRMSE,"rmse:",rmse)
            if newRMSE < rmse:
                rmse = newRMSE # RMSE da nova  rede
                rede = newRede # nova rede
                print("ACEITOU")
            else:  # data_vizinha eh pior (delta >= 0)
#                 print("negado")
                prob_aceitacao = np.exp((-newRMSE) / SA.temperature)
#                 print("probabilidade:",prob_aceitacao)
                if np.random.uniform(0, 1) < prob_aceitacao:
#                     print("prob aceita..")
                    # data_vizinha eh aceito mesmo sendo pior.
                    rmse = newRMSE # RMSE da nova  rede
                    rede = newRede # nova rede

            SA.atTemperature()
            RMSEs.append(rmse)
            print(len(RMSEs))

            #print(f"Solucao: {self.solucao} FO: {self.valor_funcao_objetivo}")

        
    
#   print(RMSEs)
    result = processNN(entrada,rede)
    print("Resultado Final:",result)
    
    plt.plot(RMSEs)
    plt.show()
    
    
if __name__ == "__main__":
    main()