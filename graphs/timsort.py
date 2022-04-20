def get_minrun(n):
    r = 0
    while n >= 64:
        r |= n & 1
        n = n >> 1
    return n + r


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


n = int(input())
a = list(map(int, input().split()))
minrun = get_minrun(n)

ind = 0

incr = False
desc = False
temp = [a[ind], a[ind+1]]
ind += 2
if temp[0] < temp[1]:
    incr = True
else:
    desc = True
h = 1
if incr:
    while temp[h] < a[ind]:
        temp.append(a[ind])
        h += 1
        ind += 1
if desc:
    while temp[h] > a[ind]:
        temp.append(a[ind])
        h += 1
        ind += 1
if desc:
    temp = temp[len(temp)-1::-1]
if len(temp) < minrun:
    dif = minrun - len(temp)
    b = a[ind:ind+dif+1]
    for x in b:
        bin_insert(temp, x)

'''
for j in range(1, n):  # не используется (merge_sort)
    ind = j
    cand = a[ind]
    i = ind - 1
    changed = False
    while a[i] > cand:
        changed = False
        a[i+1] = a[i]
        if i != 0:
            i -= 1
        else:
            a[i] = cand
            changed = True
            break

    if not changed:
        a[i+1] = cand
'''