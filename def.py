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
    divs = [x]
    if x**0.5 == int(x**0.5):
        divs.append(int(x**0.5))
    for i in range(2, ceil(x**0.5)):
        if x%i == 0:
            divs.append(i)
            divs.append(x//i)
    return sorted(divs)


def five_digits_sum(n):
    a = n%10
    b = (n//10)%10
    c = (n//100)%10
    d = (n//1000)%10
    e = (n//10000)%10
    return a+b+c+d+e


