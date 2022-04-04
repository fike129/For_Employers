from itertools import product
count_otvet = 0
for i in product('ПИРОГ', repeat=5):
    if i.count('P') == 1:
        if i.index('P') != 4:
            if i[i.index('P')+1] in 'ИО':
                count_otvet += 1
print(count_otvet)