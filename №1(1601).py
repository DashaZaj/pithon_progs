from itertools import permutations, product
'''
word = 'гладкость'
perm = list(permutations(word, r=5))
prod = list(product(word, repeat=5))  # декартово произведение
'''
word = input()
first = word[0]
last = word[-1]
n_word = word[1:5]
perm = list(permutations(n_word))
ans = list()
for p in perm:
    ans.append(first+''.join(p)+last)
ans.sort()
for a in ans:
    print(a)
