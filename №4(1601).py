from itertools import permutations, product

word = input()
vols = 'ёуеэоаыяию'
perm = list(permutations(word))
ans = list()
for p in perm:
    ind = True
    cur_word = ''.join(p)
    for i in range(len(cur_word)-1):
        if cur_word[i] in vols and cur_word[i+1] in vols:
            ind = False
    if ind:
        ans.append(cur_word)
ans.sort()
for a in ans:
    print(a)
