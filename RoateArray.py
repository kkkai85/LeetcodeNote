nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

nums[:] = nums[len(nums) - (k % len(nums)):] + nums[:len(nums) - (k % len(nums))]
print(nums)