from definicoes import *

# Implementações em python
# tradução da função em calculo lambda para o mais proximo possivel da estrutura original porem em Python
def MINlist(par):
  if isnil(first(par)) == true:
    return second(par)
  else:
    if (leq (second(par)) (head(first(par)))) == true:
      return (MINlist(pair
                (tail(first(par))) # calda da lista que recebeu como parametro do par
                (second(par))      # o menor valor da lista que recebeu no par
              ))
    else:
      return (MINlist(pair
                (tail(first(par))) # calda da lista que recebeu como parametro do par
                (head(first(par))) # o dado que foi removido da lista
              )) # chama a função diminuindo a lista e passando no par o valor que esta N

# tradução da função em calculo lambda para o mais proximo possivel da estrutura do calculo lambda, mas funcionando em python
def MAXlist(par):
  if isnil(first(par)) == true:
    return second(par)
  else:
    if (leq (head(first(par)))) (second(par)) == true:
      return (MAXlist(pair
                (tail(first(par))) # calda da lista que recebeu como parametro do par
                (second(par))      # o menor valor da lista que recebeu no par
              ))
    else:
      return (MAXlist(pair
                (tail(first(par))) # calda da lista que recebeu como parametro do par
                (head(first(par))) # o dado que foi removido da lista
              )) # chama a função diminuindo a lista e passando no par o valor que esta N


def APPENDlist(par):
    if (isnil(second(par)) == true) : #acabou o processamento da lista
      return nil # retorna o ultimo valor q é nil
    else:
      if isnil(first(par)) == false: # roda se nao chegou no final da lista original
        return cons(head(first(par)))(APPENDlist(pair(tail(first(par)))(second(par)))) # reduz o tamanho da lista original
      if isnil(second(par)) == false: # roda se nao chegou no final da lista nova
        return cons(head(second(par)))(APPENDlist(pair(first(par))(tail(second(par))))) # reduz o tamanho da lista nova


def REVERSElist(lst):
  if (isnil(head(lst)) == true):
    return nil # quando acabar
  else:
    return APPENDlist(pair #  realiza um append de forma inversa
                        (REVERSElist(tail(lst))) # passando a calda da lista
                                    (cons
                                        (head(lst)) # passando a cabeça da lista como sendo o ultimo parametro
                                        (nil)
                                    )
                     ) # ambos parametros sao uma "lista" para que o APPEND os processe.



print("lista 1:")
printList(lista)
print("lista 2:")
printList(lista2)
listaMesclada = APPENDlist(pair(lista)(lista2))
print("lista mesclada: ")
printList(listaMesclada)


listaReversed = REVERSElist(listaMesclada)
print("lista Revertida: ")
printList(listaReversed)
print("lista Revertida 2x: ")
listaReversed = REVERSElist(listaReversed)
printList(listaReversed)

print("menor valor da lista: ",MINlist(pair(listaReversed)(head(listaReversed)))(inc)(0))
print("maior valor da lista: ",MAXlist(pair(listaReversed)(head(listaReversed)))(inc)(0))