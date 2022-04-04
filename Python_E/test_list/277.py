f = open('27-6b.txt')
n = int(f.readline())
m6,m = 0,0
for i in range(n):
    x = int(f.readline())
    if x % 6 == 0 and x > m6:
        if m6 > m:
            m = m6
        m6 = x
    elif x > m:
        m = x
print(m*m6)