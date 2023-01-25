
# Solução do problema 2

O codigo foi copiado deste [Repositorio](https://github.com/tonisidneimc/Regex-Engine), e não contempla todas as solicitações pedidas no trabalho, ele esta um pouco incompleto.
Este repositorio foi eleito por conta da abordagem em que o professor havia recomendada e também porque me sentia mais confortavel em implementar. O codigo também por apresentar algumas implementações incompletas, acreditava ser o ideal para aprender a implementar este problema. (Não consegui finalizar também todos os requisitos)
A elaboração do problema foi utilizando Maquina de Estados, buscando na internet havia encontrado sobre o Algoritmo de Thompson, oque me guiou a buscar uma implementação que estivesse a usando esse algoritmo.

A parte I apenas resolve algumas operações e não atende ainda elas 100%, recomendo rodar o programa "examples.py" que é literalmente os exemplos que o dev do repo original deu. Caso queira testar usando as metricas solicitadas no trabalho rode o programa "main.py".

Primeiramente verifique se está no diretorio principal do trabalho:

```Python
cd "trab 2"
```
para executar o programa de exemplos digite:
```Python
python prob2\examples.py
```
para executar o programa que usa os parametros "-r" e "-f" digite:
```Python
python prob2\main.py
```

Acredito que com apenas a primeira parte parcialmente implementada seja o suficiente para realizar ao menos a parte II do problema cujo necessita calcular a complexidade de tempo da questão.

Dado isso, ao analisar o codigo podemos ver que existem 4 funçoes principais, sendo eles:

A "preProcess":\
	A função "preProcess" tem complexidade O(n) pois ela itera sobre a expressão regular de entrada e adiciona caracteres extras durante o processo. Operadores de concatenação são adicionados quando seus requisitos sao atendidos, e também a operação de Range, em que consiste transformar como por exemplo [1-5] viraria (1|2|3|4|5), a fim de atender todas os estados possiveis.
Portanto a complexidade se daria O(n), sendo o N a expressão regular de entrada.

O "toPosfix":\
	A função "toPosfix" tem complexidade O(n) pois ela itera sobre a expressão regular de entrada que foi previamente expandida (adicionado os concat e os estados do range), ela adiciona caracteres a uma lista de saída e empilha os operadores. basicamente ao final do processo ele organiza a ordem dos simbolos e operadores para proxima etapa.
Portanto a complexidade se daria como O(n), sendo N o tamanho da expressão regular de entrada.

O "toNFA":\
	A função toNFA é responsável por construir o NFA a partir da expressão regular na notação que o posfix organizou. Ela faz isso iterando sobre cada caractere na expressão posfix e, para cada caractere, realiza operações de pilha, como push e pop, para construir o NFA. Isso resulta em uma complexidade O(N).
Portanto a complexidade é O(n) onde N é o comprimento da expressão regular na notação posfix.

E por ultimo a função que roda o NFA sobre o texto enviado. A função "search":\
    A função search é responsável por percorrer a NFA gerada pelas etapas anteriores, e comparando a NFA com a string de entrada. Ela faz isso iterando sobre cada caractere na string de entrada e, para cada caractere, verifica todos os estados atuais e seus estados de transição. Isso resulta em uma complexidade O(M*N), onde M é o comprimento da string de entrada e N é o número de estados no NFA.

Para calcular a complexidade de tempo do algoritmo todo basta somar todas as funçoes. Utilizando apenas essas 4 funçoes principais onde,
a soma delas O(n + n + n + m*n) daria uma complexidade proxima de O(MN + 3N), onde N é o comprimento da expressão regular e M o comprimento da string de entrada.
Portanto a complexidade de tempo do algoritmo considerando o maior expoente seria de O(MN).

Vale lembrar que não estou calculando integralmente o codigo pois existem varios outros metodos que possuem menor peso na complexidade de tempo, portanto não adicionei-os na soma.