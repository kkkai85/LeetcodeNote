intervals = [[1, 3], [2, 6], [8, 16], [15, 18]]
# intervals = [[1, 4], [0, 2]]
# intervals = [[1, 4], [0, 1]]
# intervals = [[1, 3]]

# 先依照大小作排序
intervals.sort()

# [S, E]
refS, refE, newIntervals = intervals[0][0], intervals[0][1], list()
for i in range(1, len(intervals)):
    curS, curE = intervals[i][0], intervals[i][1]

    if curS <= refE:
        refE = max(refE, curE)

    else:
        newIntervals.append([refS, refE])
        refS, refE = curS, curE

newIntervals.append([refS, refE])
print(newIntervals)