n_a = int(input())
a = list(map(int, input().split()))
n_b = int(input())
b = list(map(int, input().split()))
c = []

ku_a = 0
ku_b = 0
while ku_a < n_a and ku_b < n_b:
    for v in range(n_a):
        if v == ku_a:
            print(f"<{a[v]}>", end=' ')
        else:
            print(a[v], end=' ')
    print()
    for v in range(n_b):
        if v == ku_b:
            print(f"<{b[v]}>", end=' ')
        else:
            print(b[v], end=' ')
    print()
    for x in c:
        print(x, end=' ')
    print()
    print()
    if a[ku_a] < b[ku_b]:
        c.append(a[ku_a])
        ku_a += 1
    else:
        c.append(b[ku_b])
        ku_b += 1
if ku_a != n_a:
    for x in a[ku_a:]:
        c.append(x)
elif ku_b != n_b:
    for x in b[ku_b:]:
        c.append(x)
for x in c:
    print(x, end=' ')
