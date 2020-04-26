nums = [2, 2, 3, 1, 0, 1]
nums.sort()
print(nums)
ans = nums[0]
for ele in nums:
    if ele < ans:
        ans = ele

print(ans)

print(min(nums))