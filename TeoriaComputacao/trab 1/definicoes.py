# definicoes das funçoes lambdas e seus correspondentes na linguagem do lambster a direita em comentario.

zero = lambda f: lambda x :    x                            #Lf.Lx. x
um = lambda f: lambda x :      f(x)                         #Lf.Lx. f(x)
dois = lambda f: lambda x :    f(f(x))                      #Lf.Lx. f(f(x))
tres = lambda f: lambda x :    f(f(f(x)))                   #Lf.Lx. f(f(f(x)))
quatro = lambda f: lambda x :  f(f(f(f(x))))                #Lf.Lx. f(f(f(f(x))))
cinco = lambda f: lambda x :   f(f(f(f(f(x)))))             #Lf.Lx. f(f(f(f(f(x)))))
seis = lambda f: lambda x :    f(f(f(f(f(f(x))))))          #Lf.Lx. f(f(f(f(f(f(x))))))
sete = lambda f: lambda x :    f(f(f(f(f(f(f(x)))))))       #Lf.Lx. f(f(f(f(f(f(f(x)))))))
oito = lambda f: lambda x :    f(f(f(f(f(f(f(f(x))))))))    #Lf.Lx. f(f(f(f(f(f(f(f(x))))))))
nove = lambda f: lambda x :    f(f(f(f(f(f(f(f(f(x))))))))) #Lf.Lx. f(f(f(f(f(f(f(f(f(x)))))))))

# nomes dados para ao retornar ter nomes em vez de apenas funçoes lambdas
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

inc = lambda x : x+1 # utilizado nos prints para visualizar os valores ao rodar (func)(inc)(0)

true = lambda a: lambda b : a      #La.Lb. a
false = lambda a: lambda b : b     #La.Lb. b
true.__name__ = "true"
false.__name__ = "false"

ou = lambda a: lambda b: a(a)(b) #La.Lb. a a b
e = lambda a: lambda b: a(b)(a) #La.Lb. a b a
nao = lambda p: p(false)(true) #Lp. p false true

se = lambda p: lambda a: lambda b: p(a)(b) #Lp.La.Lb. p a b

pair = lambda x: lambda y: lambda z : z(x)(y) #Lx. Ly. Lz. z x y
first = lambda p : p(true) #Lp. p(true)
second = lambda p : p(false) #Lp. p(false)

nil = pair(true)(true) # pair true true
isnil = lambda l: first(l) # Ll. first l
cons = lambda h: lambda t: pair(false)(pair(h)(t)) #Lh. Lt. pair false (pair h t)
head = lambda z : first(second(z)) #Lz. first (second z)
tail = lambda z : second(second(z)) #Lz. second (second z)

# retirado de: rosettacode.org/wiki/Y_combinator
Y = lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args))) # Lf. (Lx. f(x x)) (Lx. f(x x))

# retirado de: https://ava.cefor.ifes.edu.br/pluginfile.php/2835351/mod_resource/content/1/tc-2022-09-29.pdf

succ = lambda n: lambda f: lambda v:(f((n (f)) (v))) # Ln. Lf. Lx.(f ((n f) x))
pc = lambda p:(pair(second (p))(succ ((second) (p)))) # Lp. (pair (second p) (succ (second p)))
pred = lambda n:(first (n (pc) (pair (zero) (zero)))) # Ln. (first (n pc (pair 0 0)))
isZero = lambda x: x(false) (nao) (false) # Lx. (x FALSE NOT FALSE)
leq = lambda m: lambda n: (isZero(n (pred) (m))) # Lm. Ln. (iszero ((n (pred) (m))))


lista = cons(um)(cons(dois)(cons(tres)(cons(quatro)(nil))))
lista2 = cons(cinco)(cons(seis)(cons(sete)(cons(oito)(nil))))




def printList(list):
  toprint = []
  while isnil(list) is false:
    toprint.append(head(list)(inc)(0))
    list = tail(list)
  print(toprint)