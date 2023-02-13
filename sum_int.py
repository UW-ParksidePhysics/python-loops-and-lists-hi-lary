n = eval(input('input:'))
x = 1

for y in range(x, n, 1):
    y += x
    q = y * (y + 1) / 2
    print(y, q)

