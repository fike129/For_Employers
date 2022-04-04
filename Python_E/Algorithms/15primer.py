def task15(x,A):
    return x&A != 0 <= (x&36 == 0 <= x&6 != 0)

for A in range(0,1000):
    podA = True
    for x in range(0,1000):
        if task15(x,A) == False:
            podA = False
            break
    if podA == True:
        print(A)



