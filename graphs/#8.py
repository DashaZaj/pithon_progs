def put_to_cand(b, see_i, see_j, cand):
    if see_i >= 0 and see_j >= 0 and b[see_i][see_j] >= 0:
        cand.append(b[see_i][see_j])


def find(w, h, field, min_or_max):
    b = [[-1] * w for _ in range(h)]
    b[0][0] = field[0][0]
    for i in range(h):
        for j in range(w):
            cand = []
            put_to_cand(b, i, j - 2, cand)
            put_to_cand(b, i, j - 3, cand)
            put_to_cand(b, i - 2, j, cand)
            put_to_cand(b, i - 3, j, cand)
            if cand:
                b[i][j] = min_or_max(cand) + field[i][j]
    return b[-1][-1]


h, w = map(int, input().split())
field = [list(map(int, input().split())) for i in range(h)]

print(find(w, h, field, max), find(w, h, field, min))
