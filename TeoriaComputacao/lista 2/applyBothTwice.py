# funcao universal e ESS foram copiadas do livro "WhatCanBeComputed" (pag 105)
def universal(progString, inString):
    # Execute the definition of the function in progString. This defines
    # the function, but doesn’t invoke it.
    exec(progString)
    # Now that the function is defined, we can extract a reference to it.
    progFunction = utils.extractMainFunction(progString)
    # Invoke the desired function with the desired input string.
    return progFunction(inString)

def ESS(str1,str2):
    return "{} {}{}".format(len(str1),str1,str2)

def DESS(str):
    num = int(str.split(" ")[0])
    newstr = str[str.find(" ")+1:]
    return newstr[:num],newstr[num:]

def applyBothTwice(string):
    string,I = DESS(string)
    P,Q = DESS(string)
    print("P:{} Q:{} I:{}".format(P,Q,I))
    return universal(Q,universal(P,universal(Q,universal(P,I))))


string = ESS("program_P","program_Q")
string = ESS(string,"input_I")
print(string)
applyBothTwice(string) # nao funciona pq nao tem as funçoes P e Q definidas.