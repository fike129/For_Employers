f = open('27-13b.txt')
n = int(f.readline())
k14 = k2 = k7 = k = 0
intervals = []
pari = 0
for i in range(6):
    intervals.append(int(f.readline()))
for i in range(n-6):
    x = int(f.readline())
    if intervals[0] % 14 == 0:
        k14 += 1
    elif intervals[0] % 2 == 0:
        k2 += 1
    elif intervals[0] % 7 == 0:
        k7 += 1
    else:
        k += 1
    if x % 14 == 0:
        pari += k14 + k7 + k2 + k
    elif x % 7 == 0:
        pari += k2 + k14
    elif x % 2 == 0:
        pari += k14 + k7
    else:
        pari += k14
    for j in range(5):
        intervals[j] = intervals[j+1]
    intervals[5] = x
print(pari)
