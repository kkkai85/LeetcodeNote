num1, num2 = "123", "456"

def strToint(_str):
    value = {
        "0" : 0,
        "1" : 1,
        "2" : 2,
        "3" : 3,
        "4" : 4,
        "5" : 5,
        "6" : 6,
        "7" : 7,
        "8" : 8,
        "9" : 9,
    }
    Int = 0
    for digit in _str:
        Int = Int * 10 + value[digit]

    return Int

n1 = strToint(num1)
n2 = strToint(num2)
print(str(n1 * n2))