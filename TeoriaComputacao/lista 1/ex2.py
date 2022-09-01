def oooops(inp):
    try:
        val = int(inp)
    except ValueError:
        val = len(inp)
    s = 'A'
    i = 0
    while i != val:
        # print("i: {}".format(i,s))
        s += inp[2]
        i += 1
    return s

inputs = ["abc","abcdefghij","a","008","8","-11"]

for i,txt in enumerate(inputs):
    try:
        res = oooops(txt)
    except Exception as e:
        res = e
    print("{}: {}".format(i,res))

# F da loop infinito
# falta responder a G