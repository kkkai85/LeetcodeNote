nums = [2, 11, 15, 7, 7]
target = 18

ans = []
for y in range(0, len(nums) - 1):
    # print(y)
    for i in range(y + 1, len(nums)):
        # print(nums[i])
        if nums[y] + nums[i] == target:
            ans.append(y)
            ans.append(i)
            break

print(ans)