# exercicio: https://open.kattis.com/problems/different
# virou easy...

while(True):
    try:
        AB = input().split()
        A = int(AB[0])
        B = int(AB[1])
        if (A>B):
            print(A-B)
        else:
            print(B-A)
    except:
        break
