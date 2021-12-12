from itertools import permutations

word = "безличность"
perm = list(permutations(word))
ans = 0

for p in perm:
    cur_word = ''.join(p)
    if cur_word.count('сть') == 1 and "б" not in cur_word[:5] and "л" not in cur_word[:5] and "и" not in cur_word[:5] and "е" not in cur_word[:5] and "з" not in cur_word[:5]:
        ans += 1
print(ans)
