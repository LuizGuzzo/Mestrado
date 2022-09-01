import utils; from utils import rf
from yesOnSelfApprox import yesOnSelfApprox
from yesOnStringApprox import yesOnStringApprox
from notYesOnSelfApprox import notYesOnSelfApprox


a = yesOnStringApprox(rf('longerThan1K.py'), rf('longerThan1K.py'))
b = yesOnStringApprox(rf('maybeLoop.py'), rf('maybeLoop.py'))
c = yesOnSelfApprox(rf('longerThan1K.py'))
d = notYesOnSelfApprox(rf('containsGAGA.py'))

print(a) # se o codigo longerThan1K.py tem mais do q 1k letras.. acho q nao.
print(b) # indefinido por entrar em loop eterno
print(c) # se longerthan1k, tem longerthan1k.. acho q nao tem
print(d) # NO, porque containsGAGA tem GAGA, porem a funcão é uma negacao do resultado