s = 'еволнлмфскбгхвоялкчсупгхлнл'
sub_str = 'создатель'
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

for i in range(33):
    for j in range(i+1, 33):
        option = ''
        if j % 2 != i % 2:
            A = i
            B = j
            C = A + (B - A + 1) // 2
            key = alphabet[A:C] + alphabet[:A] + alphabet[B + 1:] + alphabet[C:B + 1]
            for x in s:
                option += alphabet[key.find(x)]
            if sub_str in option:
                print(option, A, B)
