def print_array(a, edge, j):
    n = len(a)
    for v in range(n):
        if v == j:
            print(f"<{a[v]}>", end=' ')
        else:
            print(a[v], end=' ')
        if v == edge-1:
            print('|', end=' ')
    print()


n = int(input())
a = list(map(int, input().split()))

for x in a:
    print(x, end=' ')
print('|')
print('------------')

edge = n
for i in range(n-1):
    for j in range(edge-1):
        print_array(a, edge, j)
        if a[j] < a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
    print_array(a, edge, edge-1)
    edge -= 1
    print('------------')
for x in a:
    print(x, end=' ')