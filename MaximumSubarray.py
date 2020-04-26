# nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [-2, 1]
# nums = [1]

if len(nums) < 4:
    ans = sum(nums)
    for ele in nums:
        if ele > sum(nums):
            ans = ele
    print(ans)

else:
    ansList = []
    ans = 0
    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums)):
            ansList.append((nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3]))

    print(max(ansList))