from math import ceil


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


def div(x):
    divs = []
    if x**0.5 == int(x**0.5):
        divs.append(int(x**0.5))
    for i in range(2, ceil(x**0.5)):
        if x%i == 0:
            divs.append(i)
            divs.append(x//i)
    return sorted(divs)


for i in range(750000, 1060001):
    needed = True
    d = div(i)
    if len(d) >= 2:
        for j in range(len(d)-1):
            if d[j] + 14 != d[j+1]:
                needed = False
                break
    else:
        needed = False
    if needed and first_prime_factor(i)[0] == d[0]:
        print(i, d[0], end=' ')
