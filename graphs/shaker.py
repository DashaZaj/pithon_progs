def print_array(a, edge_r, edge_l, j):
    n = len(a)
    for v in range(n):
        if v == edge_l:
            print('|', end=' ')
        if v == j:
            print(f"<{a[v]}>", end=' ')
        else:
            print(a[v], end=' ')
        if v == edge_r-1:
            print('|', end=' ')
    print()


n = int(input())
a = list(map(int, input().split()))

edge_l = 0
edge_r = n
while edge_r - edge_l > 2:
    last_swap_r = -1
    for j in range(edge_l, edge_r-1):
        print_array(a, edge_r, edge_l, j)
        if a[j] < a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            last_swap_r = j+1
    if last_swap_r == -1: break
    print_array(a, edge_r, edge_l, edge_r-1)
    edge_r = last_swap_r
    print_array(a, edge_r, edge_l, -1)
    print('---------')
    last_swap_l = -1
    for l in range(edge_r-1, edge_l, -1):
        print_array(a, edge_r, edge_l, l)
        if a[l] > a[l - 1]:
            a[l], a[l - 1] = a[l - 1], a[l]
            last_swap_l = l
    # print_array(a, edge_r, edge_l, edge_l)
    if last_swap_l == -1: break
    edge_l = last_swap_l
    print_array(a, edge_r, edge_l, -1)
    print('---------')
for x in a:
    print(x, end=' ')