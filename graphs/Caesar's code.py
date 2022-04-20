s = input()
A, B = map(int, input().split())
C = A + (B-A + 1)//2
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
key = alphabet[A:C] + alphabet[:A] + alphabet[B+1:] + alphabet[C:B+1]

for x in s:
    print(key[alphabet.find(x)], end='')
