x = -2147483648
anslist = []
ans = 0
a = 1
while x != 0:
    if x < 0:
        x *= -1
        a = -1
    anslist.append(x % 10)
    x = x // 10

for ele in anslist:
    ans = ans * 10 + ele

if ((ans * a) < (2**31 - 1)) & (a > 0):
    print(ans * a)
elif ((ans * a) > -(2**31)) & (a < 0):
    print(ans * a)
else:
    print(ans * a)