num = 0

def factorization(num):
    if num % 2 == 0:
        if num == 2:
            return True
        return factorization(num // 2) 

    elif num % 3 == 0:
        if num == 3:
            return True
        return factorization(num // 3) 

    elif num % 5 == 0:
        if num == 5:
            return True
        return factorization(num // 5) 

    else:
        return False

if num == 0:
    print(False)

elif num == 1:
    print(True)

else:
    print(factorization(num))