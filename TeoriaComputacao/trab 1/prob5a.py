from definicoes import *

lambMINList = lambda f: lambda par: (
  (isnil(first(par)) # se chegou no final da lista
    (second(par)) # retorna o minimo que esta no par
    ((leq(second(par))(head(first(par)))) # se o minimo que esta no par é menor do que esta na cabeça da lista
      (f(pair(tail(first(par)))(second(par)))) # chama a função diminuindo a lista e passando no par o valor que esta NO PAR
      (f(pair(tail(first(par)))(head(first(par))))) # chama a função diminuindo a lista e passando no par o valor que esta NA CABEÇA DA LISTA
    )
  )
) 

# como seria se fosse apenas calculo lambda o maxList
# mesma coisa do min, mas inverte o parametro no "leq"

lambMAXList = lambda f: lambda par: (
  (isnil(first(par)))
    (second(par))
    ((leq(head(first(par)))(second(par)))
      (f(pair(tail(first(par)))(second(par))))
      (f(pair(tail(first(par)))(head(first(par)))))
    )
)

lambAPPENDlist = lambda f: lambda par: (
    (isnil(second(par)) == true) #acabou o processamento da lista
      (nil) # retorna o ultimo valor q é nil
      (
        (isnil(first(par))) # roda se nao chegou no final da lista original
          (cons(head(first(par)))(f(pair(tail(first(par)))(second(par))))) # reduz o tamanho da lista original
        (isnil(second(par))) # roda se nao chegou no final da lista nova
          (cons(head(second(par)))(f(pair(first(par))(tail(second(par)))))) # reduz o tamanho da lista nova
      )
)

lambdaREVERSElist = lambda f: lambda lst: (
  (isnil(head(lst))) # enquanto nao acabar a lst
    (nil) # quando acabar
    (lambAPPENDlist(pair #  realiza um append de forma inversa
                      (f(tail(lst))) # passando a calda da lista
                      (cons
                          (head(lst)) # passando a cabeça da lista como sendo o ultimo parametro
                          (nil)
                      )
                    ) # ambos parametros sao uma "lista" para que o APPEND os processe.
    )
)

lambMIN = Y(lambMINList)(pair(lista)(head(lista)))
lambMAX = Y(lambMAXList)(pair(lista)(head(lista))) 
lambAPPEND = Y(lambAPPENDlist)(pair(lista)(lista2))
lambdaREVERSE = Y(lambdaREVERSElist)(lambAPPEND)