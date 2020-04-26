l1 = [1, 2, 3]
l2 = [4, 5, 6]

ans = 0
for (x, y) in zip(l1, l2):
    ans = ans * 10 + x + y
print(ans)

ans = 0
for i in range(len(l1)):
    ans = ans * 10 + l1[i] + l2[i]
print(ans)