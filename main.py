pp = 46368
p = 75025
a = []
l = 0
while l <= 1000000000:
    l = pp + p
    pp = p
    p = l
    a.append(l)
a = a[:-1]
print(a)
ans = []
for i in range(26, 45):
    primary = True
    for j in range(2, int(a[i-26]**0.5)+1):
        if a[i-26] % j == 0:
            primary = False
            break
    if primary:
        ans.append([i, a[i-26]])
print(ans)
