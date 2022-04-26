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
    for i in range(3881, ceil(x**0.5), 2):
        if x%i == 0:
            divs.append(i)
            divs.append(x//i)
    return sorted(divs)


for i in range(15000000, 16000001):
    needed = True
    d = div(i)
    if len(d) >= 2:
        if d[0] + 8 <= d[-1]:
            for j in range(d[0], d[-1], 8):
                if j not in d:
                    needed = False
                    break
        else:
            needed = False
        if needed and first_prime_factor(d[0])[0] == d[0] and first_prime_factor(i)[0] == d[0]:
            print(i, d[0])
            print(d)
