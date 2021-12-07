from itertools import product

word = input()
first = word[0]
last = word[-1]
prod = list(product(word, repeat=3))
ans = list()
for p in prod:
    ans.append(first+''.join(p)+last)
ans.sort()
for a in ans:
    print(a)
