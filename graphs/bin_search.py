A = list(map(int, input().split()))
x = int(input())
l = 0
r = len(A) - 1
m = (l + r) // 2

if x > A[0]:
    print(1)
elif x < A[-1]:
    print(len(A)+1)
else:
    while r - l > 1:
        if x < A[m]:
            l = m
        else:
            r = m
        m = (l + r) // 2
    while r < len(A) and x == A[r]:
        r += 1
    print(r+1)