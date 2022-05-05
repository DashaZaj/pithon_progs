"""
За один ход игрок может добавить в кучу 4 камня или увеличить количество камней в куче в 4 раза.
Игра завершается в тот момент, когда количество камней в куче становится не менее 56.
Победителем считается игрок, сделавший последний ход, то есть первым получивший кучу, в которой будет 56 или больше камней.
"""


def can_win(n, depth):
    if n >= 56:
        return [False, [f"opponent already won"], depth, depth]
    wins = []
    loses = []

    plus4 = can_win(n+4, depth+1)
    by4 = can_win(n*4, depth+1)
    depth += 1

    if not by4[0]:
        wins.append([True, [f"*4 = {n*4}"] + by4[1], by4[2], by4[3]])
    else:
        loses.append([False, [f"*4 = {n*4}"] + by4[1], by4[2], by4[3]])
    if not plus4[0]:
        wins.append([True, [f"+4 = {n+4}"] + plus4[1], plus4[2], plus4[3]])
    else:
        loses.append([False, [f"+4 = {n+4}"] + plus4[1], plus4[2], plus4[3]])

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
        [[f"even if +4 = {n+4} opponent will"]+[plus4[1]]] +
        [[f"even if *4 = {n*4} opponent will"]+[by4[1]]],
        loses[minloss][2],
        loses[maxloss][3]
        ]


for stones in range(1, 56):
    print(stones, can_win(stones, 0))
