f = open('27-B_1.txt')
n = int(f.readline())
sum_fin = 0
min_razn = 1000001
for i in range(n):
    a,b = map(int, f.readline().split())
    sum_fin += max(a,b)
    if abs(a-b) < min_razn and abs(a-b) % 3 != 0:
        min_razn = abs(a-b)
if sum_fin % 3 == 0:
    print(sum_fin - min_razn)
else:
    print(sum_fin)
#127127
#399762080