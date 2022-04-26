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


c = 0
kl = []
for i in range(416782, 498325):
    a, b = first_prime_factor(i)
    count = 1
    divs = [a]
    at = a%10
    while b != 1 and count != 3:
        a, z = first_prime_factor(b)
        if a%10 == at:
            divs.append(a)
        b = z
        count += 1
    if len(divs) == 3 and b == 1 and divs[0] != divs[1] != divs[2]:
        c += 1
        kl.append(i)

print(c, kl[-1] - kl[0])
print(kl)
