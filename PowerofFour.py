num = 16

ans = False
if num > 2 ** 32:
    ans = False

while num % 4 == 0:
    num /= 4 

if num == 1:
    ans = True
    print(ans)

else:   
    print(ans)