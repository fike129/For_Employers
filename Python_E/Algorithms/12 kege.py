#b = '0' + '1'*12 + '2'*15 + '3'*17

#while '01' in b or '02' in b or '03' in b:
 #   b = b.replace('01', '20', 1)
#    b = b.replace('02', '120', 1)
#    b = b.replace('03', '302', 1)
#print(b.count('1'))


#b = '5' * 65
#
#while '333' in b or '555' in b:
 #   if '555' in b:
  #      b = b.replace('555', '3', 1)
   # else:
    #        b = b.replace('333', '5', 1)
#print(b)



b = '4' * 123

while '4444' in b or '7777' in b:
    if '4444' in b:
        b = b.replace('4444', '77', 1)
    else:
        b = b.replace('7777', '44', 1)
    print(b)

