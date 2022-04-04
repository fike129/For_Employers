# print('y', 'x', 'z')
# for y in range(2):
#     for x in range(2):
#         for z in range(2):
#                 if ((not(x) and y and z) or (not(x) and not(z))) == True:
#                     print(y,x,z)

# print('y', 'x', 'z')
# for y in range(2):
#     for x in range(2):
#         for z in range(2):
#             if ((x or y) <= (y == z)) == False:
#                     print(y,x,z)

# print('y', 'x', 'z','w')
# for y in range(2):
#     for x in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x or y) and (not((y == z))) and (not(w)))== True:
#                     print(y,x,z,w)

# print('y', 'x', 'z','w')
# for y in range(2):
#     for x in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x and z) or ((w <= x) == (z <= y))) == False:
#                     print(y,x,z,w)

print('x','y','z','w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x == (not(y)) <= ((x and w) == z)))) == False:
                    print(x,y,z,w)