n = int(input())
k = int(input())
mask = list(map(int, input().split()))

j=-1
for i in range(k):
    if j < mask[i] < n- k + i:
        j = i
mask[j] += 1
for l in range(j+1, k):
    mask[l] = j+1+l

for x in mask:
    print(x, end=' ')
print()
