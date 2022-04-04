f = open('27-8a.txt')
n = int(f.readline())
max1 = 0
maxsum2 = 0
interv = []
for  i in range(1):
    interv.append(int(f.readline()))
for i in range(n-5):
    x = int(f.readline())
    if interv[0] > max1:
        max1 = interv[0]
    if max1+max1 + x*x > maxsum2:
        maxsum2 = max1+max1 + x*x
    print(max1,maxsum2)
