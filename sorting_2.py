n = int(input())
a = list(map(int, input().split()))
for v in range(n):
    if v == 0:
        print(f"| <{a[v]}>", end=' ')
    else:
        print(a[v], end=' ')
print()
for v in range(n):
    if v == 0:
        print(f"<{a[v]}> |", end=' ')
    else:
        print(a[v], end=' ')
print()
print()


for j in range(1, n):
    ind = j
    for v in range(n):
        if v == ind:
            print(f"| <{a[v]}>", end=' ')
        else:
            print(a[v], end=' ')
    print()
    cand = a[ind]
    i = ind - 1
    changed = False
    while a[i] > cand:
        changed = False
        a[i+1] = a[i]
        for v in range(n):
            if v == ind:
                print(f"{a[v]} |", end=' ')
            else:
                print(a[v], end=' ')
        print()
        if i != 0:
            i -= 1
        else:
            a[i] = cand
            changed = True
            break

    if not changed:
        a[i+1] = cand

    for v in range(n):
        if a[v] == cand and v == ind:
            print(f"<{a[v]}> |", end=' ')
        elif v == ind:
            print(f"{a[v]} |", end=' ')
        elif a[v] == cand and v < ind and a[v+1] != a[v]:
            print(f"<{a[v]}>", end=' ')
        else:
            print(a[v], end=' ')
    print()
    print()
for x in a:
    print(x, end=' ')
