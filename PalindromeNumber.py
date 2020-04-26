x = 1000021

anslist = []
ans = True
while x != 0:
    if x < 0:
        ans = False
        break

    else:
        anslist.append(x % 10)
        x = x // 10

y = len(anslist) // 2
min = 0
max = -1
while y != 0:
    if anslist[min] == anslist[max]:
        y -= 1
        min += 1
        max -= 1
    else:
        ans = False
        break

print(ans)