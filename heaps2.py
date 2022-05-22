def can_win(x, y, depth):
    if x**2 + y**2 >= 64:
        return [False, [f"opponent already won"], depth, depth]
    wins = []
    loses = []

    plus3_x = can_win(x + 3, y, depth + 1)
    plus2_y = can_win(x, y + 2, depth + 1)
    depth += 1

    if not plus2_y[0]:
        wins.append([True, [f"[x;y+2] = {x**2 + (y+2)**2}"] + plus2_y[1], plus2_y[2], plus2_y[3]])
    else:
        loses.append([False, [f"[x;y+2] = {x**2 + (y+2)**2}"] + plus2_y[1], plus2_y[2], plus2_y[3]])
    if not plus3_x[0]:
        wins.append([True, [f"[x+3;y] = {(x+3)**2 + y**2}"] + plus3_x[1], plus3_x[2], plus3_x[3]])
    else:
        loses.append([False, [f"[x+3;y] = {(x+3)**2 + y**2}"] + plus3_x[1], plus3_x[2], plus3_x[3]])

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
        [[f"even if y+2 = {(y + 2)**2 + x**2} opponent will"] + [plus2_y[1]]] +
        [[f"even if x+3 = {(x+3)**2 + y**2} opponent will"] + [plus3_x[1]]],
        loses[minloss][2],
        loses[maxloss][3]
        ]


for stones in [[2, 3], [-1, 5], [-3, 5], [1, 6], [5, 0], [-1, 3]]:
    c_w = can_win(stones[0], stones[1], 0)
    print(stones, c_w)
