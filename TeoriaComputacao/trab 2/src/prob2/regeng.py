import sys

# info: tabela ASCII de simbolos vai de 33 até 126

def negateRange(start,end): # fazer os estados que nao deveria entrar e deixa-los presos
	# para que caso entre nesses estados eles deem erro
	out = ['(']

	for s in range(ord(start), ord(end)) : # roda o tamanho do range
		out.append('^')
		out.append(chr(s))
		out.append('|')
	
	out.append('^')
	out.append(end)
	return out

def makeRange(start, end):
	out = ['(']
	
	for s in range(ord(start), ord(end)) : # roda o tamanho do range
		out.append(chr(s))
		out.append('|')
	
	out.append(end)
	
	return out

def preProcess(expr : str) -> list:
	"""
	A função "preProcess" tem complexidade O(n) pois ela itera sobre a expressão
	regular de entrada e adiciona caracteres a saída na saida também é adicionado:
	operadores de concatenação quando os requisitos dele são atendidos, e
	é expandido as expressões de Range como por exemplo o [1-5] vira (1|2|3|4|5), para atender todos os estados.
	Nesse caso, n é o tamanho da expressão regular de entrada.
	"""

	#add © (NFA Concat operator)
	#add range
	out = []
	i = 0

	while i < len(expr) : # @@ roda len(expr)
		
		if expr[i] == '[': # se for [a-b] é o range
			if expr[i+1] == '^': # se for [^a-b] é o range negado
				start = expr[i+2]
				end = expr[i+4]
				
				out += negateRange(start, end) # entrega um grupo, se era [^1-5], retona (^1|^2|^3|^4|^5)
				i += 5
			else:
				start = expr[i+1]
				end = expr[i+3]
				
				out += makeRange(start, end) # entrega um grupo, se era [1-5], retona (1|2|3|4|5)
				i += 4
			
		else :
			if expr[i] != ']':
				out.append(expr[i])
			else:
				out.append(')')

			# out.append(expr[i] if expr[i] != ']' else ')')

			if expr[i] in {'(', '|'} :
				i += 1; continue
	
			elif i < len(expr) - 1 :
				if expr[i+1] not in {'*', '?', '+', ')', '|', ']'} : # se nao for simbolo especial, concatena
					out.append('©')					
			i += 1			

	return out

#operator precedence table

"""
It supports:

Concatenation,
Union (|),
Closure (*),
One or More (+),
Zero or One (?) ,
Grouping (( )) and
Range ([start-end]) regex operators.

"""

Precedence = {
	'|' : 0, #NFA Union Operator
	'^' : 1, #NFA negate operator - é o concat só que com estado falho
	'©' : 1, #NFA Concat Operator - renomeado para o simbolo '©' porque o '.' agora é a wildcard
	'?' : 2, #NFA zero or one Operator
	'*' : 2, #NFA Closure Operator
	'+' : 2  #NFA one or more Operator
}

# todo:
# ^ = começo de linha -> após toda a AFND criada concatene a expressao do ^ no inicio da AFND
# $ = final de linha -> após toda a AFND criada concatene a expressao do $ no final da AFND
# . = qlqr caractere menos "newLine" -> cria um estado que recebe epsilon apenas (ideia..)
# \(...\) = começo e final de grupo - ou seja oque ta dentro é uma sequencia (ab)* é "ab" zero ou + vezes
# [...] = qlqr caractere dentro - ou seja [abc] é "a|b|c"
# [^...] = qlqr caractere menos os que estao dentro -> fazer uma AFN que caso entre nesses estados da erro [Nao funciona]
# [a-z] = qlqr caractere entre a e z
# \ = torna o proximo simbolo um simbolo nao uma expressao

def toPosfix(expr : list) -> str:
	"""
	A função "toPosfix" tem complexidade O(n) pois ela itera sobre a expressão regular 
	de entrada previamente expandida (adicionado os concat e os estados do range),
	adicionando caracteres a uma lista de saída e empilhando-os na pilha.
	basicamente ele organiza a ordem dos simbolos para proxima etapa.
	Nesse caso, n é o tamanho da expressão regular de entrada.
	"""
	
	out, stack = [], []
	
	for symb in expr : # O(M) M = expressao regular
		if symb == '(' :
			stack.append(symb)
		
		elif symb == ')' :
			try :
				while stack[-1] != '(' :
					out.append(stack.pop())
			except IndexError:
				#if IndexError, then there are some missing parentheses
				sys.stderr.write("Invalid regex pattern.\n")
				sys.exit(64)						
			else : 
				stack.pop() #pop '('
					
		elif symb in {'+', '*', '?', '©', '|', "^"} :
			# se for ^?
			while len(stack) > 0 :
				if stack[-1] == '(' : # se nao acabou o grupo
					break
				elif Precedence[symb] > Precedence[stack[-1]] :
					break
				else : 
					out.append(stack.pop())
			
			stack.append(symb)			
		
		else :
			out.append(symb)
	
	while len(stack) > 0 :
		out.append(stack.pop())
	
	return "".join(out)

class State :
	def __init__(self, isEnd : bool) :
		self.isEnd =  isEnd
		self.transition = {}
		self.epsilonTransitions = []
	
	def addEpsilonTransition(self, to) :
		self.epsilonTransitions.append(to)
	
	def addTransition(self, to, symbol) :
		self.transition[symbol] = to

class NFA :
	def __init__(self, start : State, end : State) :
		self.start = start
		self.end = end

