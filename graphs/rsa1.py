N = int(input())
a = [i for i in range(2, N+1)]
e = int(N**0.5)-1
print(e)

c = 0
for x in a:
    if c == 100:
        c = 0
        print()
    print(x, end=' ')
    c += 1
c = 0
print()

for i in range(e):
    if a[i] != 0:
        t = a[i]
        for j in range(i+t, N+t, t):
            if j < N-1:
                a[j] = 0
        for x in a:
            if c == 100:
                c = 0
                print()
            print(x, end=' ')
            c += 1
        c = 0
        print()

b = 0
for x in a:
    if x != 0:
        if c == 100:
            c = 0
            print()
        print(x, end=' ')
        b += 1
        c += 1
print()
print(b)
