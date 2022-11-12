"""
MIN - recebe uma lista de números e retorna o menor deles.
MAX - recebe uma lista de números e retorna o maior deles.
APPEND - recebe duas listas e retorna a concatenação destas duas listas.
REVERSE - recebe uma lista e retorn a lista invertida.

"""

def printList(list):
  toprint = []
  while isnil(list) is false:
    toprint.append(head(list)(inc)(0))
    list = tail(list)
  print(toprint)


#lambda arguments : expression

zero = lambda f: lambda x :    x       #Lf.Lx. x
um = lambda f: lambda x :      f(x)      #Lf.Lx. f x
dois = lambda f: lambda x :    f(f(x)) #Lf.Lx. f( f x )
tres = lambda f: lambda x :    f(f(f(x))) #Lf.Lx. f( f x )
quatro = lambda f: lambda x :  f(f(f(f(x)))) #Lf.Lx. f( f x )
cinco = lambda f: lambda x :   f(f(f(f(f(x))))) #Lf.Lx. f( f x )
seis = lambda f: lambda x :    f(f(f(f(f(f(x)))))) #Lf.Lx. f( f x )
sete = lambda f: lambda x :    f(f(f(f(f(f(f(x))))))) #Lf.Lx. f( f x )
oito = lambda f: lambda x :    f(f(f(f(f(f(f(f(x)))))))) #Lf.Lx. f( f x )
nove = lambda f: lambda x :    f(f(f(f(f(f(f(f(f(x))))))))) #Lf.Lx. f( f x )

zero.__name__ = "zero"
um.__name__ = "um"
dois.__name__ = "dois"
tres.__name__ = "tres"
quatro.__name__ = "quatro"
cinco.__name__ = "cinco"
seis.__name__ = "seis"
sete.__name__ = "sete"
oito.__name__ = "oito"
nove.__name__ = "nove"

inc = lambda x : x+1

true = lambda a: lambda b : a      #La.Lb. a
false = lambda a: lambda b : b     #La.Lb. b
true.__name__ = "true"
false.__name__ = "false"

ou = lambda a: lambda b: a(a)(b) #lambda a, b: a(true,b)   #La.Lb. a a b
e = lambda a: lambda b: a(b)(a) #lambda a, b: a(b,false)   #La.Lb. a b a
nao = lambda p: p(false)(true) #Lp. p false true

se = lambda p: lambda a: lambda b: p(a)(b) #lambda a: a  #Lp.La.Lb. p a b

pair = lambda x: lambda y: lambda z : z(x)(y) #Lx. Ly. Lz. z x y
first = lambda p : p(true) #Lp. p(Lx. Ly. x) - Lx. Ly. x = true
second = lambda p : p(false) #Lp. p(Lx. Ly. y) - Lx. Ly. y = false

nil = pair(true)(true) # pair true true
isnil = lambda l: first(l) # Ll. first l
cons = lambda h: lambda t: pair(false)(pair(h)(t)) #Lh. Lt. pair false (pair h t)
head = lambda z : first(second(z)) #Lz. first (second z)
tail = lambda z : second(second(z)) #Lz. second (second z)

# Lf. (Lx. f(x x)) (Lx. f(x x))
# combY = lambda f: ((lambda x: f(x)(x)) (lambda x: f(x)(x))) # n roda

#rosettacode.org/wiki/Y_combinator
Y = lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args)))

func = lambda f: lambda x: (
  1
  if x == 1
  else
    x * f(x-1)
  )
fact = lambda x: Y(func)(x) # fatorial
# print(fact(5))

#https://ava.cefor.ifes.edu.br/pluginfile.php/2835351/mod_resource/content/1/tc-2022-09-29.pdf

succ = lambda n: lambda f: lambda v:(f((n (f)) (v))) # Ln. Lf. Lx.(f ((n f) x))
pc = lambda p:(pair(second (p))(succ ((second) (p)))) # λp.(PAIR (SECOND p) (SUCC (SECOND p))) = Lp.(pair (second p) (succ (second p)))
pred = lambda n:(first (n (pc) (pair (zero) (zero)))) # λn.(FIRST (n PC (PAIR 0 0))) = Ln. (first (n pc (pair 0 0)))
isZero = lambda x: x(false) (nao) (false) # λx.(x FALSE NOT FALSE)
leq = lambda m: lambda n: (isZero(n (pred) (m))) # λm.λn.(ISZERO (n PRED m)) - menor ou igual = Lm. Ln. (iszero ((n (pred) (m))))

