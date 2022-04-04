#from itertools import *
#count_word = 0
#for i in product('ЧЕТО',repeat=6):
  #  if i.count('Е') >= 1:
 #       count_word += 1
#print(count_word)

#count_word = 0
#for i in permutations('ЗЛОЙ'):
 #   if i[0] != 'Й' and 'ОЙ' not in ''.join(i):
 #       count_word += 1
#print(count_word)


count_word = set()
for i in permutations('ТАРТАР'):
        count_word.add(i)
print(len(count_word))