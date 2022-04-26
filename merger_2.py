def merge_sort(arr):
    l = len(arr)
    if l == 1 or l == 0:
        print(f"список {arr} сортировать незачем")
        return arr
    else:
        half = l//2
        print(f"чтобы отсортировать список {arr}, нужно отсортировать списки {arr[:half]} и {arr[half:]} и слить результаты")
        n_a = len(arr[:half])
        a = merge_sort(arr[:half])
        n_b = len(arr[half:])
        b = merge_sort(arr[half:])
        c = []

        ku_a = 0
        ku_b = 0
        while ku_a < n_a and ku_b < n_b:
            if a[ku_a] < b[ku_b]:
                c.append(a[ku_a])
                ku_a += 1
            else:
                c.append(b[ku_b])
                ku_b += 1
        if ku_a != n_a:
            for x in a[ku_a:]:
                c.append(x)
        elif ku_b != n_b:
            for x in b[ku_b:]:
                c.append(x)
        print(f"отсортированные подсписки {a}, {b} слиты в список {c}")
        return c


k = input()
print(merge_sort(list(map(int, input().split()))))
