numRows = 3

ans = []

for x in range(numRows + 2):
    ansList = []
    # print(x)
    if x == 0:
        continue

    for y in range(x):
        # print(y)
        if y == 0 or y == (x - 1):
            ansList.append(1)

        else:
            ansList.append(ans[x - 2][y - 1] + ans[x - 2][y])
    
    ans.append(ansList)
print(ans[numRows])