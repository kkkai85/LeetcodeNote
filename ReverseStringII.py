s = "abcdefg"
k = 2

for i in range(0, len(s), k * 2):
    print(i)
    s = s[:i] + s[i:i + k:][::-1] + s[i + k:]

print(s)