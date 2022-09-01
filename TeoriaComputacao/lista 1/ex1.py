def sumSlicer(texto,pos):
    lista_texto = texto.split(" ")
    sum = 0
    for i, slice in enumerate(lista_texto):
        if (i+1) % pos == 0:
            sum += int(slice)

    return sum

def decisionProgram(texto):
    if sumSlicer(texto,3) > sumSlicer(texto,2):
        return True
    else:
        return False


txt = "58 41 78 3 25 9" #entrada
a = sumSlicer(txt,2)
b = sumSlicer(txt,3)

print("a: ",a)
print("b: ",b)

c = decisionProgram(txt)
print("c: ",c)