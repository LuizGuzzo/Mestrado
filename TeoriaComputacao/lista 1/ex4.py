# Como indicado na Figura 3.3 do livro “What Can Be Computed?”, a saída do comando
# containsGAGA(rf('containsGAGA.py')) é “yes”. Escreva uma nova versão deste programa, chamada containsGA_GA.py.
# Essa nova versão deve ser equivalente à antiga,
# i.e., produzir as mesmas respostas para as mesmas entradas. Além disso os comandos
# containsGA_GA(rf('containsGA_GA.py')) e containsGAGA(rf('containsGA_GA.py'))
# devem ambos retornar “no”.

from containsGA_GA import containsGA_GA
from containsGAGA import containsGAGA

containsGAGAtxt = open("containsGAGA.py","r").read()
containsGA_GAtxt = open("containsGA_GA.py","r").read()

print(containsGA_GA(containsGAGAtxt)) #deveria sair yes
print(containsGAGA(containsGAGAtxt)) #deveria sair yes
print("respostas aceitas: NO NO")
print(containsGA_GA(containsGA_GAtxt)) #deve sair no
print(containsGAGA(containsGA_GAtxt)) # deve sair no
