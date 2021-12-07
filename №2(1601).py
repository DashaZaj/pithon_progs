from itertools import permutations, product
'''
word = 'гладкость'
perm = list(permutations(word, r=5))
prod = list(product(word, repeat=5))  # декартово произведение
'''
word = input()
vols = 'ёуеэоаыяию'
perm = list(permutations(word))
ans = list()
for p in perm:
    cur_word = ''.join(p)
    soft_sing = cur_word.find('ь')
    if soft_sing != 0 and cur_word[soft_sing-1] not in vols:
        ans.append(cur_word)
ans.sort()
for a in ans:
    print(a)
