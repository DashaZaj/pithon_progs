alphabet = list(input())
key_word = input()
message = input()
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

factor = len(message)//len(key_word)
if len(message) % len(key_word) != 0:
    factor += 1
code_str = key_word*factor
ans = ''
for i in range(len(message)):
    x = alphabet.index(message[i])
    y = alphabet.index(code_str[i])
    ans += table[x][y]
print(ans)
