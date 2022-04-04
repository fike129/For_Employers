s = ">"+"1"*14+"2"*20+"3"*25
a1 = ">1"; a2 = "22>3"
b1 = ">2"; b2 = "2>"
c1 = ">3"; c2 = "11>2"
v=0
while a1 in s or b1 in s or c1 in s:
    if a1 in s:
      s = s.replace(a1, a2, 1)
    if b1 in s:
      s = s.replace(b1, b2, 1)
    if c1 in s:
      s = s.replace(c1, c2, 1)
      for i in range(0, len(s) - 1):
          print(s)
          print(v)