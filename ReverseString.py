s = ["H", "e", "l", "l", "o"]

t = ""
for i in range(1, len(s)//2 + 1):
    t = s[i - 1]
    s[i - 1] = s[-i]
    s[-i] = t

print(s)