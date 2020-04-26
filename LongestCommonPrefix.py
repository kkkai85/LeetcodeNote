# strs = ["flight", "flow", "flower"]
# strs = ["dog","racecar","car"]
# strs = ["", ""]
strs = []

ansStr = ""
ansList = []
for x in range(len(strs) - 1):

    for y in range(x + 1, len(strs)):
        ansStr = ""
        if len(strs[x]) == 0 or len(strs[y]) == 0:
            ansStr = ""

        elif strs[x][0] == strs[y][0]:
            for (i, j) in zip(strs[x], strs[y]):
                if i == j:
                    ansStr += i

        ansList.append(ansStr)
        
for ans in ansList:
    if len(ans) < len(ansStr):
        ansStr = ans
        
print(ansStr)