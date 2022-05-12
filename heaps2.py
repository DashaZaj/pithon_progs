def can_win(c, n, depth):
    if c+n >= 49:
        return [False, [f"opponent already won"], depth, depth]
    wins = []
    loses = []

    plus3_c = can_win(c+3, n, depth+1)
    plus3_n = can_win(c, n+3, depth+1)
    by2_c = can_win(c*2, n, depth+1)
    by2_n = can_win(c, n*2, depth+1)
    depth += 1

    if not by2_n[0]:
        wins.append([True, [f"n*2 + c = {(n*2)+c}"] + by2_n[1], by2_n[2], by2_n[3]])
    else:
        loses.append([False, [f"n*2 + c = {(n*2)+c}"] + by2_n[1], by2_n[2], by2_n[3]])
    if not by2_c[0]:
        wins.append([True, [f"c*2 + n = {(c*2)+n}"] + by2_c[1], by2_c[2], by2_c[3]])
    else:
        loses.append([False, [f"c*2 + n = {(c*2)+n}"] + by2_c[1], by2_c[2], by2_c[3]])
    if not plus3_n[0]:
        wins.append([True, [f"n+3 + c  = {n + 3 + c}"] + plus3_n[1], plus3_n[2], plus3_n[3]])
    else:
        loses.append([False, [f"n+3 + c = {n+3 + c}"] + plus3_n[1], plus3_n[2], plus3_n[3]])
    if not plus3_c[0]:
        wins.append([True, [f"c+3 + n = {n + 3 + c}"] + plus3_c[1], plus3_c[2], plus3_c[3]])
    else:
        loses.append([False, [f"c+3 + n = {n + 3 + c}"] + plus3_c[1], plus3_c[2], plus3_c[3]])

    if len(wins) != 0:
        minwin_idx = 0
        for i in range(len(wins)):
            if wins[minwin_idx][2] > wins[i][2]:
                minwin_idx = i
        return wins[minwin_idx]

    minloss = 0
    maxloss = 0
    for i in range(len(loses)):
        if loses[minloss][2] > loses[i][2]:
            minloss = i
        if loses[maxloss][3] < loses[i][3]:
            maxloss = i

    return [
        False,
        [[f"even if n+3 = {n+3 + c} opponent will"]+[plus3_n[1]]] +
        [[f"even if c+3 = {n + 3 + n} opponent will"] + [plus3_c[1]]] +
        [[f"even if n*2 = {n*2 + c} opponent will"]+[by2_n[1]]] +
        [[f"even if c*2 = {c*2 + n} opponent will"]+[by2_c[1]]],
        loses[minloss][2],
        loses[maxloss][3]
        ]


for stones in range(1, 39):
    c_w = can_win(9, stones, 0)
    print(stones, c_w[0], c_w[-2:])
