s = 7* 729**220 - 6 * 81**200 + 9**210 - 80
otvet = 0
while s > 0:
    if s % 9 == 0:
        otvet += 1
    s = s // 9
print(otvet)