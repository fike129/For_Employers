# def Del(n,m):
#     return n % m == 0
#
# for A in range(1,1000):
#     podoshelA = True
#     for x in range(1,1000):
#         if ((not(Del(x,A))) <= (Del(x,6) <= (not (Del(x,9))))) == False:
#             podoshelA = False
#             break
#     if podoshelA == True:
#         print(A)


# def Del(n,m):
#     return n % m == 0

# for A in range(1,1000):
#     podoshelA = True
#     for x in range(1,1000):
#         if ((not Del(x,A)) <= ((Del(x,6)) <= (not Del(x,4)))) == False:
#             podoshelA = False
#             break
#     if podoshelA == True:
#         print(A)


# def Del(n,m):
#      return n % m == 0
#
#  for A in range(1,1000):
#     podoshelA = True
# for x in range(1,1000):
#          if (Del(110,A) and ((Del(x,80)) and Del(x,75)) <= Del(x,A) ) == False:
#              podoshelA = False
#              break
#      if podoshelA == True:
#          print(A)


# for A in range(0,1000):
#      podoshelA = True
#      for x in range(0,1000):
#          if ((x & 51 == 0) or ((x & 41 == 0) <= (x & A == 0))) == False:
#              podoshelA = False
#              break
#      if podoshelA == True:
#          print(A)


# P = list(range(12, 24+1))
# Q = list(range(18, 30+1))
#
# A = []
# for x in range(1,1000):
#     if ((x not in A) <= ((x in P) <= (x not in Q))) == False:
#         A.append(x)
# print(A)
# '24 -18 = 6'


# P = list(range(15, 30+1))
# Q = list(range(8, 25+1))
#
# A = []
# for x in range(1,1000):
#     if ((x in P) <= ((x in Q) <= (x in A))) == False:
#         A.append(x)
# print(A[-1]-A[0])


# P = list(range(12, 28+1))
# Q = list(range(8, 16+1))
#
# A = list(range(1,1000))
# for x in range(1,1000):
#     if ((x in A) <= (((x in P)) and (x not in Q))) == False:
#         A.remove(x)
# print(A)


# def Del(n,m):
#     return n % m == 0
#
# for A in range(1,1000):
#     podoshelA = True
#     for x in range(1,1000):
#         if (Del(x,A) <= (Del(x,21)) or (Del(x,35))) == False:
#             podoshelA = False
#             break
#     if podoshelA == True:
#         print(A)


# def Del(n,m):
#     return n % m == 0
#
# for A in range(1,1000):
#     podoshelA = False
#     for x in range(1,1000):
#         for y in range(1,1000):
#             if (((y - 50 < A) and (50 - y < A)) or (x * y > 30)) == True:
#                 podoshelA = False
#                 break
#     if podoshelA == False:
#         print(A)



# for A in range(1,1000):
#     podoshelA = True
#     for x in range(1,1000):
#         if ((x % 29 != 0 <= ((x & 9 == 0) <= (x & A != 0)))) == False:
#             podoshelA = False
#             break
#     if podoshelA == True:
#         print(A)

for A in range(1,1000):
    for x in range(1,1000):
        if ((x & 25 != 0) <= ((x & 9 == 0) <= (x & A != 0))) == False:
            podoshelA = False
            break
    if podoshelA == True:
        print(A)
