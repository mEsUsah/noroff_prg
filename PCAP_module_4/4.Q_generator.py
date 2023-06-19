def fun(n):
    s = 'x'
    for i in range(n):
        s += s
        yield s

for x in fun(2):
    # print(x, end='')
    print(x)