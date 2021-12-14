n = int(input())
b = list(map(int, input().split()))
a = [0]*n
mask = a
comb = []
lis = []

for k in range(1, n+1):
    for i in range(2**n):
        if mask.count(1) == k:
            for m in range(n):
                if mask[m] == 1:
                    comb.append(b[m])
            comb.sort()
            lis.append(comb)
        comb = []
        cur_sum = a[-1] + 1
        up = cur_sum // 2
        mask = [cur_sum % 2]
        for j in range(n-2, -1, -1):
            cur_sum = a[j] + up
            ans_1 = cur_sum % 2
            mask = [ans_1] + mask
            up = cur_sum // 2
        a = mask

lis.sort()
for x in lis:
    for y in x:
        print(y, end=" ")
    print()
