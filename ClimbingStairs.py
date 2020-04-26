n = 15

step = [0, 1, 2]
for i in range(3, n + 1):
    step.append(step[i - 1] + step[i - 2])

print(step[n])