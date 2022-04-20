c_s = input()
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

bigramms = [0]*(len(c_s)//2)
c = 0
for i in range(len(bigramms)):
    bigramms[i] = [c_s[c], c_s[c+1]]
    c += 2

ans = ''
for i in range(len(bigramms)):
    x0 = pre_table.index(bigramms[i][0]) % 8
    y0 = pre_table.index(bigramms[i][0]) // 8
    x1 = pre_table.index(bigramms[i][1]) % 8
    y1 = pre_table.index(bigramms[i][1]) // 8
    if y0 == y1:
        if x0 == 0:
            bigramms[i][0] = table[y0][7]
        else:
            bigramms[i][0] = table[y0][x0-1]
        if x1 == 0:
            bigramms[i][1] = table[y1][7]
        else:
            bigramms[i][1] = table[y1][x1-1]
    elif x0 == x1:
        if y0 == 0:
            bigramms[i][0] = table[3][x0]
        else:
            bigramms[i][0] = table[y0-1][x0]
        if y1 == 0:
            bigramms[i][1] = table[3][x1]
        else:
            bigramms[i][1] = table[y1-1][x1]
    else:
        bigramms[i][0] = table[y0][x1]
        bigramms[i][1] = table[y1][x0]
    ans += bigramms[i][0]
    ans += bigramms[i][1]

print(ans)