lista = cons(um)(cons(dois)(cons(tres)(cons(quatro)(nil))))


# conversao da combY pythonica para lambda
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
    listaOriginal = first(par)
    listaNew = second(par)
    if (isnil(listaNew) == true) and (isnil(listaOriginal) == true) : #acabou o processamento das listas
      return nil # retorna o ultimo valor q é nil
    else:
      if isnil(listaOriginal) == false: # roda se nao chegou no final da lista original
        return cons(head(listaOriginal))(APPENDlist(pair(tail(listaOriginal))(listaNew))) # reduz o tamanho da lista original
      if isnil(listaNew) == false: # roda se nao chegou no final da lista nova
        return cons(head(listaNew))(APPENDlist(pair(listaOriginal)(tail(listaNew)))) # reduz o tamanho da lista nova

lista2 = cons(cinco)(cons(seis)(cons(sete)(cons(oito)(nil))))
print("lista 1:")
printList(lista)
print("lista 2:")
printList(lista2)
listaMesclada = APPENDlist(pair(lista)(lista2))
print("lista mesclada: ")
printList(listaMesclada)

def REVERSElist(lst):
  if (isnil(head(lst)) == true):
    return nil
  else:
    return APPENDlist(pair(REVERSElist(tail(lst)))(cons(head(lst))(nil))) # adiciona uma lista que esta sendo criada em uma "lista" gerada pela cabeça
    

listaReversed = REVERSElist(listaMesclada)
print("lista Revertida: ")
printList(listaReversed)

print("menor valor da lista: ",MINlist(pair(listaReversed)(head(listaReversed)))(inc)(0))
print("maior valor da lista: ",MAXlist(pair(listaReversed)(head(listaReversed)))(inc)(0))


# print("testando as funçoes")
# print(true(1)(0))
# print(false(1)(0))

# print("ou")
# print("true: ", ou(true)(false).__name__)  # true(true)(false) - true
# print("true: ", ou(false)(true).__name__)  # false(true)(true) - true
# print("false: ", ou(false)(false).__name__) # false(true)(false) - false
# print("true: ", ou(true)(true).__name__)   # true(true)(true) - true
# print("e")
# print("false: ", e(true)(false).__name__)
# print("false: ", e(false)(true).__name__)
# print("false: ", e(false)(false).__name__)
# print("true: ", e(true)(true).__name__)
# print("se")
# print("se(e)(true)(true) - true : ", se(e)(true)(true).__name__)
# print("se(e)(false)(true) - false: ", se(e)(false)(true).__name__)
# print("nao")
# print("not true: ", nao(true).__name__) # true(false,true) - false
# print("not false: ", nao(false).__name__) # false(false,true) - true

# print(" ------------ ")

# x = pair(32)(64)
# print(first(x))
# print(second(x))

# #https://sookocheff.com/post/fp/representing-pairs-and-lists-in-lambda-calculus/
# lista = cons(1)(cons(2)(cons(3)(cons(4)(nil))))
# toprint = []
# for _ in range(5):
#   toprint.append(head(lista))
#   lista = tail(lista)
#   if isnil(lista) is true:
#     break
# print(toprint)

# print(fact(5))

# print("succ um: ",succ(um)(inc)(0))
# print("leq um dois :",leq(um)(dois)(1)(0))
# print("leq dois um :",leq(dois)(um)(1)(0))
# print("leq um um :",leq(um)(um)(1)(0))

# print(isnil(lista)(1)(0))
# rabo = tail(tail(tail(tail(lista))))
# print(isnil(rabo)(1)(0))

# def isEnd(lst):
#   return isnil(lst)(1)(tail(lst))

# aux = isEnd(lista)
# print(aux)
# aux = isEnd(aux)
# print(aux)
# aux = isEnd(aux)
# print(aux)
# aux = isEnd(aux)
# print(aux)
# aux = isEnd(aux) # chegou no fim da lista e retornou 1
# print(aux)