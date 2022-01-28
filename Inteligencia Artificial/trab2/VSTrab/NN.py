import numpy as np

## NN

class Camada():
    def __init__(self, input_units, output_units):
        # iniciando os pesos "aleatoriamente" (matriz)
        self.weights = np.random.normal(loc=0.0, 
                                        scale = 5, 
                                        size = (input_units,output_units))
        self.biases = np.random.normal(loc=0.0, 
                                        scale = 5,
                                        size = output_units)
#         self.weights = np.zeros((input_units,output_units))
#         self.biases = np.zeros(output_units)
        #print("peso:",self.weights)
        #print("bias:",self.biases)
        
    def forward(self,inpt):
        # multiplicando o input com os pesos depois somando a bias + calculando o tanh
        return np.tanh(np.dot(inpt,self.weights) + self.biases)
