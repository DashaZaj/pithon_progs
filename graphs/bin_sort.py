from math import log2, ceil


def bin_insert(a: list, x: int):
    if len(a) == 0:
        return [x]
    if x <= a[0]:
        return [x] + a
    if x >= a[-1]:
        return a + [x]

    size = len(a)
    l: int = 0
    r = size - 1
    while (r-l) > 1:
        m = (l + r) // 2
        if x < a[m]:
            r = m
        else:
            l = m
    return a[:l+1] + [x] + a[r:]


print(bin_insert([4, 5, 6, 8, 10], 1))
print(bin_insert([1, 4, 5, 6, 8], 10))
print(bin_insert([1, 4, 6, 8, 10], 5))
print(bin_insert([1, 4, 6, 8, 10], 9))
print(bin_insert([1, 4, 6, 8], 3))
print(bin_insert([1, 8], 3))
print(bin_insert([1], 3))
print(bin_insert([], 3))
