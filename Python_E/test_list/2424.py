# f = open('24-11_GOozfED.txt')
# s = f.readline()
# otvet = [s[0]]
# otvet_final = ''
# for i in range(len(s)-1):
#     if s[i+1] >= s[i]:
#         otvet = otvet + s[i+1]
#         if len(otvet) > len(otvet_final):
#             otvet_final = otvet
#     else:
#         otvet = s[i+1]
# print(otvet_final)

f = open('24-12_EH4e1UJ.txt')
s = f.readline()
count = 0
for s in f:
    countK = 0
    countU = 0
    for i in range(len(s)):
        if s[i] == 'K':
            countK += 1
        if s[i] == 'U':
            countU += 1
    if countK > countU:
        count += 1
print(count)


