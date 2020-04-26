A = "ababaa"
B = "ababcc"

ans = False
# 長度不同
if len(A) != len(B):
    ans = False

# 字串相等
if A == B:
    seen = set()
    for a in A:
        if a in seen:
            ans = True
        seen.add(a)

else:
    pairs = []
    for (a, b) in zip(A, B):
        if a != b:
            pairs.append((a, b))
        if len(pairs) >= 3: ans = False
    ans = True if len(pairs) == 2 and pairs[0] == pairs[1][::-1] else False

print(ans)