ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


# caracteresEspeciais = . * + ? ^ $ \ [
# caracteresEspeciaisColchetes = ] - ^

def matching(reg,txt):
    if reg is None:
        return 0
    if reg == "":
        return MatchEmpty(reg)
    # se a expressão é uma letra da linguagem, retorna 1


    return False


#[0-9]+

#armazena oque ve numa string dentro de um array
#viu colchetes vai pra funcao colchete
#viu plus armazena a copia da funcão anterior e repete ela

def colchetes(txt): #sets
    # cria um array armazenando os valores que ve
    # encontrou -, joga na funçao hifen, passando txt[i-1],txt[i+1]
    # encontrou ]
    # retorna o array de possibilidades (da um extend no array principal)
    ## deveria verificar se tem dado repetido?
    return

def hifen(conjX,conjY):
    # consulta a posição q esta no dicionario A-Z, a-z e 0-9
    # retorna um array com os valores de intervalo entre x e y
    return

def negacao():

    return

def ou():
    # e = (e'|e")
    return

def e():
    # e = (e')(e")
    # e = e' e"
    return

def estrela():
    # e = (e')*
    return
