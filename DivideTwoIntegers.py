dividend = -2147483648
divisor = -3

ans = dividend//divisor
if dividend < 0 and divisor == -1:
    if dividend == divisor:
        print(int(ans))

    else:
        print(int(ans) - 1)

else:
    print(int(ans))