def F(N):
    if N == 0: return 0

    if N == 1: return 1

    return F(N - 1) + F(N - 2)

N = 4
print(F(N))