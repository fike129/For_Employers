from itertools import*
otvet = 0
for i in product('ВИШНЯ',repeat=7):
    if i.count('Ш') <= 1 and i[0] != 'H' and i[i] in 'ИЯ':
        otvet += 1
print(otvet)