def F(n):
    if n <= 1:
        return 1
    if n > 1 and n % 2 == 0:
        return 3 + F(n // 2 - 1)
    if n > 1 and n % 2 == 1:
        return 10000000000
n = 1
while F(n) != 19:
    n += 1
print(n)