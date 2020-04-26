nums = [2, 0, 1, 2, 1, 0]

t = 1
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            t = nums[i]
            nums[i] = nums[j]
            nums[j] = t

print(nums)