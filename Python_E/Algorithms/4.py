f = open('1.txt')
s = f.readline()
count = 0
count_final = 0
for i in range(len(s)):
    if s[i] in "ABC":
        count+=1
        count_final = max(count_final, count)
    else:
        count = 0
print(count_final)
