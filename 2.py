def first_prime_factor(N):
    j = 0
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            j = i
            break
    if j != 0:
        return j, N//j
    else:
        return N, 1


for i in range(2531, 51238):
    a, b = first_prime_factor(i)
    d = [a]
    while b != 1:
        a, z = first_prime_factor(b)
        if d.count(a) == 0:
            d.append(a)
        b = z
    if len(d) >= 6:
        print(i, d[-1], end=' ')
