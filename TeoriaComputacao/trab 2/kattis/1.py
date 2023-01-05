"""
Exercicio: https://open.kattis.com/problems/interactivetictactoe

first
...
...
...

W
...
.x.
...

R
.o.
.x.
...

20 - se o programa joga um jogo valido
25 - se nunca perde um jogo
30 - sempre ganha se for possivel
25 - nunca perde um jogo e sempre ganha se possivel

If you output a grid where you win or play a draw your program should terminate.
If you read a grid where Mårten won or drew your program should terminate.

Marten é bolinha (o) e ele sempre ganha
Preciso fazer uma IA que ganhe dele, vou chamar de Netram
"""
from random import randrange
from math import inf
from os import system
import platform

MARTEN = -1 # IA do Kattis : O
NETRAM = +1 # minha IA - é a q espero que vença : X
    
def minimax(mesa,depth,jogador):
    # Referencia: https://github.com/Cledersonbc/tic-tac-toe-minimax
    if jogador == NETRAM:
        best = [-1,-1,-inf]
    else:
        best = [-1,-1,+inf]

    if depth == 0 or game_over(mesa):
        score = valida(mesa)
        return [-1,-1,score]

    for celula in celulas_vazias(mesa):
        x,y = celula[0], celula[1]
        mesa[x][y] = jogador
        score = minimax(mesa,depth-1,-jogador)
        mesa[x][y] = 0
        score[0],score[1] = x,y

        if jogador == NETRAM:
            if score[2] > best[2]:
                best = score # maior valor
        else:
            if score[2]< best[2]:
                best = score # menor valor
        

    return best

def game_over(mesa):
    return vencedor(mesa,NETRAM) or vencedor(mesa,MARTEN) or check_tilt(mesa)

def check_tilt(mesa): # checar se tem mais X q O (caçando problema de n ta rodando)
    qX = 0
    qO = 0
    for linha in mesa:
        for celula in linha:
            if celula == -1: # O
                qO += 1
            if celula == 1: # X
                qX += 1
    
    if -1 <= (qO - qX) <= 1:
        return False
    else:
        return True

def celulas_vazias(mesa):
    celulas_vazias = []
    for x in range(len(mesa)):
        for y in range(len(mesa[x])):
            if mesa[x][y] == 0:
                celulas_vazias.append([x,y])
    return celulas_vazias

def vencedor(mesa,jogador):
    for i in range(3):
        #checando linhas
        if mesa[i][0] == mesa[i][1] == mesa[i][2] == jogador:
            return True
        #checando colunas
        if mesa[0][i] == mesa[1][i] == mesa[2][i] == jogador:
            return True
    
    #checando diagonais
    if mesa[0][0] == mesa[1][1] == mesa[2][2] == jogador:
        return True
    if mesa[0][2] == mesa[1][1] == mesa[2][0] == jogador:
        return True

    return False

def valida(mesa):
    if vencedor(mesa,MARTEN):
        return -1
    elif vencedor(mesa,NETRAM):
        return +1
    else:
        return 0

def netram_turno(mesa):
    depth = len(celulas_vazias(mesa))
    if depth == 0 or game_over(mesa):
        return mesa
    
    if depth == 9:
        x,y = randrange(3),randrange(3)
    else:
        x,y,_ = minimax(mesa,depth,NETRAM)
    
    mesa[x][y] = NETRAM

    # print("")
    # print("netram turn")
    imprime_mesa(mesa)
    
    return mesa

def matren_turno_leitura(mesa):
    if len(celulas_vazias(mesa))==0 or game_over(mesa):
        return mesa

    # lendo mesa por input
    dict = {
        ".": 0,
        "o": -1,
        "x": 1
    }

    # print("")
    # print("matren turn")
    
    
    for i in range(3):
        linha = str(input())
        mesa[i] = [dict[linha[0]],dict[linha[1]],dict[linha[2]]]

    return mesa

def imprime_mesa(mesa):
    dict = {
        0: ".",
        -1: "o",
        1: "x"
    }


    for linha in mesa:
        for celula in linha:
            letra = dict[celula]
            print(f'{letra}',end='')
        print('')

    # for i in range(len(mesa)):
    #     s = dict[mesa[i][0]] dict[mesa[i][1]] dict[mesa[i][2]]
        # print(s)


move = input()
mesa = [[0,0,0],[0,0,0],[0,0,0]]
# leio a ordem de inicio - first: eu movo primeiro - second: oponente move primeiro
while len(celulas_vazias(mesa))>0 and not game_over(mesa):
    if move == "first":
        #imprime branco
        # imprime_mesa(mesa)
        for i in range(3):
            trash = input() # queimando o input pq ja to com a mesa limpa

        mesa = netram_turno(mesa)
        move = ""
    elif move == "second":
        #imprime a mesa do movimento do oponente
        mesa = matren_turno_leitura(mesa) # lendo a mesa
        #output a grid with the move you perfomed
        mesa = netram_turno(mesa)
        move = ""
    
    #le a mesa
    #output a mesa com oq vc fez
    mesa = matren_turno_leitura(mesa)
    mesa = netram_turno(mesa)

# print("FIM DE JOGO")

# loop enquanto tiver espaço na mesa E nao for fim de jogo
    # muda conforme inicio - turno do Mårten
    # meu turno
    # turno Marten

