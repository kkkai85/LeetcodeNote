digits = [9, 9, 9, 9]
# digits = [4, 3, 2, 1]
# digits = [0]
# digits = []

for i in range(len(digits) - 1, -1, -1):
    if digits[i] < 9:
        digits[i] += 1
        break

    digits[i] = 0

    if i == 0:
        digits = [1] + digits
        break

print(digits)