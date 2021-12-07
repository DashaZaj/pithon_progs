from itertools import permutations, product
'''
word = 'гладкость'
perm = list(permutations(word, r=5))
prod = list(product(word, repeat=5))  # декартово произведение
'''
word = input()
perm = list(permutations(word))
ans = list()
first = word[0]
last = word[-2:]
for p in perm:
    cur_word = ''.join(p)
    if cur_word[0] != first and cur_word.find(last) == -1:
        ans.append(cur_word)
ans.sort()
for a in ans:
    print(a)
