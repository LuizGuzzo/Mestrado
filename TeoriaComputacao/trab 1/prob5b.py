from definicoes import *

lambMINList = lambda par: ( # lambda f removido
  (isnil(first(par)) # se chegou no final da lista
    (second(par)) # retorna o minimo que esta no par
    ((leq(second(par))(head(first(par)))) # se o minimo que esta no par é menor do que esta na cabeça da lista
      ((pair(tail(first(par)))(second(par)))) # recursividade removida
      ((pair(tail(first(par)))(head(first(par))))) # recursividade removida
    )
  )
) 

lambMAXList = lambda par: ( # lambda f removido
  (isnil(first(par)))
    (second(par))
    ((leq(head(first(par)))(second(par)))
      ((pair(tail(first(par)))(second(par)))) # recursividade removida
      ((pair(tail(first(par)))(head(first(par))))) # recursividade removida
    )
)

lista = cons(um)(cons(dois)(cons(tres)(cons(quatro)(nil))))
print("print lista: ")
printList(lista)

pList = lista
pMin = head(pList)
while isnil(pList) == false:  
  pair_list_min = lambMINList(pair(pList)(head(pMin)))
  pList = first(pair_list_min)
  pMin = second(pair_list_min)

print("print pMin")
print(pMin(inc)(0))

pList = lista
pMax = head(pList)
while isnil(pList) == false:  
  pair_list_max = lambMAXList(pair(pList)(head(pMax)))
  pList = first(pair_list_max)
  pMax = second(pair_list_max)

print("print pMax")
print(pMax(inc)(0))
