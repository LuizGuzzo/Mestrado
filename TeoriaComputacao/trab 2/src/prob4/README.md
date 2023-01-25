
# Solução do problema 4

## Parte 1
É utilizado uma redução de tempo polinomial do problema "sub-set-Sum" para o problema de recrutamento (EMP).

## Parte 2
O arquivo que corresponde a parte 2 é o arquivo "prob4\prob4.py"
Nele o algoritmo testa todas as possibildades de equipes, oque configuraria a complexidade de tempo O(N**k)

Para executa-lo, primeiramente verifique se esta no diretorio principal:
```Python
cd "trab 2"
```

Para executar o codigo da parte 2 escreva no terminal:

```Python
python prob4\prob4.py
```
Ja que não foi solicitado padroes de entrada, ao executar o codigo ele ira rodar apenas a função contida na questão com os parametros:

L = [[0,1,2],[1,3],[4,3]] ;
M = 5 ;
K = 2 ;

E entregara a resposta entre chaves dos indices dos candidatos aprovados. Ex: [0,2]

No codigo possui um gerador de candidatos comentado caso deseje usa-lo, basta comentar as linhas 72, 83 e 93, comentando o inicio e fim da string do gerador e o problema do exercicio.

## Parte 3

É solicitado alteraçoes no programa elaborado na Parte 2 para gerar uma versão dele mais eficiente computacionalmente, ou seja com menor ordem de complexidade de tempo.



Para executa-lo, primeiramente verifique se esta no diretorio principal:
```Python
cd "trab 2"
```
Para executar o codigo da parte 3 escreva no terminal:

```Python
python prob4\prob4Best.py
```

Semelhante ao codigo da parte 2, este também possui um gerador de candidatos, caso deseje utiliza-lo.
