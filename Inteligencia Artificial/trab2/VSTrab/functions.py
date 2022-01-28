import numpy as np

##FUNÇÕES 

def true_regression_fn(x): # troca pra coseno dps tangente
    return np.sin(x) + np.random.normal(loc=0.0, scale = 0.1)

def calculaRMSE(TREINO_ESCOPO,RESP_FO,rede):
    
    y_pred = []
    y = RESP_FO
    for input in TREINO_ESCOPO:
        data = processNN([input],rede)[0] # ja que é uma entrada e uma saida por isso do [0]
#         print(data)
        y_pred.append(data)
    
#     print("y_pred:",y_pred)
#     print("y:",y)

    error = np.subtract(y,y_pred)
#     print(error)
    return np.sqrt(np.mean(np.square(error)))
    

def processNN(entrada,rede):
    activations = []
    for l in rede:
        activations.append(l.forward(entrada))
        entrada = activations[-1]
    return entrada

def plot_fn(true_regression_fn, search_space, step=0.1):
    # plt.clf()
    x = np.arange(search_space[0], search_space[1], step)
    y = np.array(list(map(true_regression_fn, x)))
    plt.plot(x, y)