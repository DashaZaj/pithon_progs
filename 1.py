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


def sum_five_digits(x):
    a = x%10
    b = (x//10)%10
    c = (x//100)%10
    d = (x//1000)%10
    e = (x//10000)%10
    return a+b+c+d+e


for i in range(49790, 57899):
    if first_prime_factor(i)[0] == i and sum_five_digits(i) > 35:
        print(i, end=' ')
