s = input()
key_word = input()

key_letters = []
alphabet = [chr(i) for i in range(ord('а'), ord('я') + 1)]
for x in key_word:
    if x == 'ё':
        p = 'е'
    else:
        p = x
    if p not in key_letters:
        key_letters.append(p)
    if p in alphabet:
        alphabet.remove(p)

pre_table = key_letters + alphabet

table = []
p = 0
for i in range(4):
    temp = []
    for j in range(8):
        temp.append(pre_table[p+j])
    p += 8
    table.append(temp)

s_r = ''
for y in s:
    if y not in [',', '.', ':', ';', '-', '!', '?', ')', '(', ' ']:
        if y.lower() == 'ё':
            s_r += 'е'
        else:
            s_r += y.lower()
i = 0
changed = False
while len(s_r)-1 > i:
    if i % 2 == 0 and s_r[i] == s_r[i+1]:
        s_r = s_r[:i+1] + 'х' + s_r[i+1:]
        i += 2
        changed = True
    if not changed:
        i += 1
    changed = False

if len(s_r) % 2 != 0:
    s_r += 'х'

bigramms = [0]*(len(s_r)//2)
c = 0
for i in range(len(bigramms)):
    bigramms[i] = [s_r[c], s_r[c+1]]
    c += 2

ans = ''
for i in range(len(bigramms)):
    x0 = pre_table.index(bigramms[i][0]) % 8
    y0 = pre_table.index(bigramms[i][0]) // 8
    x1 = pre_table.index(bigramms[i][1]) % 8
    y1 = pre_table.index(bigramms[i][1]) // 8
    if y0 == y1:
        if x0 == 7:
            bigramms[i][0] = table[y0][0]
        else:
            bigramms[i][0] = table[y0][x0+1]
        if x1 == 7:
            bigramms[i][1] = table[y1][0]
        else:
            bigramms[i][1] = table[y1][x1+1]
    elif x0 == x1:
        if y0 == 3:
            bigramms[i][0] = table[0][x0]
        else:
            bigramms[i][0] = table[y0+1][x0]
        if y1 == 3:
            bigramms[i][1] = table[0][x1]
        else:
            bigramms[i][1] = table[y1+1][x1]
    else:
        bigramms[i][0] = table[y0][x1]
        bigramms[i][1] = table[y1][x0]
    ans += bigramms[i][0]
    ans += bigramms[i][1]

print(ans)
