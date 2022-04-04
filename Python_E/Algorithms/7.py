f = open('24_8.txt')
s = f.readline()
count = 0
for i in range(len(s)):
    b = set(s[i:i+3])
    if len(b) == 3:
        count+=1
print(count)