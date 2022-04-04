f = open('24_13_gzqwOO1.txt')
s = f.readline()
slov = {}
for i in range(len(s)):
    if s[i] == 'X':
        if slov.get(s[i+1], 0) != 0:
            slov[s[i+1]] += 1
        else:
            slov[s[i+1]] = 1
max_final = [0, '']
for key in slov.keys():
    if slov[key] > max_final[0]:
        max_final[0] = slov[key]
        max_final[1] = key
print(max_final)
