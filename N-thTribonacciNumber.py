n = 2

if not n : print(0)

else:
    a, b, c = 0, 0, 1

    for i in range(n - 1):
        a, b, c = b, c, a + b + c

    print(c)