# s = "Hello World"
s = "as a "

ansList = s.split(" ")
ans = 0
print(ansList)
if ansList[-1] != "":
    ans = len(ansList[-1])

else:
    for i in range(0, len(ansList)):
        print(ansList[::-1][i])
        if ansList[::-1][i] != "":
            ans = len(ansList[::-1][i])
            break

print(ans)