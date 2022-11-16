
# Trabalho 1 --- Teoria da Computação --- 2022/2

Trabalho da materia de Teoria da computação abordando os temas da materia: Computabilidade e Cálculo lambda

**Professor:** Jefferson O. Andrade

**Autor:** [Luiz Antonio Roque Guzzo](https://www.github.com/luizguzzo)

Irei abordar apenas  os problemas que não foram respondidos no PDF.
Todas as soluções foram implementadas em Python.

Sendo eles os problemas: 1, 4, 5, 6



## Problema 1

Este problema pede a construção de um programa que receba como entrada um programa e escreva ele entre "<>" 2 vezes, ou seja, sendo P como a transcrição do programa a resposta é <P><P>

Para executar o programa, execute o programa prob1.py :

```python
python prob1.py
```

## Problema 4

Este problema pede para provar a execucão de uma função em calculo Lambda,
se ela retorna sempre TRUE se e somente se ao menos duas das entradas forem iguais a TRUE,
ja que o programa recebe apenas 3 entradas, é demonstrado todos os cenarios possiveis de resposta,
provando que tal função realiza o procedimento.

Realizei os testes todos no site do [Lambster](https://lambster.dev).

A sequencia utilizada - e suas respostas:

```
000 - 0
001 - 0
010 - 0
011 - 1
100 - 0
101 - 1
110 - 1
111 - 1
```
Os simbolos 1 e 0 da questão correspondem a "true" e "false" do proprio lambster,
por isso que utilizei os nomes "true" para representar o numero 1,
 e "false" para representar o numero 0 na função alt

Segue o codigo executado no Lambster com as alteraçoes dos simbolos:

```
alt = La b c.(a (b true (c true false) ) (b c false) )

alt false false false 
alt false false true  
alt false true false  

alt false true true   
alt true false false  
alt true false true   

alt true true false   
alt true true true    

```

A resposta retornada do Lambster ao executar os comandos, provando o resultado da questão.

```
lambster: A lambda calculus interpreter
version 1.0.6 -- type 'help' for more information
λ> alt = La b c.(a (b true (c true false) ) (b c false) )
>>> alt = (λa. (λb. (λc. ((a ((b (λt. (λf. t))) ((c (λt. (λf. t))) (λt. (λf. f))))) ((b c) (λt. (λf. f)))))))
λ> alt false false false
>>> (λt. (λf. f))
    ↳ equivalent to: false, zero
λ> alt false false true
>>> (λt. (λf. f))
    ↳ equivalent to: false, zero
λ> alt false true false
>>> (λt. (λf. f))
    ↳ equivalent to: false, zero
λ> alt false true true
>>> (λt. (λf. t))
    ↳ equivalent to: true
λ> alt true false false
>>> (λt. (λf. f))
    ↳ equivalent to: false, zero
λ> alt true false true
>>> (λt. (λf. t))
    ↳ equivalent to: true
λ> alt true true false
>>> (λt. (λf. t))
    ↳ equivalent to: true
λ> alt true true true
>>> (λt. (λf. t))
    ↳ equivalent to: true
```
## Problema 5

O problema pede para implementar as funções "MIN, MAX, APPEND, REVERSE" em Calculo Lambda utilizando a codificação de Church.

As funções estão implementadas no arquivo prob5.py , porem python possui dificuldades ao executar
o combinador Y para rodar a recursividade das funções executadas, tentei fazer um contorno
nas funçoes para demonstrar que a função construida funciona, porem apenas as de MIN e MAX que consegui
devido ao APPEND e REVERSE depender das chamadas internas para construir o vetor, acabei não fazendo a versão que roda por um loop externo

As funçoes MIN e MAX fiz uma versão delas sem o λf, fazendo as funçoes rodar a repetição em um loop externo feito
pelo proprio Python.

Os codigos de como rodaria puramente em calculo Lambda as funções se encontram no arquivo **prob5a.py** ,
porem o arquivo ao ser executado ira dar problema de recursividade infinita, devido a dificuldade que python possui
para tratar.

E o arquivo **prob5b.py** é versão simplificada de MIN e MAX sendo rodadas por um loop externo.
Ao executa-lo ira retornar sem problemas, devido a adaptação.

Ambas versões possui comentario nas linhas para facilitar o entendimento das mesmas.
E importam as funcoes basicas vindas do arquivo **definicoes.py** que tem a implementação das
funçoes do calculo lambda basica + em cada linha sua versão de calculo Lambda interpretado pelo Lambster.

Para executar o problema basta rodar.

```
# programa 5 A - versão que dá recursividade infinita, porem o mais proximo do calculo lambda

python prob5a.py

# programa 5 B - versão que retorna os resultados de MIN e MAX
# utilizando as funçoes sem a recursividade interna

python prob5b.py
```


## Problema 6

Construir as implementações feitas no problema 5 em uma linguagem de programação que tenha a construção lambda
A implementaçao deve ser o mais próxima do Calculo Lambda que a linguagem permitir.

Tal questão é basicamente a tradução do problema 5 em um formato que o Python consegue processar
sem dar recursividade infinita.

Para rodar a solução do problema basta executar o comando:

```
python prob6.py
```