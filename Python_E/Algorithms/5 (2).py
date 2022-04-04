for i in range(1,10000):
    x = i
    L = 0
    M = 0
    while x > 0:
        L = L + 1
        if x % 2 == 0:
           M = M + x % 10
        x = x//10
    if (L,M) == (4,8):
         print(i) 