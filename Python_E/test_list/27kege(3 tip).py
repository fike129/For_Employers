f = open('27-28b_5XuYtUR.txt')
n = int(f.readline())
min_razn = 100001
sum_final = 0
for i in range(n):
    a,b = map(int, f.readline().split())
    sum_final += min(a,b)
    if abs(a-b) < min_razn and abs(a-b) % 8 != 2:
        min_razn = abs(a-b)
if sum_final % 8 == 2:
    print(sum_final+min_razn)
else:
    print(sum_final)

#19751921