# f = open('27-30b.txt')
# n = int(f.readline())
# sum_final = 0
# min_raz = 1000001
# for i in range(n):
#     a = list(map(int, f.readline().split()))
#     a.sort()
#     sum_final += a[0]
#     if (a[2] - a[0]) < min_raz and (a[2] - a[0]) % 7 != 0:
#         min_raz = a[2] - a[0]
#
#     if (a[1] - a[0]) < min_raz and (a[1] - a[0]) % 7 != 0:
#         min_raz = a[1] - a[0]
#
# if sum_final % 7 == 0:
#     sum_final += min_raz
# print(sum_final)

f = open('27-2b.txt')
n = int(f.readline())
sum_final = 0
m_ost = [100001]*3
m_ost1 = [100001]*3

for i in range(n):
    a,b = map(int, f.readline().split())
    sum_final += max(a,b)

    if abs(a-b) % 3 != 0:
        for ost in range(1,3):
            k = (abs(a-b) + m_ost[ost]) % 3
            m_ost1[k] = min(m_ost[k], (abs(a-b) + m_ost[ost]))

    if abs(a-b) < m_ost[abs(a-b)%3]:
        m_ost1[abs(a-b)%3] = abs(a-b)
    m_ost = m_ost1

if sum_final % 3 != 0:
    sum_final -= m_ost[sum_final % 3]
print(sum_final)
