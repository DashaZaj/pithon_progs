def can_win(n, depth):
    if n >= 27:
        return [False, [f"opponent already won"], depth, depth]
    wins = []
    loses = []

    plus2 = can_win(n+2, depth+1)
    plus3 = can_win(n+3, depth+1)
    by3 = can_win(n*3, depth+1)
    depth += 1

    if not by3[0]:
        wins.append([True, [f"*3 = {n*3}"] + by3[1], by3[2], by3[3]])
    else:
        loses.append([False, [f"*3 = {n*3}"] + by3[1], by3[2], by3[3]])
    if not plus2[0]:
        wins.append([True, [f"+2 = {n+2}"] + plus2[1], plus2[2], plus2[3]])
    else:
        loses.append([False, [f"+2 = {n+2}"] + plus2[1], plus2[2], plus2[3]])
    if not plus3[0]:
        wins.append([True, [f"+3 = {n + 3}"] + plus3[1], plus3[2], plus3[3]])
    else:
        loses.append([False, [f"+3 = {n + 3}"] + plus3[1], plus3[2], plus3[3]])

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
        [[f"even if +2 = {n+2} opponent will"]+[plus2[1]]] +
        [[f"even if +3 = {n + 3} opponent will"] + [plus3[1]]] +
        [[f"even if *3 = {n*3} opponent will"]+[by3[1]]],
        loses[minloss][2],
        loses[maxloss][3]
        ]


for stones in range(1, 26):
    c_w = can_win(stones, 0)
    print(stones, c_w[0] ,c_w[-2:])
