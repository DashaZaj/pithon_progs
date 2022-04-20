n, m = map(int, input().split())  # ввод
A = [list(map(int, input().split())) for s in range(n)]
k = int(input())

c = 0  # переменные
count = []
bef_ans = []
found = False
done = False

for i in range(n):  # цикл по почти всем элементам
    for j in range(1, m):
        if A[i][0] == 0 and (not done):  # проверяем элементы вне цикла
            c = 1
            done = True

        if A[i][j] == 0 and A[i][j-1] == 0:  # условие увеличения счётчика
            c += 1
        if A[i][j] == 0 and A[i][j - 1] == 1:  # начало нового счётчика
            c = 1
        if (j == m - 1 and c != 0) or (A[i][j-1] == 0 and A[i][j] == 1):  # сброс счётчика
            count.append(c)
            c = 0
    bef_ans.append(count)
    count = []
    done = False  # сброс проверки элемента вне цикла в следующей строке

for i in range(len(bef_ans)):  # вывод
    if not found:
        for x in bef_ans[i]:
            if x >= k:
                print(i + 1)
                found = True
                break
if not found:
    print(0)
