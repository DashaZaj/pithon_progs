def can_win(matches, steps):
    if matches <= 0:
        return (True, ((f'enemy took the last match'),), steps)
    if matches < 2:
        return (False, ((f'you have to take the last match'),), steps+1)
    by2 = ()
    if matches %2 == 0:
        by2 = can_win(matches // 2, steps+1)
        if not by2[0]:
            return (True, (((f'/2 = {matches//2}',) + by2[1]),), by2[2])
    minus4 = can_win(matches-4, steps+1)
    if not minus4[0]:
        return (True, (((f'-4 = {matches-4}',)+minus4[1]),), minus4[2])
    minus3 = can_win(matches-3, steps+1)
    if not minus3[0]:
        return (True, (((f'-3 = {matches-3}',) + minus3[1]),), minus3[2])
    minus2 = can_win(matches - 2, steps + 1)
    if not minus2[0]:
        return (True, (((f'-2 = {matches-2}',) + minus2[1]),), minus4[2])
    return (False, (((f'even if -2 = {matches - 2}',) + minus2[1],) +
                    ((f'even if -3 = {matches - 3}',) + minus3[1],) +
                    ((f'even if -4 = {matches - 4}',) + minus4[1],) +
                    (((f'even if /2 = {matches//2}',) + by2[1]) if (matches%2 == 0) else ()),), max(((by2[2]) if matches %2 == 0 else minus4[2]), minus2[2], minus3[2], minus4[2]))


print(can_win(13, 0))
