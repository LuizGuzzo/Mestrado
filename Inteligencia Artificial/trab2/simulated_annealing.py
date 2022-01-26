
import numpy as np
import matplotlib.pyplot as plt


def plot_fn(my_obj_fn, search_space, step=0.1):
    # plt.clf()
    x = np.arange(search_space[0], search_space[1], step)
    y = np.array(list(map(my_obj_fn, x)))
    plt.plot(x, y)


def my_obj_fn(x):
    return np.sin(x)


def gera_vizinhos(solucao, desvio_padrao, n_vizinhos, espaco_busca):
    vizinhos = []

    for _ in range(n_vizinhos):
        vizinho = solucao + np.random.normal(loc=0, scale=desvio_padrao)

        while vizinho < espaco_busca[0] or vizinho > espaco_busca[1]:
            vizinho = solucao + np.random.normal(loc=0, scale=desvio_padrao)

        vizinhos.append(vizinho)

    return vizinhos


def main():
    search_space = [-np.pi, np.pi]
    DESVIO_PADRAO = 0.3
    N_ITERATIONS = 2000

    np.random.seed(7)
    plt.figure(figsize=(20, 40))

    solucao = np.random.uniform(low=search_space[0], high=search_space[1])
    valor_funcao_objetivo = my_obj_fn(solucao)

    temperature = 100
    alpha = 0.9995

    temperatures = [temperature]

    for iteration in range(N_ITERATIONS):
        vizinhos = gera_vizinhos(solucao, DESVIO_PADRAO, 10, search_space)
        for vizinho in vizinhos:
            fo_vizinho = my_obj_fn(vizinho)

            delta = fo_vizinho - valor_funcao_objetivo
            if delta < 0:  # vizinho eh melhor
                solucao = vizinho # valor X do vizinho
                valor_funcao_objetivo = fo_vizinho # valor y do vizinho
            else:  # vizinho eh pior (delta >= 0)
                prob_aceitacao = np.exp((-delta) / temperature)
                if np.random.uniform(0, 1) < prob_aceitacao:
                    # vizinho eh aceito mesmo sendo pior.
                    solucao = vizinho
                    valor_funcao_objetivo = fo_vizinho

            temperature *= alpha
            temperatures.append(temperature)

            print(f"Solucao: {solucao} FO: {valor_funcao_objetivo}")

        plt.subplot(1, 2, 1)
        plt.cla()
        plot_fn(my_obj_fn, search_space)
        plt.plot(vizinhos, my_obj_fn(vizinhos),'*g', markersize=7)
        plt.plot([solucao], [valor_funcao_objetivo],'*r', markersize=7)
        plt.title(f"Iteration: {iteration}")
        plt.subplot(1, 2, 2)
        plt.cla()
        plt.plot(temperatures)
        plt.title("temperature")
        plt.waitforbuttonpress()

    plt.show()


if __name__ == "__main__":
    main()
