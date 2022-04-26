def first_prime_factor(N):
    j = 0
    for i in range(3, int(N**0.5)+1, 2):
        if N % i == 0:
            j = i
            break
    if j != 0:
        return j, N//j
    else:
        return N, 1


for i in range(78000000, 85000001):
    j = i
    while j % 2 == 0:
        j = j // 2
    if j != 1:
        ji = int(j**0.25)
        if j**0.25 == ji and first_prime_factor(ji)[0] == ji:
            print(i, j)
