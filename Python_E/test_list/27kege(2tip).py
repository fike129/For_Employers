f = open('27-23b.txt')
n = int(f.readline())
min_razn = 100001
sum_final = 0
for i in range(n):
    a,b = map(int, f.readline().split())
    sum_final += max(a,b)
    if abs(a-b) < min_razn and abs(a-b) % 10 != 5:
        min_razn = abs(a-b)
if sum_final % 10 == 5:
    print(sum_final-min_razn)
else:
    print(sum_final)
    #13159
    #40799379
