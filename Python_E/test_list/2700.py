f = open('27-12b.txt')
n = int(f.readline())
k6 = 0
k2 = 0
k3 = 0
for i in range(n):
    x = int(f.readline())
    if x % 6 == 0:
        k6 += 1
    elif x % 2 == 0:
        k2 += 1
    elif x % 3 == 0:
        k3 += 1
print(k6*(n- k6) + k6*(k6-1)//2 + k2*k3)
