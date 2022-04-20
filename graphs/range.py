ma = []
count = 0
for i in range(1165, 7643):
    a = i % 10
    b = (i % 100)//10
    c = (i % 1000)//100
    d = (i % 10000)//1000
    if (a+b+c+d) % 2 == 0 and i % 25 != 23:
        count += 1
        ma.append(i)
print(count, ma[-1])
