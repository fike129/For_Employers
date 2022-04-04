# s = '8'*62
# while '222' in s or '888' in s:
#     if '222' in s:
#         s = s.replace('222','8',1)
#     else:
#         s = s.replace('888','2',1)
# print(s)

# s = '8'*9 + '5'*12
# # while '555' in s or '888' in s:
# #     while '555' in s:
# #         s = s.replace('555','8',1)
# #     while '888' in s:
# #         s = s.replace('888','5',1)
# # print(s)

# s = '1' + '8'*80
# while '18' in s or '288' in s or '3888' in s:
#     if '18' in s:
#         s = s.replace('18', '2',1)
#     else:
#         if '288' in s:
#             s = s.replace('288', '3',1)
# print(s)

# for i in range(80,500):
#     s = '1'*i
#     while '111' in s:
#         s = s.replace('111', '2', 1)
#         s = s.replace('222','1',1)
#     if s == '21':
#         print(i)

# s = '1'*50 + '2'*50 + '3'*50
# while '12' in s or '32' in s or '31' in s:
#     if '12' in s:
#         s = s.replace('12','21',1)
#     if '32' in s:
#         s = s.replace('32','23',1)
#     if '31' in s:
#         s = s.replace('31','13',1)
# print(s[19],s[79],s[119])


# s = '1'*81
# while "1111" in s or '88888' in s:
#     if '1111' in s:
#         s = s.replace('1111','888',1)
#     else:
#         s = s.replace('88888','888',1)
# print(s)

