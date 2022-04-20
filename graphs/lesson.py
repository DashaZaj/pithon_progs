from math import ceil


def div(x):
    divs = [x]
    if x**0.5 == int(x**0.5):
        divs.append(int(x**0.5))
    for i in range(2, ceil(x**0.5)):
        if x%i == 0:
            divs.append(i)
            divs.append(x//i)
    return sorted(divs)


for i in range(203000001, 203000100):
    a = sorted(div(i))
    if len(a) >= 5:
        f = 1
        for y in a[:5]:
            f *= y
        if f < i:
            print(f, end=' ')
