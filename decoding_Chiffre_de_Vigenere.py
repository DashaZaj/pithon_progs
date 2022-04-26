alphabet = list(input())
key_word = input()
encrypted = input()
a = len(alphabet)
table = []
for i in range(a):
    temp = []
    for j in range(a):
        if j+i < a:
            temp.append(alphabet[j+i])
        else:
            temp.append(alphabet[j+i-a])
    table.append(temp)

factor = len(encrypted) // len(key_word)
if len(encrypted) % len(key_word) != 0:
    factor += 1
code_str = key_word*factor
ans = ''
for i in range(len(encrypted)):
    y = alphabet.index(code_str[i])
    temp = table[:][y]
    a = temp.index(encrypted[i])
    ans += alphabet[a]
print(ans)
