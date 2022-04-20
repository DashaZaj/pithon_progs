s = input()
key_word = input()

l = len(key_word)
n = len(s)//l
if len(s) % l != 0:
    n += 1
    s += ' '*(l - len(s) % l)

table = []
for i in range(n):
    temp = list(s[:l])
    if len(s) > l:
        s = s[l:]
    table.append(temp)

pos = [ord(x) for x in key_word]
pos.sort()
order = []
for x in key_word:
    order.append(pos.index(ord(x)))
    pos[pos.index(ord(x))] = ''

for i in range(l):
    for j in range(n):
        print(table[j][order.index(i)], end='')
