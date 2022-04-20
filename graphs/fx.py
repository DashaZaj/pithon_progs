s = input()
key_word = input()

lk = len(key_word)
n = len(s) // lk
if len(s) % lk != 0:
    n += 1
    s += ' '*(lk - len(s) % lk)

table = []
for i in range(lk):
    table.append(list(s[:n]))
    s = s[n:]


pos = [ord(x) for x in key_word]
pos.sort()
order = []
for x in key_word:
    order.append(pos.index(ord(x)))
    pos[pos.index(ord(x))] = ''

n_table = [0] * lk
for i in range(lk):
    n_table[i] = table[order[i]]

ans = ''
for i in range(n):
    for j in range(lk):
       ans += n_table[j][i]
i = -1
while ans[i] == ' ':
    i -= 1
if i != -1:
    ans = ans[:i+1]
print(ans)