def fromEpsilon() -> NFA:
	start = State(False)
	end = State(True)
	start.addEpsilonTransition(end)
	
	return NFA(start, end)

def fromSymbol(symbol) -> NFA:
	start = State(False)
	end = State(True)
	start.addTransition(end, symbol)
	# e se for um wildcard?
	
	return NFA(start, end)

def concatenate(first : NFA, second : NFA) -> NFA:
	first.end.addEpsilonTransition(second.start)
	first.end.isEnd = False

	return NFA(first.start, second.end)

def union(first : NFA, second : NFA) -> NFA:
	start = State(False)
	start.addEpsilonTransition(first.start)
	start.addEpsilonTransition(second.start)

	end = State(True)
	first.end.addEpsilonTransition(end)
	first.end.isEnd = False	
	second.end.addEpsilonTransition(end)
	second.end.isEnd = False

	return NFA(start, end)

def closure(nfa : NFA) -> NFA:
	start = State(False)
	end = State(True)

	start.addEpsilonTransition(nfa.start)
	start.addEpsilonTransition(end)

	nfa.end.addEpsilonTransition(nfa.start)
	nfa.end.addEpsilonTransition(end)
	nfa.end.isEnd = False
	
	return NFA(start, end)

def oneOrMore(nfa : NFA) -> NFA:
	start = State(False)
	end = State(True)

	start.addEpsilonTransition(nfa.start)

	nfa.end.addEpsilonTransition(nfa.start)
	nfa.end.addEpsilonTransition(end)
	nfa.end.isEnd = False
	
	return NFA(start, end)

def zeroOrOne(nfa : NFA) -> NFA:
	start = State(False)
	end = State(True)

	start.addEpsilonTransition(nfa.start)
	start.addEpsilonTransition(end)

	nfa.end.addEpsilonTransition(end)
	nfa.end.isEnd = False
	
	return NFA(start, end)

def negate(nfa:NFA) -> NFA:

	nfa.start.isEnd = True
	nfa.end.isEnd = False # altera para estado falho
	
	return NFA(nfa.start, nfa.start)


def toNFA(posfixExpr : str) -> NFA:
	"""
	A função toNFA é responsável por construir o NFA a partir da expressão regular na notação posfix. 
	Ela faz isso iterando sobre cada caractere na expressão posfix e, para cada caractere, realiza operações 
	de pilha, como push e pop, para construir o NFA. Isso resulta em uma complexidade O(N), onde N é o 
	comprimento da expressão regular na notação posfix.
	"""
	if(posfixExpr == '') :
		return fromEpsilon()
	
	stack = [] #stack of NFAs
	
	try :
		for symb in posfixExpr : # O(N) N = expressao regular (alterada a posicao apenas)
			if symb == '*' :	
				stack.append(closure(stack.pop()))
			elif symb == '+' :
				stack.append(oneOrMore(stack.pop()))
			elif symb == '?':
				stack.append(zeroOrOne(stack.pop()))			
			elif symb == '|':
				right = stack.pop()
				left = stack.pop()
				stack.append(union(left, right))
			elif symb == '©' :
				right = stack.pop()
				left = stack.pop()
				stack.append(concatenate(left, right))
			elif symb == "^": # o start vira estado final e o end para de ser final.
				stack.append(negate(stack.pop()))
			else :
				stack.append(fromSymbol(symb))
				# adicionar o wildcard
	
	except IndexError: 
		#if indexError, then the NFA could not be built correctly
		sys.stderr.write("Invalid regex pattern.\n")
		sys.exit(64)
	else :
		return stack.pop()

def setNextState(state : State, nextStates : list, visited : list) :
	
	if len(state.epsilonTransitions) > 0 :
		for stt in state.epsilonTransitions:
			if not stt in visited :
				visited.append(stt)
				setNextState(stt, nextStates, visited)
	else :
		nextStates.append(state)

def search(nfa : NFA, word : str) -> bool :
	"""
	A função search é responsável por percorrer a NFA que era uma expressão regular, e comparando a NFA com a string de entrada.
	Ela faz isso iterando sobre cada caractere na string de entrada e, para cada caractere,
	verifica todos os estados atuais e seus estados de transição. Isso resulta em uma complexidade O(M*N),
	onde M é o comprimento da string de entrada e N é o número de estados no NFA.
	"""
	current = []
	setNextState(nfa.start, current, [])
	
	for symbol in word : # O(M*N) M = tamanho Texto ; N = NFA
		nextStates = []
		
		for state in current :
			if symbol in state.transition:
				setNextState(state.transition[symbol], nextStates, [])
		
		current = nextStates
	
	for state in current:
		if state.isEnd :
			return True
	
	return False

class Regex :
	def __init__(self, expr : str) :
		prepos = preProcess(expr) # O(n)
		expr = toPosfix(prepos) # O(n) - sendo q N é a expressão ja expandida do prepos
		self.nfa = toNFA(expr) # O(n) - N é a expressão em ordenação do "posfix"

	def match(self, word : str) -> bool:
		return search(self.nfa, word) # O(mn) - sendo M o texto e N a NFA

		# para calcular a complexidade basta somar todas essas funçoes)
		# daria algo proximo de O(MN + 3N)

#'ab|c|c^d^|e^|f^|©'
#'ab|c|cd|e|f|©'
# r = Regex('[a-c][^c-f]') 
# r = Regex('([^a-c]|_)([c-f]|[0-9])*')

# r.match('') #False
# r.match('identifer') #True
# r.match('987c') #False
# r.match('_usr501132') #True
