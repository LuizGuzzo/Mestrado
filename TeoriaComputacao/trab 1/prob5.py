"""
MIN - recebe uma lista de números e retorna o menor deles.
MAX - recebe uma lista de números e retorna o maior deles.
APPEND - recebe duas listas e retorna a concatenação destas duas listas.
REVERSE - recebe uma lista e retorn a lista invertida.

"""

# https://users.monash.edu/~lloyd/tildeFP/Lambda/Examples/list/
"""
append = lambda L1. lambda L2.
    if null L1 then L2
    else (hd L1) :: (append (tl L1) L2)


reverseS = lambda L.
  if null L then nil
  else append (reverseS tl L) (hd L :: nil)

"""

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

print("ou")
print("true: ", ou(true)(false).__name__)  # true(true)(false) - true
print("true: ", ou(false)(true).__name__)  # false(true)(true) - true
print("false: ", ou(false)(false).__name__) # false(true)(false) - false
print("true: ", ou(true)(true).__name__)   # true(true)(true) - true
print("e")
print("false: ", e(true)(false).__name__)
print("false: ", e(false)(true).__name__)
print("false: ", e(false)(false).__name__)
print("true: ", e(true)(true).__name__)
print("se")
print("se(e)(true)(true) - true : ", se(e)(true)(true).__name__)
print("se(e)(false)(true) - false: ", se(e)(false)(true).__name__)
print("nao")
print("not true: ", nao(true).__name__) # true(false,true) - false
print("not false: ", nao(false).__name__) # false(false,true) - true

pair = lambda x: lambda y: lambda z : z(x)(y) #Lx. Ly. Lz. z x y
first = lambda p : p(true) #Lp. p(Lx. Ly. x) - Lx. Ly. x = true
second = lambda p : p(false) #Lp. p(Lx. Ly. y) - Lx. Ly. y = false

nil = pair(true)(true)
isnil = first
cons = lambda h: lambda t: pair(false)(pair(h)(t)) #Lh. Lt. pair false (pair h t)
head = lambda z : first(second(z)) #Lz. first (second z)
tail = lambda z : second(second(z)) #Lz. second (second z)

# Lf. (Lx. f(x x)) (Lx. f(x x))
# combY = lambda f: ((lambda x: f(x)(x)) (lambda x: f(x)(x))) # n roda

#rosettacode.org/wiki/Y_combinator
Y = lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args)))

func = lambda f: lambda x: (1 if x == 1 else x * f(x-1))
fact = lambda x: Y(func)(x) # fatorial

#https://ava.cefor.ifes.edu.br/pluginfile.php/2835351/mod_resource/content/1/tc-2022-09-29.pdf

succ = lambda f: lambda v:(f((n (f)) (v))) # Lf. Lx.(f ((n f) x))
pc = lambda p:(pair(second (p))(succ ((second) (p)))) # λp.(PAIR (SECOND p) (SUCC (SECOND p))) = Lp.(pair (second p) (succ (second p)))
pred = lambda n:(first (n (pc) (pair (0) (0)))) # λn.(FIRST (n PC (PAIR 0 0))) = Ln. (first (n pc (pair 0 0)))
isZero = lambda x: x(false) (nao) (false) # λx.(x FALSE NOT FALSE)
leq = lambda m: lambda n: (isZero(n (pred) (m))) # λm.λn.(ISZERO (n PRED m)) - menor ou igual = Lm. Ln. (iszero ((n (pred) (m))))

lista = cons(1)(cons(2)(cons(3)(cons(4)(nil))))
# lista = cons(um)(cons(dois)(cons(tres)(cons(quatro)(nil))))
# print("leq one two :",leq(um)(dois))

print(um.__name__)
print("succ 2:", succ(um).__name__)


# codigo inicial
# # first(par) = list | second(par) = value
# minList = lambda f: lambda par: (
#   lista = first(par)
#   minValue = second(par)
#   if isnil(first(par)) == true: # der true executa apenas a proxima execuçao, por entre () os outros
#     return minValue # second(par)
#   else:# se deu false vai rodar aqui
#     val = head(lista)
#     if val < minValue: # isZero(subtracao(minValue)(val)) #vai dar true ou false
#       minValue = val # (f(pair(tail(lista))(head(lista))))
#     f(pair(tail(lista))(minValue)) # (f(pair(tail(lista))(second(par))))
# )


# tentativa de transforma-lo em lambda calculo
# minList = lambda f: lambda par: (
#   (isnil(first(par)) # se chegou no final da lista
#     (second(par)) # retorna o minimo que esta no par
#     ((leq(second(par))(head(first(par)))) # se o minimo que esta no par é menor do que esta na cabeça da lista
#       (f(pair(tail(first(par)))(second(par)))) # chama a função diminuindo a lista e passando no par o valor que esta NO PAR
#       (f(pair(tail(first(par)))(head(first(par))))) # chama a função diminuindo a lista e passando no par o valor que esta NA CABEÇA DA LISTA
#     )
#   )
# ) 

# para o maxList é repetir o anterior e trocar os parametros do leq, mantendo sempre o maior no pair


# append = lambda f: lambda par: (
#   listaOld = first(par)
#   listaNew = second(par)
#   if isnil(listaOld): #acabou o processamento da listaOld
#     return listaNew
#   else:
#     #cria um nó e adiciona a cabeça do listaNew no tail do listaOld
# )

# reverse = lambda f: lambda par: (
#   listaOg = first(par) # lista original
#   listaRv = second(par) # lista revertida
#   if isnil(listaOld): #acabou o processamento da lista original
#     return listaNew
#   else:
#     # da um append da calda do listOg na listaRv
# )



# MIN = lambda lst: Y(minList)(pair(lst)(head(lst)))

# print(MIN(lista))




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

