Integer = {
    1 : "I",
    5 : "V",
    10 : "X",
    50 : "L",
    100 : "C",
    500 : "D",
    1000 : "M"
}

keys = list(Integer.keys())
print(keys)

Input = 58
ans = ""

m = 1
while Input != 0:
    a = Input % 10

    if a == 4:
        ans = Integer[keys[m - 1]] + Integer[keys[m]] + ans

    elif a == 9:
        ans = Integer[keys[m - 1]] + Integer[keys[m + 1]] + ans
    
    elif 1 <= a < 4:
        ans = Integer[keys[m - 1]] * a + ans

    elif 5 <= a < 9:
        ans = Integer[keys[m]] + Integer[keys[m - 1]] * (a - 5) + ans

    m += 2
    Input //= 10

print(ans)