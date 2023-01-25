
# Solução do problema 3

Para demonstrar que o problema de "Dominating Set" é um problema NP-completo irei fazer uma redução do problema de "Vertex-Cover" que foi resolvido por Karp como NP-completo e que foi abordado pelo Teorema 7.44 do livro de Sipser e na lista dos 21 problemas NP-Completos (17.3) do livro "What Can Be Computed", após isso irei fazer a redução para o "Simplified Dominating Set".

Em resumo a redução sera: Vertex-Cover > Dominating Set > Simplified Dominating Set.

Os passos a passos da redução foram obtidos desta [Referencia](https://www.youtube.com/watch?v=HueFKEg7QZ8)

Sendo os passos da redução:
1. Converte o grafo original G em um grafo bipartido H:
    * Se faz 2 conjuntos A e B como cópia dos vértices do grafo G.
    * Coloca-se uma aresta entre cada vértice de A para B se eles forem adjacentes a G
    * Coloca-se também uma aresta ligando o vertice de A entre o correspondente em B
2. Calcula o grau de todos os vértices de A
3. 
    * Seleciona o vértices de A com o maior grau e adiciona o vértice V ao um conjunto D
    * Remova todos os vértices no conjunto B que estão cobertos pelo vértice eleito V, inclusive ele mesmo
    * Remova o vértice V de A
4. Repete o passo 2 depois o 3 até que não haja mais vértices no conjunto B, os vértices contidos no conjunto D é o conjunto dominante


## Uso/Exemplos

Primeiramente verifique se está no diretorio principal do trabalho:

```Python
cd "trab 2"
```
para executar o programa digite:
```Python
python prob3\prob3.py
```

Caso queira alguns exemplos de grafos para testar basta copiar um dos grafos abaixo e colar no terminal em que esta executando o programa.
```Python
# grafo 1
8 
0 1
0 2
0 3
1 3
2 3
3 4
4 6
5 6

# grafo 2
8
2 0
2 3
2 5
2 4
3 1
3 4
3 5
4 5
4 6
5 7

#grafo 3
9
1 0
1 2
1 3
6 4
6 5
6 7
6 8
0 2
0 3
0 7
0 8
2 5
2 7
3 4
3 8
4 5
4 7
5 8

```
