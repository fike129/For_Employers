def graf(x,y,A):
    return (y + 5*x < A) or (3*x + 2*y > 80)
for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not graf(x, y, A):
                flag = False
                break
        if not flag:
            break
    if flag:
        print(A)