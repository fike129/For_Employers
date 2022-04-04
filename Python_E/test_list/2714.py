f = open('27-15b.txt')
n = int(f.readline())
ostatki = [0]*14
intervals = []
pari = 0
for i in range(6):
    intervals.append(int(f.readline()))
for i in range(n-6):
    ostatki[intervals[0] % 14] += 1
    x = int(f.readline())
    pari += ostatki[(14 - (x % 14))%14]
    for j in range(5):
        intervals[j] = intervals[j+1]
    intervals[5] = x
print(pari)