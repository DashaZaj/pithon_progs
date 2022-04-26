n = int(input())
a = list(map(int, input().split()))
ind = 0
print('|', end=' ')
for k in range(len(a)):
    print(a[k], end=' ')
print()
for i in range(n):
    b = a[ind:]
    min = 0
    for j in range(len(b)):
        if b[j] < b[min]:
            min = j
    min += ind
    a[ind], a[min] = a[min], a[ind]
    ind += 1
    for k in range(len(a)):
        if k == ind-1:
            print(a[k], '|', end=' ')
        else:
            print(a[k], end=' ')
    print()
