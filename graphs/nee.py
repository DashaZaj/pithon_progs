def go(s, f):
    if s > f:
        return 0
    if s == 16:
        return 0
    if s == f:
        return 1
    return go(s+1, f) + go(s*2, f)


def F(n):
  print("A",end='')
  if n > 0:
    print("B",end='')
    G(n-1)
def G(n):
  print("C",end='')
  if n > 1:
    F(n-2)


print(go(3, 6)*go(6, 33))
